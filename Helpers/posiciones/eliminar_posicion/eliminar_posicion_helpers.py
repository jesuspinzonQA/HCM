import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def buscar_y_seleccionar_posicion_por_nombre(driver, nombre_posicion):
    posicion = buscar_posicion_a_eliminar(driver, nombre_posicion)
    _click_js(driver, posicion)


def abrir_posicion(driver, nombre_posicion):
    buscar_y_seleccionar_posicion_por_nombre(driver, nombre_posicion)


def abrir_menu_acciones(driver):
    boton_acciones = _primer_clickable(
        driver,
        [
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


def eliminar_posicion(driver, nombre_posicion):
    abrir_posicion(driver, nombre_posicion)
    abrir_menu_acciones(driver)
    seleccionar_opcion_eliminar(driver)
    confirmar_eliminacion(driver)
