import os

import pytest
from selenium import webdriver


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
