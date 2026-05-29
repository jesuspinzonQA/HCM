from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def abrir_boton_filtros(driver):

    wait = WebDriverWait(driver, 40)

    boton_filtros = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@role='listitem' and normalize-space(.)='Filtros']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_filtros
    )


    driver.execute_script(
        "arguments[0].click();",
        boton_filtros
    )

    time.sleep(5)

def seleccionar_fecha_vigencia_filtro(driver, fecha):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Fecha de vigencia"
    seccion_fecha = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Fecha de vigencia']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_fecha
    )


    driver.execute_script(
        "arguments[0].click();",
        seccion_fecha
    )


    # 2. Buscar input fecha
    campo_fecha = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[contains(@id,'EffectiveDate')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_fecha
    )


    driver.execute_script(
        "arguments[0].click();",
        campo_fecha
    )

    # 3. Limpiar campo
    campo_fecha.send_keys(Keys.CONTROL + "a")
    campo_fecha.send_keys(Keys.DELETE)

    # 4. Agregar fecha
    campo_fecha.send_keys(fecha)


    # 5. ENTER
    campo_fecha.send_keys(Keys.ENTER)

    time.sleep(1)

def seleccionar_estado_activa(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Estado"
    seccion_estado = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Estado']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_estado
    )


    driver.execute_script(
        "arguments[0].click();",
        seccion_estado
    )


    # 2. Seleccionar checkbox "Activa"
    checkbox_activa = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='checkbox' and @name='Status' and @value='Activa']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        checkbox_activa
    )


    driver.execute_script(
        "arguments[0].click();",
        checkbox_activa
    )


    # 3. Validar selección
    assert checkbox_activa.is_selected(), \
        "El checkbox 'Activa' no quedó seleccionado"

    # 4. ENTER
    checkbox_activa.send_keys(Keys.ENTER)

    time.sleep(1)

def seleccionar_titulares(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Titulares"
    seccion_titulares = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Titulares']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_titulares
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_titulares
    )


    # 2. Campo Nombre de titular
    campo_nombre_titular = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "IncumbentName|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_nombre_titular
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_nombre_titular
    )

    campo_nombre_titular.send_keys(Keys.CONTROL + "a")
    campo_nombre_titular.send_keys(Keys.DELETE)
    campo_nombre_titular.send_keys("Jose Miguel")


    # 3. Ir al campo "Número de persona titular"
    ActionChains(driver).send_keys(Keys.TAB).perform()

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 4. Seleccionar radio "Posiciones con titulares"
    radio_titulares = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='radio' and @name='HasIncumbent' and @value='true']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        radio_titulares
    )

    driver.execute_script(
        "arguments[0].click();",
        radio_titulares
    )

    # 5. Salir del campo "Número de persona titular"
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)
    
def seleccionar_posicion_principal(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Posición principal"
    seccion_posicion_principal = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Posición principal']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_posicion_principal
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_posicion_principal
    )


    # 2. Campo Código de posición principal
    campo_codigo_posicion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[@role='combobox' and contains(@aria-controls,'dropdown')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_codigo_posicion
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_codigo_posicion
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = '300815';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_codigo_posicion)


    # Seleccionar fila/opción código 300815
    fila_codigo = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'300815')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_codigo
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_codigo
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

    # 3. Campo Nombre de posición principal
    campo_nombre_posicion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_nombre_posicion
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_nombre_posicion
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'Sucursal La Plata Norte - Gerente de sucursal';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_nombre_posicion)


    # Seleccionar fila/opción nombre posición principal
    fila_nombre = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'Sucursal La Plata Norte - Gerente de sucursal')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_nombre
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_nombre
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)

