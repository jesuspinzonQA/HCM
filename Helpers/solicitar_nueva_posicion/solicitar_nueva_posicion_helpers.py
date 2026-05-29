from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def seleccionar_solicitar_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    boton_nueva_posicion = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:0:ll01Upl:UPsp1:ll01Pce:ll01Itr:0:ll02Pce:ll01Lv:1:ll01Pse:ll01Cl"
            )
        )
    )

    # Scroll para visualizar la opción en pantalla
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_nueva_posicion
    )


    # Click en "Solicitar nueva posición"
    driver.execute_script(
        "arguments[0].click();",
        boton_nueva_posicion
    )

    time.sleep(1)

def seleccionar_informacion_adicional_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Buscar sección "Información adicional"
    seccion_informacion_adicional = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(normalize-space(.),'Información adicional')]"
            )
        )
    )

    # Scroll para visualizar la sección
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_informacion_adicional
    )

    # 2. Buscar switch
    switch_informacion_adicional = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='switch' and @aria-label='Información adicional']"
            )
        )
    )

    # Click en el switch
    driver.execute_script(
        "arguments[0].click();",
        switch_informacion_adicional
    )

    time.sleep(1)

def seleccionar_informacion_legislativa_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    # 1. Buscar sección "Información legislativa"
    seccion_informacion_legislativa = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(normalize-space(.),'Información legislativa')]"
            )
        )
    )

    # Scroll para visualizar la sección
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        seccion_informacion_legislativa
    )

    # 2. Buscar switch
    switch_informacion_legislativa = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='switch' and @aria-label='Información legislativa']"
            )
        )
    )

    # Click en el switch
    driver.execute_script(
        "arguments[0].click();",
        switch_informacion_legislativa
    )

    time.sleep(1)

def presionar_boton_continuar_formulario_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    boton_continuar = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-label='Continuar']"
            )
        )
    )

    # Scroll para visualizar el botón
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_continuar
    )

    # Click en Continuar
    driver.execute_script(
        "arguments[0].click();",
        boton_continuar
    )

    time.sleep(1)

def seleccionar_fecha_inicio_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    campo_fecha = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "effectiveStartDateWhenAndWhyInputDate|input")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", campo_fecha)
    driver.execute_script("arguments[0].click();", campo_fecha)

    campo_fecha.send_keys(Keys.CONTROL + "a")
    campo_fecha.send_keys(Keys.DELETE)
    campo_fecha.send_keys("20/05/2026")

    # Pasar al campo motivo
    campo_fecha.send_keys(Keys.TAB)

    time.sleep(1)

def seleccionar_motivo_solicitud(driver):

    wait = WebDriverWait(driver, 40)

    # Como ya venimos con TAB desde fecha, usamos el campo activo
    campo_motivo = driver.switch_to.active_element

    campo_motivo.send_keys("Carga Inicial Posiciones")

    opcion_motivo = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@role='row' and contains(normalize-space(.),'Carga Inicial Posiciones')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion_motivo)

    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def presionar_boton_continuar_detalles_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    boton_continuar = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-label='Continuar']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_continuar
    )

    driver.execute_script(
        "arguments[0].click();",
        boton_continuar
    )

    time.sleep(1)

