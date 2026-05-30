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


def pytest_addoption(parser):
    parser.addoption(
        "--posicion-busqueda",
        action="store",
        default="Sucursal Microcentro",
        help="Texto para buscar posiciones.",
    )
    parser.addoption(
        "--nombre-posicion",
        action="store",
        default="Prueba QA Jesus",
        help="Nombre de posicion para crear, buscar o modificar.",
    )
    parser.addoption(
        "--posicion-eliminar",
        action="store",
        default=None,
        help="Nombre de posicion a eliminar. Si no se informa, usa --nombre-posicion.",
    )
    parser.addoption(
        "--fecha-vigencia",
        action="store",
        default="19/01/2026",
        help="Fecha de inicio de vigencia para crear posicion.",
    )
    parser.addoption(
        "--fecha-filtro",
        action="store",
        default="01/01/2024",
        help="Fecha usada en filtros de posicion.",
    )
    parser.addoption(
        "--codigo-posicion-principal",
        action="store",
        default="300016",
        help="Codigo de posicion principal para filtros.",
    )
    parser.addoption(
        "--nombre-posicion-principal",
        action="store",
        default="Relaciones Laborales, Liquidaciones y Servicios de Salud - Resp. Relaciones Laborales, Liquidaci\u00f3n y Servicios de Salud",
        help="Nombre de posicion principal para filtros.",
    )


@pytest.fixture
def posicion_busqueda(request):
    return request.config.getoption("--posicion-busqueda")


@pytest.fixture
def nombre_posicion(request):
    return request.config.getoption("--nombre-posicion")


@pytest.fixture
def posicion_eliminar(request, nombre_posicion):
    return request.config.getoption("--posicion-eliminar") or nombre_posicion


@pytest.fixture
def fecha_vigencia(request):
    return request.config.getoption("--fecha-vigencia")


@pytest.fixture
def fecha_filtro(request):
    return request.config.getoption("--fecha-filtro")


@pytest.fixture
def codigo_posicion_principal(request):
    return request.config.getoption("--codigo-posicion-principal")


@pytest.fixture
def nombre_posicion_principal(request):
    return request.config.getoption("--nombre-posicion-principal")


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
