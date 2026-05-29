from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def seleccionar_filtro_fecha_vigencia(driver, fecha):
    wait = WebDriverWait(driver, 40)

    # 1. Click en el filtro Fecha de vigencia
    filtro = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@aria-label='Filtro sugerido Etiqueta: Fecha de vigencia']")
        )
    )
    driver.execute_script("arguments[0].click();", filtro)

    # 2. Esperar y buscar el input por el label asociado
    campo_fecha = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[.//span[normalize-space()='Fecha de vigencia']]/following::input[@role='combobox'][1]"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", campo_fecha)
    driver.execute_script("arguments[0].click();", campo_fecha)

    # 3. Limpiar y escribir fecha
    campo_fecha.send_keys(Keys.CONTROL + "a")
    campo_fecha.send_keys(Keys.DELETE)
    campo_fecha.send_keys(fecha)
    campo_fecha.send_keys(Keys.ENTER)

    time.sleep(4)

def seleccionar_filtro_estado_activa(driver):
    wait = WebDriverWait(driver, 40)

    # 1. Click en filtro Estado
    filtro_estado = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@aria-label='Filtro sugerido Etiqueta: Estado']")
        )
    )
    driver.execute_script("arguments[0].click();", filtro_estado)

    # 2. Click en el label de Activa
    label_activa = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//label[.//oj-option[contains(normalize-space(.),'Activa')]]"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", label_activa)
    driver.execute_script("arguments[0].click();", label_activa)

    # 3. Validar checkbox seleccionado
    checkbox_activa = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='checkbox' and @name='Status' and @value='Activa']")
        )
    )

    assert checkbox_activa.is_selected(), "El checkbox Activa no quedó seleccionado"

    # 4. Presionar ENTER
    checkbox_activa.send_keys(Keys.ENTER)

    time.sleep(5)

def seleccionar_filtro_titular_posiciones_con_titulares(driver):
    wait = WebDriverWait(driver, 40)

    # 1. Buscar el filtro Titular por texto visible
    filtro_titular = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='listitem' and normalize-space(.)='Titular']"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", filtro_titular)
    driver.execute_script("arguments[0].click();", filtro_titular)

    # 2. Seleccionar radio "Posiciones con titulares"
    radio_titular = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='radio' and @name='HasIncumbent' and @value='true']"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", radio_titular)
    driver.execute_script("arguments[0].click();", radio_titular)

    # 3. Validar que quedó seleccionado
    assert radio_titular.is_selected(), "El radio 'Posiciones con titulares' no quedó seleccionado"

    # 4. Presionar ENTER
    radio_titular.send_keys(Keys.ENTER)

    time.sleep(5)

def seleccionar_filtro_codigo_posicion_principal(driver, codigo):
    wait = WebDriverWait(driver, 40)

    filtro_codigo = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@role='listitem' and contains(.,'Código de posición principal')]")
        )
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", filtro_codigo)
    driver.execute_script("arguments[0].click();", filtro_codigo)

    campo_codigo = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@role='combobox']")
        )
    )

    driver.execute_script("arguments[0].click();", campo_codigo)
    campo_codigo.send_keys(Keys.CONTROL + "a")
    campo_codigo.send_keys(Keys.DELETE)
    campo_codigo.send_keys(codigo)

    opcion_codigo = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(normalize-space(.),'{codigo}')]")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", opcion_codigo)
    driver.execute_script("arguments[0].click();", opcion_codigo)

    campo_codigo.send_keys(Keys.ENTER)

    time.sleep(5)

def seleccionar_filtro_nombre_posicion_principal(driver, nombre_posicion):

    wait = WebDriverWait(driver, 40)

    # 1. Seleccionar filtro "Nombre de posición principal"
    filtro_nombre = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='listitem' and contains(.,'Nombre de posición principal')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        filtro_nombre
    )

    driver.execute_script(
        "arguments[0].click();",
        filtro_nombre
    )

    # 2. Buscar input combobox
    campo_nombre = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[@role='combobox']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_nombre
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_nombre
    )

    # 3. Limpiar campo
    campo_nombre.send_keys(Keys.CONTROL + "a")
    campo_nombre.send_keys(Keys.DELETE)

    # 4. Escribir nombre posición
    campo_nombre.send_keys(nombre_posicion)

    # Esperar resultados
    time.sleep(2)

    # 5. Seleccionar opción/checkbox
    opcion_nombre = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//*[contains(normalize-space(.),'{nombre_posicion}')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        opcion_nombre
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion_nombre
    )

    # 6. ENTER
    campo_nombre.send_keys(Keys.ENTER)

    time.sleep(5)

def seleccionar_filtro_estado_contratacion_aprobada(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Click en flecha hacia la derecha / Siguiente
    flecha_siguiente = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@role='button' and @title='Siguiente']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        flecha_siguiente
    )

    # 2. Seleccionar filtro "Estado de contratación"
    filtro_estado_contratacion = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='listitem' and contains(.,'Estado de contratación')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        filtro_estado_contratacion
    )

    driver.execute_script(
        "arguments[0].click();",
        filtro_estado_contratacion
    )

    # 3. Seleccionar checkbox "Aprobada"
    checkbox_aprobada = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='checkbox' and @name='HiringStatus' and @value='Aprobada']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        checkbox_aprobada
    )

    assert checkbox_aprobada.is_selected(), \
        "El checkbox 'Aprobada' no quedó seleccionado"

    # 4. ENTER
    checkbox_aprobada.send_keys(Keys.ENTER)

    time.sleep(5)

def seleccionar_filtro_tipo_titular_individual(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Seleccionar filtro "Tipo"
    filtro_tipo = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@role='listitem' and normalize-space(.)='Tipo']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", filtro_tipo)
    driver.execute_script("arguments[0].click();", filtro_tipo)

    # 2. Seleccionar checkbox "Titular individual"
    checkbox_titular_individual = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='checkbox' and @name='Type' and @value='Titular individual']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        checkbox_titular_individual
    )

    driver.execute_script(
        "arguments[0].click();",
        checkbox_titular_individual
    )

    # 3. Validar selección
    assert checkbox_titular_individual.is_selected(), \
        "El checkbox 'Titular individual' no quedó seleccionado"

    # 4. ENTER
    checkbox_titular_individual.send_keys(Keys.ENTER)

    time.sleep(5)

def presionar_boton_borrar(driver):

    wait = WebDriverWait(driver, 40)

    boton_borrar = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(normalize-space(.),'Borrar')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_borrar
    )

    driver.execute_script(
        "arguments[0].click();",
        boton_borrar
    )

    time.sleep(2)