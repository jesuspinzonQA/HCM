from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Helpers.login.login_helpers import login

from Helpers.navegacion_a_estructuras_de_personal.navegacion_estructuras_helpers import (
    ir_a_pagina_inicial,
    seleccionar_mis_grupos_clientes,
    seleccionar_estructuras_personal
)

def test_navegacion_estructuras_personal(driver, credenciales_hcm):

    usuario, password = credenciales_hcm

    # LOGIN
    login(driver, usuario, password)

    wait = WebDriverWait(driver, 40)

    wait.until(
        EC.url_contains("AtkHomePageWelcome")
    )

    assert "AtkHomePageWelcome" in driver.current_url

    # IR A PAGINA INICIAL
    ir_a_pagina_inicial(driver)

    # INGRESAR A MIS GRUPOS DE CLIENTES
    seleccionar_mis_grupos_clientes(driver)

    # INGRESAR A ESTRUCTURAS DE PERSONAL
    seleccionar_estructuras_personal(driver)


#Para correr solamente este test: pytest test\modulo_estructuras_de_personal\00_navegacion_estructuras\navegacion_estructuras.py::test_navegacion_estructuras_personal -v -s
