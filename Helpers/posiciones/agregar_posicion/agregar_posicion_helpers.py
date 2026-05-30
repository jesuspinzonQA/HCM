from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def esperar_campo_fecha_inicio_vigencia(driver):

    wait = WebDriverWait(driver, 30)

    selectores_fecha = [
        (By.ID, "effectiveStartDateId|input"),
        (By.CSS_SELECTOR, "input[id*='effectiveStartDate'][id$='|input']"),
        (By.CSS_SELECTOR, "input[id*='EffectiveStartDate'][id$='|input']"),
        (By.CSS_SELECTOR, "input[id*='StartDate'][id$='|input']"),
        (By.XPATH, "//input[contains(@id,'effectiveStartDate')]"),
        (By.XPATH, "//input[contains(@aria-label,'Fecha') and contains(@aria-label,'vigencia')]"),
        (By.XPATH, "//input[contains(@aria-label,'Date') and contains(@aria-label,'start')]"),
    ]

    for selector in selectores_fecha:
        try:
            return wait.until(
                EC.element_to_be_clickable(selector)
            )
        except Exception:
            pass

    raise AssertionError("No se encontro el campo Fecha inicio vigencia en el formulario de nueva posicion.")

def boton_agregar_posiciones(driver):

    fin = time.monotonic() + 40
    botones_visibles = []

    while time.monotonic() < fin:
        resultado = driver.execute_script(
            """
            const normalizar = (texto) => (texto || '')
                .normalize('NFD')
                .replace(/[\\u0300-\\u036f]/g, '')
                .toLowerCase();

            const candidatos = [
                ...document.querySelectorAll('button, [role="button"], oj-button')
            ];

            return candidatos.find((elemento) => {
                const texto = normalizar(
                    elemento.innerText ||
                    elemento.textContent ||
                    elemento.getAttribute('aria-label') ||
                    elemento.getAttribute('title')
                );
                const etiqueta = normalizar(
                    elemento.getAttribute('aria-label') ||
                    elemento.getAttribute('title')
                );
                const rect = elemento.getBoundingClientRect();
                const visible = rect.width > 0 && rect.height > 0;

                return visible &&
                    (texto.includes('agregar') || etiqueta.includes('agregar')) &&
                    (texto.includes('posici') || etiqueta.includes('posici'));
            });
            const visibles = candidatos
                .filter((elemento) => {
                    const rect = elemento.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                })
                .map((elemento) => (
                    elemento.innerText ||
                    elemento.textContent ||
                    elemento.getAttribute('aria-label') ||
                    elemento.getAttribute('title') ||
                    elemento.id ||
                    elemento.tagName
                ).trim())
                .filter(Boolean)
                .slice(0, 20);

            return [boton || null, visibles];
            """
        )

        boton_agregar = resultado[0]
        botones_visibles = resultado[1]

        if boton_agregar:
            break

        time.sleep(1)
    else:
        raise AssertionError(
            "No se encontro el boton Agregar posicion. "
            f"Botones visibles detectados: {botones_visibles}"
        )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", boton_agregar)

    try:
        ActionChains(driver).move_to_element(boton_agregar).click().perform()
    except Exception:
        driver.execute_script("arguments[0].click();", boton_agregar)

    esperar_campo_fecha_inicio_vigencia(driver)
    return


def completar_fecha_inicio_vigencia(driver, fecha):

    campo_fecha = esperar_campo_fecha_inicio_vigencia(driver)

    campo_fecha.clear()

    campo_fecha.send_keys(fecha)

    campo_fecha.send_keys(Keys.ENTER)

    time.sleep(1)