def seleccionar_posicion_principal(driver):

    wait = WebDriverWait(driver, 40)

    campo_posicion_principal = wait.until(
        EC.presence_of_element_located(
            (By.ID, "parentPositionLovSelect|input")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_posicion_principal
    )

    driver.execute_script(
        "arguments[0].focus(); arguments[0].click();",
        campo_posicion_principal
    )

    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Productos y Serv. Transacc.") \
        .perform()

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(.),'Co-Resp. Prod. y Serv. Transaccionales')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    ActionChains(driver).send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_estado(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Estado
    campo_estado = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "statusLovSelectSingle|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_estado
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_estado
    )

    # Limpiar valor actual y escribir "Activa"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Activa") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_unidad_negocio(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Unidad de negocio
    campo_unidad_negocio = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.BusinessUnitId|input"
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

    # Limpiar valor actual y escribir nuevo valor
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Corp.Banking & Corp.Affairs") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_nombre(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Nombre
    campo_nombre = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.PositionName|input"
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

    # Limpiar y escribir nombre
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("jesus pinzon") \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def saltar_campo_codigo(driver):

    # TAB para saltar el campo Código
    ActionChains(driver) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_departamento(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Departamento
    campo_departamento = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.DepartmentId|input"
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

    # Limpiar valor actual y escribir nuevo valor
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Productos y Serv. Transacc.") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_puesto(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Puesto
    campo_puesto = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.JobId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_puesto
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_puesto
    )

    # Escribir valor y seleccionar desde desplegable
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Analista QARM Sr") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_ubicacion(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Ubicación
    campo_ubicacion = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.LocationId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_ubicacion
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_ubicacion
    )

    # Escribir valor y seleccionar desde desplegable
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Edificio Madero Office") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_tiempo_completo_parcial(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Tiempo completo o tiempo parcial
    campo_tiempo_completo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.FullPartTime|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_tiempo_completo
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_tiempo_completo
    )

    # Limpiar valor actual y seleccionar "Tiempo completo"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Tiempo completo") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_indefinido_temporal(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Indefinido o temporal
    campo_indefinido_temporal = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.RegularTemporary|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_indefinido_temporal
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_indefinido_temporal
    )

    # Limpiar valor actual y seleccionar "Indefinido"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Indefinido") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_horas_laborables_estandar(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Horas laborables estándar
    campo_horas_estandar = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "standardWorkingHoursInputText|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_horas_estandar
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_horas_estandar
    )

    # Limpiar valor actual y escribir 7,5
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("7.5") \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_frecuencia(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Frecuencia
    campo_frecuencia = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_dynform_StandardWorkingHoursGroup_fl_positionsV2.StandardWorkingFrequency|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_frecuencia
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_frecuencia
    )

    # Limpiar valor actual y seleccionar "Diaria"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Diaria") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_horas_laborables(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Horas laborables
    campo_horas_laborables = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "workingHoursInputText|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_horas_laborables
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_horas_laborables
    )

    # Limpiar valor actual y escribir 7,5
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("7.5") \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_frecuencia_horas_laborables(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Frecuencia horas laborables
    campo_frecuencia_horas = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_dynform_WorkingHoursGroup_fl_positionsV2.WorkingHoursFrequency|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_frecuencia_horas
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_frecuencia_horas
    )

    # Limpiar valor actual y seleccionar "Diaria"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Diaria") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_estado_contratacion(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Estado de contratación
    campo_estado_contratacion = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.HiringStatus|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_estado_contratacion
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_estado_contratacion
    )

    # Limpiar valor actual y seleccionar "Aprobada"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Aprobada") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_tipo(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Tipo
    campo_tipo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.PositionType|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_tipo
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_tipo
    )

    # Limpiar valor actual y seleccionar "Titular individual"
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("Titular individual") \
        .pause(2) \
        .send_keys(Keys.ARROW_DOWN) \
        .pause(1) \
        .send_keys(Keys.ENTER) \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def saltar_plan_compensaciones(driver):

    wait = WebDriverWait(driver, 40)

    # Campo "Plan de compensaciones"
    campo_plan = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form--1188403581-1_fl_positionsV2.positionsDFF.ICBCCOMPPLAN|input"
            )
        )
    )

    # Scroll al campo
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_plan
    )

    time.sleep(1)

    # Click en el campo
    driver.execute_script(
        "arguments[0].click();",
        campo_plan
    )

    time.sleep(1)

    # Saltear campo
    ActionChains(driver) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(1)

def seleccionar_plantilla(driver):

    wait = WebDriverWait(driver, 40)

    # Campo Plantilla
    campo_plantilla = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "headCountInputText|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_plantilla
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        campo_plantilla
    )

    time.sleep(1)

    # Limpiar valor actual y escribir 1
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("1") \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(3)

def seleccionar_equivalente_tiempo_completo(driver):

    wait = WebDriverWait(driver, 40)

    # Campo FTE / Plantilla
    campo_fte = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "fteInputText|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_fte
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        campo_fte
    )

    time.sleep(1)

    # Limpiar valor actual y escribir 1
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .send_keys("1") \
        .pause(1) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(3)

def saltar_boton_agregar(driver):

    time.sleep(1)

    # Saltar botón "Agregar"
    ActionChains(driver) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(2)

def saltar_grupo_registro(driver):

    time.sleep(1)

    # Saltar campo "Grupo de registro"
    ActionChains(driver) \
        .send_keys(Keys.TAB) \
        .perform()

    time.sleep(2)

def presionar_boton_continuar_nueva_posicion(driver):

    wait = WebDriverWait(driver, 40)

    # Botón Continuar
    boton_continuar = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-label='Continuar']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_continuar
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        boton_continuar
    )

    time.sleep(3)

