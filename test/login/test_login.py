from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from Helpers.login.login_helpers import login


def test_login_exitoso(driver, credenciales_hcm):

    usuario, password = credenciales_hcm

    login(driver, usuario, password)

    wait = WebDriverWait(driver, 40)

    wait.until(
        EC.url_contains("AtkHomePageWelcome")
    )

    assert "AtkHomePageWelcome" in driver.current_url


@pytest.mark.parametrize(
    "caso",
    [
        "password_incorrecta",
        "usuario_incorrecto",
        "usuario_mal_formado",
        "usuario_vacio",
        "password_vacio",
    ],
)
def test_login_negativo(driver, credenciales_hcm, caso):
    usuario_valido, password_valido = credenciales_hcm
    datos = {
        "password_incorrecta": (usuario_valido, "password_incorrecta"),
        "usuario_incorrecto": ("usuario.incorrecto@example.com", password_valido),
        "usuario_mal_formado": ("usuario.incorrecto", password_valido),
        "usuario_vacio": ("", password_valido),
        "password_vacio": (usuario_valido, ""),
    }
    usuario, password = datos[caso]

    login(driver, usuario, password)

    wait = WebDriverWait(driver, 20)

    wait.until(
        lambda d:
        "signin" in d.current_url
        or len(
            d.find_elements(
                By.CSS_SELECTOR,
                "[role='alert'], .oj-message-summary, .oj-message-detail"
            )
        ) > 0
    )

    assert "signin" in driver.current_url

    #Para correr solo login: pytest test/login -v -s
