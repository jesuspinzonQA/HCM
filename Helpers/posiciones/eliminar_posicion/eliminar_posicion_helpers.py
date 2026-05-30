import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def texto_xpath(texto):
    if "'" not in texto:
        return f"'{texto}'"

    partes = texto.split("'")
    return "concat(" + ', "\"\'\"", '.join(f"'{parte}'" for parte in partes) + ")"


def click_con_javascript(driver, elemento):
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elemento)
    driver.execute_script("arguments[0].click();", elemento)


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

    time.sleep(2)


def seleccionar_posicion_a_eliminar(driver, nombre_posicion):

    wait = WebDriverWait(driver, 40)
    nombre = texto_xpath(nombre_posicion)

    posicion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//td[contains(@class,'oj-table-data-cell')]//a[.//span[normalize-space()={nombre}]]"
            )
        )
    )

    click_con_javascript(driver, posicion)

    wait.until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def presionar_boton_mas_acciones(driver):

    wait = WebDriverWait(driver, 40)

    boton_mas_acciones = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-label='Más acciones'] | //button[@aria-label='Mas acciones'] | //button[.//span[contains(@class,'oj-ux-ico-overflow-h')]]"
            )
        )
    )

    click_con_javascript(driver, boton_mas_acciones)

    time.sleep(1)


def seleccionar_suprimir_posicion(driver):

    wait = WebDriverWait(driver, 40)

    opcion_suprimir = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@role='menuitem' and @data-oj-label='Suprimir posición'] | "
                "//a[@role='menuitem' and @data-oj-key='pageGeneralHeader_h_delete_position_action'] | "
                "//*[@role='menuitem'][.//span[normalize-space()='Suprimir posición']]"
            )
        )
    )

    click_con_javascript(driver, opcion_suprimir)

    time.sleep(1)


def confirmar_suprimir_posicion(driver):

    wait = WebDriverWait(driver, 40)

    boton_suprimir = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#deletePositionDialog_deleteConfirm button"
            )
        )
    )

    click_con_javascript(driver, boton_suprimir)

    time.sleep(2)


def volver_al_buscador_posiciones(driver):

    for _ in range(3):
        try:
            wait = WebDriverWait(driver, 5)

            return wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
                )
            )

        except TimeoutException:
            driver.back()

    wait = WebDriverWait(driver, 20)

    return wait.until(
        EC.visibility_of_element_located(
            (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
        )
    )


def buscar_posicion_eliminada(driver, nombre_posicion):

    buscador = volver_al_buscador_posiciones(driver)

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", buscador)
    driver.execute_script("arguments[0].focus();", buscador)
    driver.execute_script(
        """
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """,
        buscador
    )

    buscador.send_keys(nombre_posicion)
    buscador.send_keys(Keys.ENTER)

    time.sleep(15)


def posicion_sigue_visible(driver, nombre_posicion):

    wait = WebDriverWait(driver, 10)
    nombre = texto_xpath(nombre_posicion)

    try:
        wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//td[contains(@class,'oj-table-data-cell')]//a[.//span[normalize-space()={nombre}]]"
                )
            )
        )

        return True

    except TimeoutException:
        return False
