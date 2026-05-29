from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Helpers.login.login_helpers import login

from Helpers.navegacion_a_estructuras_de_personal.navegacion_estructuras_helpers import (
    ir_a_pagina_inicial,
    seleccionar_mis_grupos_clientes,
    seleccionar_estructuras_personal
)

from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
    buscador_posiciones
)


def test_buscador_posiciones(driver, credenciales_hcm):

    usuario, password = credenciales_hcm

    login(driver, usuario, password)

    wait = WebDriverWait(driver, 40)

    wait.until(
        EC.url_contains("AtkHomePageWelcome")
    )

    assert "AtkHomePageWelcome" in driver.current_url

    ir_a_pagina_inicial(driver)

    seleccionar_mis_grupos_clientes(driver)

    seleccionar_estructuras_personal(driver)

    seleccionar_posiciones(driver)

    buscador_posiciones(driver, "Sucursal Microcentro")

    assert True

    #Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\01_test_buscador.py::test_buscador_posiciones -v -s