def seleccionar_solicitar_cambio_posicion(driver):

    wait = WebDriverWait(driver, 40)

    opcion = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(text(),'Solicitar cambio de posición')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        opcion
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(1)

def buscar_posicion(driver, valor):

    wait = WebDriverWait(driver, 40)

    buscador = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "ojHcmAdvancedSearchBox_position-adv-srch|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        buscador
    )

    driver.execute_script(
        "arguments[0].click();",
        buscador
    )

    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys("a") \
        .key_up(Keys.CONTROL) \
        .send_keys(Keys.DELETE) \
        .perform()

    buscador.send_keys(valor)

    buscador.send_keys(Keys.ENTER)

    time.sleep(1)

def seleccionar_posicion(driver, valor):

    wait = WebDriverWait(driver, 40)

    posicion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//a[contains(normalize-space(), '{valor}')]"
            )
        )
    )

    # Scroll hasta la posición
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        posicion
    )

    # Click
    driver.execute_script(
        "arguments[0].click();",
        posicion
    )

    time.sleep(1)

def seleccionar_informacion_adicional_cambio_posicion(driver):

    wait = WebDriverWait(driver, 40)

    switch = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='switch' and @aria-label='Información adicional']"
            )
        )
    )

    # Scroll
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        switch
    )

    # Click mediante JavaScript
    driver.execute_script(
        "arguments[0].click();",
        switch
    )

    time.sleep(1)

def seleccionar_informacion_legislativa_cambio_posicion(driver):

    wait = WebDriverWait(driver, 40)

    switch = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='switch' and @aria-label='Información legislativa']"
            )
        )
    )

    # Scroll al switch
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        switch
    )

    # Verificar estado
    estado = switch.get_attribute("aria-checked")

    # Activar únicamente si está apagado
    if estado == "false":

        driver.execute_script(
            "arguments[0].click();",
            switch
        )

        time.sleep(1)

def presionar_boton_continuar_cambio_posicion(driver):

    wait = WebDriverWait(driver, 40)

    boton_continuar = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@aria-label='Continuar']"
            )
        )
    )

    # Scroll hasta el botón
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton_continuar
    )

    # Click mediante JavaScript
    driver.execute_script(
        "arguments[0].click();",
        boton_continuar
    )

    time.sleep(1)

def seleccionar_fecha_inicio_cambio_posicion(driver):

    wait = WebDriverWait(driver, 40)
    fecha = "25/05/2026"

    campo_fecha = wait.until(
        EC.presence_of_element_located(
            (By.ID, "effectiveStartDateWhenAndWhyInputDate|input")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_fecha
    )

    driver.execute_script("arguments[0].focus();", campo_fecha)

    driver.execute_script(
        """
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """,
        campo_fecha
    )

    campo_fecha.send_keys(fecha)

    campo_fecha.send_keys(Keys.ENTER)

    campo_fecha.send_keys(Keys.TAB)

def seleccionar_motivo_solicitud_cambio_posicion(driver):

    wait = WebDriverWait(driver, 40)
    valor = "Reorganización"

    campo_motivo = wait.until(
        EC.presence_of_element_located(
            (By.ID, "actionReasonWhenAndWhyPositionChangeId|input")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        campo_motivo
    )

    # Click y foco real
    driver.execute_script("arguments[0].click();", campo_motivo)
    time.sleep(1)

    # Limpiar sin CTRL + A global
    driver.execute_script(
        """
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """,
        campo_motivo
    )

    # Escribir usando teclado activo, no campo_motivo.send_keys()
    ActionChains(driver) \
        .send_keys(valor) \
        .perform()

    # Forzar apertura/búsqueda del desplegable
    ActionChains(driver) \
        .send_keys(Keys.ARROW_DOWN) \
        .perform()

    # Seleccionar opción
    opcion = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[normalize-space()='Reorganización'] | //oj-highlight-text[contains(.,'Reorganización')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        opcion
    )

    driver.execute_script("arguments[0].click();", opcion)

    # Confirmar
    ActionChains(driver) \
        .send_keys(Keys.ENTER) \
        .perform()

    time.sleep(1)

def presionar_boton_continuar_cambio_posicion_final(driver):

    wait = WebDriverWait(driver, 40)

    boton = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//oj-c-progress-button[contains(@id,'continue')]//button[@aria-label='Continuar']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        boton
    )

    wait.until(
        lambda d: boton.is_enabled()
    )

    driver.execute_script("arguments[0].click();", boton)

    time.sleep(1)
