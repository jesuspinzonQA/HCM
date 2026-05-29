from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def seleccionar_posiciones(driver):

    wait = WebDriverWait(driver, 30)

    posiciones = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:0:ll01Upl:UPsp1:ll01Pce:ll01Itr:0:ll02Pce:ll01Lv:0:ll01Pse:ll01Cl"
            )
        )
    )

    driver.execute_script("arguments[0].click();", posiciones)

    time.sleep(1)

def buscador_posiciones(driver, valor_buscador):

    wait = WebDriverWait(driver, 30)

    buscador = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
        )
    )

    buscador.clear()

    buscador.send_keys(valor_buscador)

    time.sleep(1)

    buscador.send_keys(Keys.ENTER)

    time.sleep(1)