def seleccionar_puesto(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Puesto"
    seccion_puesto = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Puesto']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_puesto
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_puesto
    )


    # 2. Campo Código de puesto
    campo_codigo_puesto = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[3]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_codigo_puesto
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_codigo_puesto
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = '30000530';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_codigo_puesto)


    fila_codigo_puesto = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'30000530')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_codigo_puesto
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_codigo_puesto
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()


    # 3. Campo Nombre de puesto
    campo_nombre_puesto = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[4]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_nombre_puesto
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_nombre_puesto
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'Contador/Cajero';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_nombre_puesto)


    fila_nombre_puesto = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'Contador/Cajero')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_nombre_puesto
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_nombre_puesto
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_departamento(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Departamento"
    seccion_departamento = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Departamento']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_departamento
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_departamento
    )


    # 2. Campo Departamento
    campo_departamento = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[5]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_departamento
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_departamento
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'Sucursal La Plata Norte';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_departamento)


    fila_departamento = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'Sucursal La Plata Norte')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_departamento
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_departamento
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_ubicacion(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Ubicación"
    seccion_ubicacion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Ubicación']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_ubicacion
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_ubicacion
    )


    # 2. Campo Código de ubicación
    campo_codigo_ubicacion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[6]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_codigo_ubicacion
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_codigo_ubicacion
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'SUC-871';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_codigo_ubicacion)


    fila_codigo_ubicacion = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'SUC-871')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_codigo_ubicacion
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_codigo_ubicacion
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()


    # 3. Campo Nombre de ubicación
    campo_nombre_ubicacion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[7]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_nombre_ubicacion
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_nombre_ubicacion
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'La Plata Norte';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_nombre_ubicacion)


    fila_nombre_ubicacion = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'La Plata Norte')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_nombre_ubicacion
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_nombre_ubicacion
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_unidad_negocio(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Unidad de negocio"
    seccion_unidad_negocio = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Unidad de negocio']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_unidad_negocio
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_unidad_negocio
    )


    # 2. Campo Unidad de negocio
    campo_unidad_negocio = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@role='combobox' and contains(@aria-controls,'dropdown')])[8]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_unidad_negocio
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_unidad_negocio
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'Personal Banking';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_unidad_negocio)


    fila_unidad_negocio = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[contains(normalize-space(.),'Personal Banking')]/ancestor::div[contains(@class,'FlexStyles_baseStyles')][1]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        fila_unidad_negocio
    )

    driver.execute_script(
        "arguments[0].click();",
        fila_unidad_negocio
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_estado_contratacion(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección Estado de contratación
    seccion_estado_contratacion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Estado de contratación']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_estado_contratacion
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_estado_contratacion
    )


    # 2. Seleccionar checkbox "Aprobada"
    checkbox_aprobada = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='checkbox' and @name='HiringStatus' and @value='Aprobada']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        checkbox_aprobada
    )


    driver.execute_script(
        "arguments[0].click();",
        checkbox_aprobada
    )


    # 3. Pasar a la siguiente sección sin cerrar Estado de contratación
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_tipo(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Tipo"
    seccion_tipo = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Tipo']"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", seccion_tipo)
    driver.execute_script("arguments[0].click();", seccion_tipo)


    # 2. Seleccionar checkbox "Titular individual"
    checkbox_titular_individual = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@type='checkbox' and @name='Type' and @value='Titular individual']"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", checkbox_titular_individual)
    driver.execute_script("arguments[0].click();", checkbox_titular_individual)


    # 3. Salir del checkbox y pasar a la siguiente sección
    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_posicion(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Abrir sección "Posición"
    seccion_posicion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'oj-collapsible-header') and normalize-space(.)='Posición']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_posicion
    )

    driver.execute_script(
        "arguments[0].click();",
        seccion_posicion
    )


    # 2. Campo Código
    campo_codigo = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "PositionCode|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_codigo
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_codigo
    )

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = '300819';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_codigo)

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    time.sleep(1)

    # 3. Campo Nombre
    campo_nombre = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "PositionName|input"
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

    driver.execute_script("""
        arguments[0].focus();
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].value = 'sucursal la plata';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, campo_nombre)

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    time.sleep(1)

def presionar_ver_resultados(driver):

    wait = WebDriverWait(driver, 40)

    # Botón "Ver resultados"
    boton_ver_resultados = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(normalize-space(.),'Ver resultados')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_ver_resultados
    )

    driver.execute_script(
        "arguments[0].click();",
        boton_ver_resultados
    )

    time.sleep(1)