def seleccionar_motivo_accion(driver):

    wait = WebDriverWait(driver, 30)

    motivo_accion = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[id*='ActionReasonId'][id$='|input']"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", motivo_accion)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(motivo_accion).click().perform()

    time.sleep(1)

    actions.send_keys("Carga Inicial Posiciones").perform()

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def seleccionar_estado(driver, estado):

    wait = WebDriverWait(driver, 30)

    campo_estado = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[id*='Status'][id$='|input']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_estado
    )

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo_estado).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    time.sleep(1)

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys(estado).perform()

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def seleccionar_posicion_principal(driver):

    wait = WebDriverWait(driver, 30)

    campo_posicion = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "createParentPositionLovTemplate|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_posicion
    )

    time.sleep(1)

    actions = ActionChains(driver)

    # SELECCIONAR CAMPO
    actions.move_to_element(campo_posicion).click().perform()

    time.sleep(1)

    # BORRAR VALOR EXISTENTE
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    time.sleep(1)

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    # ESCRIBIR VALOR PARA BUSCAR
    actions.send_keys("Productos y Serv. Transacc.").perform()

    time.sleep(1)

    # SELECCIONAR OPCION DEL DESPLEGABLE
    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Co-Resp. Prod. y Serv. Transaccionales')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(1)

    # PRESIONAR ENTER
    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def seleccionar_unidad_negocio(driver):

    wait = WebDriverWait(driver, 30)

    campo_unidad = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.BusinessUnitId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_unidad
    )

    time.sleep(1)

    actions = ActionChains(driver)

    # SELECCIONAR CAMPO
    actions.move_to_element(campo_unidad).click().perform()

    time.sleep(1)

    # BORRAR VALOR EXISTENTE
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    time.sleep(1)

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    # ESCRIBIR VALOR
    actions.send_keys("Corp.Banking & Corp.Affairs").perform()

    time.sleep(1)

    # SELECCIONAR OPCION DEL DESPLEGABLE
    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Corp.Banking & Corp.Affairs')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(1)

    # PRESIONAR ENTER
    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def completar_nombre(driver, nombre):

    wait = WebDriverWait(driver, 30)

    campo_nombre = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.PositionName|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_nombre
    )

    time.sleep(1)

    campo_nombre.click()

    campo_nombre.clear()

    campo_nombre.send_keys(nombre)

    time.sleep(1)

def saltar_campo_codigo(driver):

    actions = ActionChains(driver)

    time.sleep(1)

    actions.send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_departamento(driver):

    wait = WebDriverWait(driver, 30)

    campo_departamento = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.DepartmentId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_departamento
    )

    time.sleep(1)

    actions = ActionChains(driver)

    # SELECCIONAR CAMPO
    actions.move_to_element(campo_departamento).click().perform()

    time.sleep(1)

    # BORRAR VALOR EXISTENTE
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    time.sleep(1)

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    # ESCRIBIR NUEVO VALOR
    actions.send_keys("Productos y Serv. Transacc.").perform()

    time.sleep(1)

    # SELECCIONAR OPCION DEL DESPLEGABLE
    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Productos y Serv. Transacc.')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(1)

    # PRESIONAR ENTER
    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def completar_puesto(driver):

    wait = WebDriverWait(driver, 30)

    campo_puesto = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.JobId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_puesto
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        campo_puesto
    )

    time.sleep(1)

    # ESCRIBIR PUESTO
    campo_puesto.send_keys(
        "Analista Riesgo de Mercado"
    )

    time.sleep(1)

    # SELECCIONAR OPCION DEL DESPLEGABLE
    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(text(),'Analista Riesgo de Mercado S/Sr')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(1)

def seleccionar_ubicacion(driver):

    wait = WebDriverWait(driver, 30)

    campo_ubicacion = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.LocationId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_ubicacion
    )

    time.sleep(1)

    # CLICK EN EL CAMPO
    driver.execute_script(
        "arguments[0].click();",
        campo_ubicacion
    )

    time.sleep(1)

    # ESCRIBIR UBICACION
    campo_ubicacion.send_keys(
        "Edificio Carlos Pellegrini"
    )

    time.sleep(1)

    # SELECCIONAR OPCION DEL LOV
    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(text(),'Edificio Carlos Pellegrini')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(1)

