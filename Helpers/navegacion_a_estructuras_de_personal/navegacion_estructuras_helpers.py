from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def ir_a_pagina_inicial(driver):

    wait = WebDriverWait(driver, 30)

    boton_home = wait.until(
        EC.presence_of_element_located(
            (By.ID, "pt1:_UIShome")
        )
    )

    driver.execute_script("arguments[0].click();", boton_home)

    time.sleep(1)

def seleccionar_mis_grupos_clientes(driver):

    wait = WebDriverWait(driver, 30)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "groupNode_workforce_management")
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

def seleccionar_estructuras_personal(driver):

    wait = WebDriverWait(driver, 30)

    modulo = wait.until(
        EC.presence_of_element_located(
            (By.ID, "itemNode_workforce_management_workforce_structures_0")
        )
    )

    # Scroll para que visualmente aparezca el icono
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        modulo
    )


    # Click en Estructuras de personal
    driver.execute_script(
        "arguments[0].click();",
        modulo
    )

    time.sleep(1)