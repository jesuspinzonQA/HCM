from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Helpers.login.login_helpers import login

from Helpers.navegacion_a_estructuras_de_personal.navegacion_estructuras_helpers import (
    ir_a_pagina_inicial,
    seleccionar_mis_grupos_clientes,
    seleccionar_estructuras_personal
)

from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
)

from Helpers.posiciones.agregar_posicion.agregar_posicion_helpers import (
    boton_agregar_posiciones,
    completar_fecha_inicio_vigencia,
    seleccionar_motivo_accion,
    seleccionar_estado,
    seleccionar_posicion_principal,
    seleccionar_unidad_negocio,
    completar_nombre,
    saltar_campo_codigo,
    seleccionar_departamento,
    completar_puesto,
    seleccionar_ubicacion,
    completar_tiempo_completo_parcial,
    completar_indefinido_temporal,
    completar_horas_laborables_estandar,
    completar_frecuencia_estandar,
    completar_horas_laborables,
    completar_frecuencia_horas_laborables,
    completar_estado_contratacion,
    completar_tipo,
    completar_plantilla,
    completar_equivalente_tiempo_completo,
    completar_plan_compensaciones,
    seleccionar_checkbox_perfil_digital,
    suprimir_cualquier_grupo_existente,
    presionar_boton_agregar_grupos_validos,
    presionar_boton_guardar_grupos_validos,
    presionar_boton_ejecutar,
    esperar_pantalla_buscador_posiciones,
    buscar_posicion_creada
)


def test_agregar_una_posicion(driver, credenciales_hcm):

    usuario, password = credenciales_hcm

    # LOGIN
    login(driver, usuario, password)

    wait = WebDriverWait(driver, 40)

    wait.until(
        EC.url_contains("AtkHomePageWelcome")
    )

    assert "AtkHomePageWelcome" in driver.current_url

    # IR A PAGINA INICIAL
    ir_a_pagina_inicial(driver)

    # INGRESAR A MIS GRUPOS DE CLIENTES
    seleccionar_mis_grupos_clientes(driver)

    # INGRESAR A ESTRUCTURAS DE PERSONAL
    seleccionar_estructuras_personal(driver)

    # INGRESAR A POSICIONES
    seleccionar_posiciones(driver)

    # PRESIONAR EL BOTON AGREGAR POSICIONES
    boton_agregar_posiciones(driver)

    # COMPLETAR FECHA INICIO VIGENCIA
    completar_fecha_inicio_vigencia(driver, "19/01/2026")

    # SELECCIONAR MOTIVO DE ACCION
    seleccionar_motivo_accion(driver)

    #SELECCIONAR ESTADO
    seleccionar_estado(driver, "Activa")

    #SELECCIONAR POSICION PRINCIPAL
    seleccionar_posicion_principal(driver)

    #SELECCIONAR UNIDAD DE NEGOCIO
    seleccionar_unidad_negocio(driver)

    # COMPLETAR NOMBRE
    completar_nombre(driver, "Prueba QA Jesus")

    # SALTAR CAMPO CODIGO
    saltar_campo_codigo(driver)

    # COMPLETAR CAMPO DEPARTAMENTO
    seleccionar_departamento(driver)

    # COMPLETAR PUESTO
    completar_puesto(driver)

    # SELECCIONAR UBICACION
    seleccionar_ubicacion(driver)

    # COMPLETAR TIEMPO COMPLETO / PARCIAL
    completar_tiempo_completo_parcial(driver)

    # COMPLETAR INDEFINIDO / TEMPORAL
    completar_indefinido_temporal(driver)

    # COMPLETAR HORAS LABORABLES ESTANDAR
    completar_horas_laborables_estandar(driver)

    # SALTAR FRECUENCIA
    completar_frecuencia_estandar(driver)

    # COMPLETAR HORAS LABORABLES
    completar_horas_laborables(driver)

    # COMPLETAR FRECUENCIA HORAS LABORABLES
    completar_frecuencia_horas_laborables(driver)

    # SALTAR ESTADO DE CONTRATACION
    completar_estado_contratacion(driver)

    # COMPLETAR TIPO
    completar_tipo(driver)

    # SALTAR PLANTILLA
    completar_plantilla(driver)

    # COMPLETAR EQUIVALENTE A TIEMPO COMPLETO
    completar_equivalente_tiempo_completo(driver)

    # COMPLETAR PLAN DE COMPENSACIONES
    completar_plan_compensaciones(driver)

    # SELECCIONAR CHECKBOX PERFIL DIGITAL
    seleccionar_checkbox_perfil_digital(driver)

    # PRESIONAR EL BOTON SUPRIMIR EN GRUPOS VALIDOS
    suprimir_cualquier_grupo_existente(driver)

    # PRESIONAR EL BOTON AGREGAR EN GRUPOS VALIDOS
    presionar_boton_agregar_grupos_validos(driver)

    # PRESIONAR BOTON GUARDAR EN GRUPOS VALIDOS
    presionar_boton_guardar_grupos_validos(driver)

    # PRESIONAR BOTON EJECUTAR
    presionar_boton_ejecutar(driver)

    # ESPERAR A LA PANTALLA DEL BUSCADOR DE POSICIONES
    esperar_pantalla_buscador_posiciones(driver)

    # BUSCAR LA POSICION CREADA
    buscar_posicion_creada(driver, "Prueba QA Jesus")

    #Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\02_test_agregar_posicion.py::test_agregar_una_posicion -v -s