def completar_tiempo_completo_parcial(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.FullPartTime|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("Tiempo completo").perform()

    time.sleep(1)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Tiempo completo')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def completar_indefinido_temporal(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_positionsV2.RegularTemporary|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("Indefinido").perform()

    time.sleep(1)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Indefinido')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def completar_horas_laborables_estandar(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "standardWorkingHoursInputText|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("7.5").perform()

    time.sleep(1)

def completar_frecuencia_estandar(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_dynform_StandardWorkingHoursGroup_fl_positionsV2.StandardWorkingFrequency|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("Diaria").perform()

    time.sleep(1)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Diaria')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def completar_horas_laborables(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "workingHoursInputText|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("7.5").perform()

    time.sleep(1)

def completar_frecuencia_horas_laborables(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_dynform_WorkingHoursGroup_fl_positionsV2.WorkingHoursFrequency|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("Diaria").perform()

    time.sleep(1)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Diaria')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(1)

def completar_estado_contratacion(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_dynform_Type_fl_positionsV2.HiringStatus|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("Aprobada").perform()

    time.sleep(2)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Aprobada')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(2)

def completar_tipo(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "oj-dyn-form-2092688325-1_fl_dynform_Type_fl_positionsV2.PositionType|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("Titular individual").perform()

    time.sleep(2)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(normalize-space(),'Titular individual')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", opcion)

    time.sleep(1)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(2)

def completar_plantilla(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "headCountInputText|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("1").perform()

    time.sleep(2)

def completar_equivalente_tiempo_completo(driver):

    wait = WebDriverWait(driver, 30)

    campo = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "fteInputText|input"
            )
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo)

    time.sleep(1)

    actions = ActionChains(driver)

    actions.move_to_element(campo).click().perform()

    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    actions.send_keys("1").perform()

    time.sleep(2)

def completar_plan_compensaciones(driver):

    wait = WebDriverWait(driver, 30)

    campo_plan = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[id*='ICBCCOMPPLAN'][id$='|input']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_plan
    )

    time.sleep(2)

    actions = ActionChains(driver)

    actions.move_to_element(campo_plan).click().perform()

    time.sleep(1)

    actions.send_keys("BB Car").perform()

    time.sleep(2)

    opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(text(),'BB Car')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion
    )

    time.sleep(2)

    actions.send_keys(Keys.ESCAPE).perform()

    time.sleep(1)

    actions.send_keys(Keys.TAB).perform()

    time.sleep(1)

def seleccionar_checkbox_perfil_digital(driver):

    wait = WebDriverWait(driver, 30)

    checkbox = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[type='checkbox'][name*='perfilDigital_checkbox']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        checkbox
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        checkbox
    )

    time.sleep(1)

def suprimir_cualquier_grupo_existente(driver):

    wait = WebDriverWait(driver, 30)

    # BUSCAR FILA EXISTENTE DENTRO DE GRUPOS VALIDOS
    filas = driver.find_elements(
        By.CSS_SELECTOR,
        "#validGradesCreateListView li[role='row']"
    )

    if not filas:
        print("No hay grupos existentes para suprimir.")
        return

    fila = filas[0]

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        fila
    )

    time.sleep(1)

    # SELECCIONAR FILA
    driver.execute_script(
        "arguments[0].click();",
        fila
    )

    time.sleep(2)

    # BOTON SUPRIMIR DENTRO DE ESA MISMA FILA
    boton_suprimir = fila.find_element(
        By.CSS_SELECTOR,
        "oj-button[actionid='delete_valid_grade'] button"
    )

    driver.execute_script(
        "arguments[0].click();",
        boton_suprimir
    )

    time.sleep(3)

def presionar_boton_agregar_grupos_validos(driver):

    wait = WebDriverWait(driver, 30)

    # BOTON AGREGAR
    boton_agregar = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#addButtonAction button"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        boton_agregar
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        boton_agregar
    )

    time.sleep(1)

    # CAMPO GRUPO
    campo_grupo = wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "addValidGradeDynForm0_fl_GradeId|input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        campo_grupo
    )

    time.sleep(1)

    # FORZAR FOCO
    driver.execute_script(
        "arguments[0].focus();",
        campo_grupo
    )

    driver.execute_script(
        "arguments[0].click();",
        campo_grupo
    )

    time.sleep(1)

    actions = ActionChains(driver)

    # LIMPIAR CAMPO
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    time.sleep(1)

    actions.send_keys(Keys.BACKSPACE).perform()

    time.sleep(1)

    # ESCRIBIR 42
    actions.send_keys("42").perform()

    time.sleep(1)

    # SELECCIONAR OPCION DEL LOV
    opcion_42 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[normalize-space()='42']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        opcion_42
    )

    time.sleep(1)

    # CERRAR LOV
    actions.send_keys(Keys.TAB).perform()

    time.sleep(1)

def presionar_boton_guardar_grupos_validos(driver):

    wait = WebDriverWait(driver, 30)

    boton_guardar = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#ojHcmCollectionItem_validGradesCollectionItem_toolBarButtonSave button"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        boton_guardar
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        boton_guardar
    )

    time.sleep(1)

def presionar_boton_ejecutar(driver):

    wait = WebDriverWait(driver, 60)

    boton_ejecutar = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#oj_ssce1_h_primaryActionFromHeader_primaryActionCta button"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        boton_ejecutar
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        boton_ejecutar
    )

    time.sleep(1)

def esperar_pantalla_buscador_posiciones(driver):

    wait = WebDriverWait(driver, 60)

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
        )
    )

    time.sleep(1)

def buscar_posicion_creada(driver, valor_buscador):

    wait = WebDriverWait(driver, 60)

    buscador = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "ojHcmAdvancedSearchBox_position-adv-srch|input")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        buscador
    )

    time.sleep(1)

    buscador.click()

    buscador.send_keys(Keys.CONTROL, "a")
    buscador.send_keys(Keys.BACKSPACE)

    buscador.send_keys(valor_buscador)

    time.sleep(1)

    buscador.send_keys(Keys.ENTER)

    time.sleep(1)
