from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def seleccionar_posiciones(driver):

    wait = WebDriverWait(driver, 40)

    posiciones = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:0:ll01Upl:UPsp1:ll01Pce:ll01Itr:0:ll02Pce:ll01Lv:0:ll01Pse:ll01Cl"
            )
        )
    )

    driver.execute_script("arguments[0].click();", posiciones)

    wait.until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    selectores_buscador = [
        (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input"),
        (By.CSS_SELECTOR, "input[id='ojHcmAdvancedSearchBox_position-adv-srch|input']"),
        (By.CSS_SELECTOR, "input[id*='AdvancedSearchBox'][id$='|input']"),
        (By.CSS_SELECTOR, "input[id*='position'][id$='|input']"),
        (By.XPATH, "//input[contains(@id,'ojHcmAdvancedSearchBox') and contains(@id,'position')]"),
        (By.XPATH, "//input[contains(@placeholder,'Buscar')]"),
        (By.XPATH, "//input[contains(@aria-label,'Buscar')]"),
        (By.XPATH, "//input[contains(@aria-label,'Search')]"),
    ]

    fin = time.monotonic() + 60

    while time.monotonic() < fin:
        for selector in selectores_buscador:
            elementos = driver.find_elements(*selector)

            for elemento in elementos:
                if elemento.is_displayed() and elemento.is_enabled():
                    return elemento

        time.sleep(1)

    raise AssertionError(
        "No se encontro el buscador de Posiciones despues de seleccionar el modulo."
    )

def obtener_buscador_posiciones(driver):

    wait = WebDriverWait(driver, 40)

    return wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[id*='AdvancedSearchBox'][id$='|input']"
            )
        )
    )

def buscador_posiciones(driver, valor_buscador):

    wait = WebDriverWait(driver, 40)

    buscador = obtener_buscador_posiciones(driver)

    buscador.clear()

    buscador.send_keys(valor_buscador)

    buscador.send_keys(Keys.ENTER)

    return wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(normalize-space(), '{valor_buscador}')]")
        )
    )
