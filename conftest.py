import os

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Helpers.login.login_helpers import login
from Helpers.navegacion_a_estructuras_de_personal.navegacion_estructuras_helpers import (
    ir_a_pagina_inicial,
    seleccionar_estructuras_personal,
    seleccionar_mis_grupos_clientes,
)


@pytest.fixture
def credenciales_hcm():
    usuario = os.environ.get("HCM_USER")
    password = os.environ.get("HCM_PASSWORD")

    if not usuario or not password:
        pytest.skip("Configura HCM_USER y HCM_PASSWORD para ejecutar estos tests.")

    return usuario, password


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def sesion_hcm(driver, credenciales_hcm):
    usuario, password = credenciales_hcm

    login(driver, usuario, password)

    WebDriverWait(driver, 40).until(
        EC.url_contains("AtkHomePageWelcome")
    )

    assert "AtkHomePageWelcome" in driver.current_url

    return driver


@pytest.fixture
def estructuras_personal(sesion_hcm):
    ir_a_pagina_inicial(sesion_hcm)
    seleccionar_mis_grupos_clientes(sesion_hcm)
    seleccionar_estructuras_personal(sesion_hcm)

    return sesion_hcm
