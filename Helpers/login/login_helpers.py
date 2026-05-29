from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ejig-test.fa.em2.oraclecloud.com/fscmUI/faces/AtkHomePageWelcome"

def login(driver, usuario, password):

    wait = WebDriverWait(driver, 30)

    driver.get(URL)

    # USERNAME
    usuario_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "idcs-signin-basic-signin-form-username|input")
        )
    )

    usuario_input.clear()
    usuario_input.send_keys(usuario)

    # PASSWORD
    password_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "idcs-signin-basic-signin-form-password|input")
        )
    )

    password_input.clear()
    password_input.send_keys(password)

    # BOTON LOGIN
    boton_login = wait.until(
        EC.presence_of_element_located(
            (By.ID, "idcs-signin-basic-signin-form-submit")
        )
    )

    driver.execute_script("arguments[0].click();", boton_login)