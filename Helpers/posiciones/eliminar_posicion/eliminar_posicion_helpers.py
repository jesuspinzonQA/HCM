import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def _xpath_text(texto):
    if "'" not in texto:
        return f"'{texto}'"
    partes = texto.split("'")
    return "concat(" + ', "\"\'\"", '.join(f"'{parte}'" for parte in partes) + ")"


def _click_js(driver, elemento):
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elemento)
    driver.execute_script("arguments[0].click();", elemento)


def _primer_clickable(driver, locators, timeout=40):
    fin = time.monotonic() + timeout

    while time.monotonic() < fin:
        for by, selector in locators:
            elementos = driver.find_elements(by, selector)
            for elemento in elementos:
                if elemento.is_displayed() and elemento.is_enabled():
                    return elemento
        time.sleep(0.5)

    raise TimeoutError("No se encontro ningun elemento clickable con los selectores informados.")


def buscar_posicion_a_eliminar(driver, nombre_posicion):
    wait = WebDriverWait(driver, 40)

    buscador = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
        )
    )

    buscador.clear()
    buscador.send_keys(nombre_posicion)
    buscador.send_keys(Keys.ENTER)

    texto = _xpath_text(nombre_posicion)
    return wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'oj-table-data-cell')]//a[.//span[normalize-space()={texto}]]",
            )
        )
    )


def _obtener_buscador_posiciones(driver, timeout=15):
    wait = WebDriverWait(driver, timeout)
    return wait.until(
        EC.visibility_of_element_located(
            (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
        )
    )


def _volver_al_buscador_si_es_necesario(driver):
    for _ in range(3):
        try:
            return _obtener_buscador_posiciones(driver, timeout=5)
        except TimeoutException:
            driver.back()

    return _obtener_buscador_posiciones(driver, timeout=20)


def buscar_y_seleccionar_posicion_por_nombre(driver, nombre_posicion):
    posicion = buscar_posicion_a_eliminar(driver, nombre_posicion)
    _click_js(driver, posicion)
    WebDriverWait(driver, 40).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def abrir_posicion(driver, nombre_posicion):
    buscar_y_seleccionar_posicion_por_nombre(driver, nombre_posicion)


def abrir_menu_acciones(driver):
    boton_acciones = _primer_clickable(
        driver,
        [
            (By.XPATH, "//button[@aria-label='Más acciones']"),
            (By.XPATH, "//button[@aria-label='Mas acciones']"),
            (By.XPATH, "//button[.//span[contains(@class,'oj-ux-ico-overflow-h')]]"),
            (By.XPATH, "//button[contains(normalize-space(.),'Acciones')]"),
            (By.XPATH, "//button[contains(normalize-space(.),'Actions')]"),
            (By.XPATH, "//button[contains(@aria-label,'Acciones')]"),
            (By.XPATH, "//button[contains(@aria-label,'Actions')]"),
            (By.XPATH, "//button[contains(@title,'Acciones')]"),
            (By.XPATH, "//button[contains(@title,'Actions')]"),
            (By.XPATH, "//button[contains(@aria-label,'Mas')]"),
            (By.XPATH, "//button[contains(@aria-label,'Más')]"),
            (By.XPATH, "//button[contains(@title,'Mas')]"),
            (By.XPATH, "//button[contains(@title,'Más')]"),
        ],
    )
    _click_js(driver, boton_acciones)


def seleccionar_opcion_eliminar(driver):
    opcion_eliminar = _primer_clickable(
        driver,
        [
            (By.XPATH, "//a[@role='menuitem' and @data-oj-label='Suprimir posición']"),
            (By.XPATH, "//a[@role='menuitem' and @data-oj-key='pageGeneralHeader_h_delete_position_action']"),
            (By.XPATH, "//*[@role='menuitem'][.//span[normalize-space()='Suprimir posición']]"),
            (By.XPATH, "//*[self::a or self::button or @role='menuitem'][contains(normalize-space(.),'Eliminar')]"),
            (By.XPATH, "//*[self::a or self::button or @role='menuitem'][contains(normalize-space(.),'Suprimir')]"),
            (By.XPATH, "//*[self::a or self::button or @role='menuitem'][contains(normalize-space(.),'Delete')]"),
        ],
    )
    _click_js(driver, opcion_eliminar)


def confirmar_eliminacion(driver):
    try:
        boton_confirmar = _primer_clickable(
            driver,
            [
                (By.CSS_SELECTOR, "#deletePositionDialog_deleteConfirm button"),
                (By.ID, "deletePositionDialog_deleteConfirm"),
                (By.XPATH, "//oj-button[@id='deletePositionDialog_deleteConfirm']//button"),
                (By.XPATH, "//button[contains(normalize-space(.),'Eliminar')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'Suprimir')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'Aceptar')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'Si')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'Sí')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'OK')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'Delete')]"),
                (By.XPATH, "//button[contains(normalize-space(.),'Yes')]"),
            ],
            timeout=10,
        )
    except TimeoutError:
        return False

    _click_js(driver, boton_confirmar)
    return True


def posicion_sigue_visible(driver, nombre_posicion):
    buscador = _volver_al_buscador_si_es_necesario(driver)

    buscador.clear()
    buscador.send_keys(nombre_posicion)
    buscador.send_keys(Keys.ENTER)

    texto = _xpath_text(nombre_posicion)

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//td[contains(@class,'oj-table-data-cell')]//a[.//span[normalize-space()={texto}]]",
                )
            )
        )
        return True
    except TimeoutException:
        return False


def eliminar_posicion(driver, nombre_posicion):
    abrir_posicion(driver, nombre_posicion)
    abrir_menu_acciones(driver)
    seleccionar_opcion_eliminar(driver)
    confirmar_eliminacion(driver)
