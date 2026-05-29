from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Helpers.login.login_helpers import login

from Helpers.navegacion_a_estructuras_de_personal.navegacion_estructuras_helpers import (
    ir_a_pagina_inicial,
    seleccionar_mis_grupos_clientes,
    seleccionar_estructuras_personal
)

from Helpers.solicitar_nueva_posicion.solicitar_nueva_posicion_helpers import (
    seleccionar_solicitar_nueva_posicion,
    seleccionar_informacion_adicional,
    seleccionar_informacion_legislativa,
    presionar_boton_continuar,
    seleccionar_fecha_inicio_nueva_posicion,
    seleccionar_motivo_solicitud,
    presionar_boton_continuar,
    seleccionar_posicion_principal,
    seleccionar_estado,
    seleccionar_unidad_negocio,
    seleccionar_nombre,
    saltar_campo_codigo,
    seleccionar_departamento,
    seleccionar_puesto,
    seleccionar_ubicacion,
    seleccionar_tiempo_completo_parcial,
    seleccionar_indefinido_temporal,
    seleccionar_horas_laborables_estandar,
    seleccionar_frecuencia,
    seleccionar_horas_laborables,
    seleccionar_frecuencia,
    seleccionar_estado_contratacion,
    seleccionar_tipo,
    saltar_plan_compensaciones,
    seleccionar_plantilla,
    seleccionar_equivalente_tiempo_completo,
    saltar_boton_agregar,
    saltar_grupo_registro,
    presionar_boton_continuar
)

def test_crear_nueva_posicion(driver, credenciales_hcm):

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

    # INGRESAR A SOLICITAR NUEVA POSICION
    seleccionar_solicitar_nueva_posicion(driver)

    # SELECCIONAR EL BOTON: INFORMACION ADICIONAL
    seleccionar_informacion_adicional(driver)

    # SELECCIONAR EL BOTON: INFORMACION LEGISLATIVA
    seleccionar_informacion_legislativa(driver)

    # PRESIONAR EL BOTON CONTINUAR
    presionar_boton_continuar(driver)

    # COMPLETAR CON FECHA EL CAMPO: ¿CUANDO COMIENZA LA NUEVA POSICION?
    seleccionar_fecha_inicio_nueva_posicion(driver)

    # SELECCIONAR EL MOTIVO DEL CAMPO: ¿CUAL ES EL MOTIVO DE ESTA SOLICITUD?
    seleccionar_motivo_solicitud(driver)

    # PRESIONAR EL BOTON CONTINUAR
    presionar_boton_continuar(driver)

    # EN LA PAGINA: DETALLES DE POSICION
    # SELECCIONAR EL CAMPO POSICION PRINCIPAL: FECHA 20/05/2026
    seleccionar_posicion_principal(driver)

    # SELECCIONAR EL CAMPO ESTADO: ACIVA
    seleccionar_estado(driver)

    # SELECCIONAR EL CAMPO UNIDAD DE NEGOCIO: Corp.Banking & Corp.Affairs
    seleccionar_unidad_negocio(driver)

    # SELECCIONAR EL CAMPO NOMBRE: JESUS PINZON QA
    seleccionar_nombre(driver)

    # SALTAR EL CAMPO CODIGO
    saltar_campo_codigo(driver)

    # SELECCIONAR EL CAMPO DEPARTAMENTO: Productos y Serv. Transacc.
    seleccionar_departamento(driver)

    # SELECCIONAR EL CAMPO PUESTO: Jefe de QARM
    seleccionar_puesto(driver)

    # SELECCIONAR EL CAAMPO UBICACIONES: Edificio Madero Office
    seleccionar_ubicacion(driver)

    # SELECCIONAR EL CAMPO TIEMPO COMPLETO O TIEMPO PARCIAL: Tiempo Completo
    seleccionar_tiempo_completo_parcial(driver)

    # SELECCIONAR EL CAMPO INDEFINIDO O TEMPORAL: Indefinido
    seleccionar_indefinido_temporal(driver)

    # SELECCIONAR EL CAMPO HORAS LABORABLES ESTANDAR: 7.5
    seleccionar_horas_laborables_estandar(driver)

    # SELECCIONAR EL CAMPO FRECUENCIA: Diaria
    seleccionar_frecuencia(driver)

    # SELECCIONAR EL CAMPO HORAS LABORABLES: Diaria
    seleccionar_horas_laborables(driver)

    # SELECCIONAR EL CAMPO FRECUENCIA: Diaria
    seleccionar_frecuencia(driver)

    # SELECCIONAR EL CAMPO ESTADO DE CONTRATACION: Aprobada
    seleccionar_estado_contratacion(driver)

    # SELECCIONAR EL CAMPO TIPO: Titular individual
    seleccionar_tipo(driver)

    # SALTAR EL CAMPO PLAN DE COMPENSACIONES
    saltar_plan_compensaciones(driver)

    # SELECCIONAR EL CAMPO PLANTILLA: 1
    seleccionar_plantilla(driver)

    # SELECCIONAR EL CAMPO EQUIVALIENTE A TIEMPO COMPLETO: 1
    seleccionar_equivalente_tiempo_completo(driver)

    # SALTAR BOTON AGREGAR
    saltar_boton_agregar(driver)

    # SALTAR CAMPO GRUPO REGISTRO
    saltar_grupo_registro(driver)

    # PRESIONAR EL BOTON CONTINUAR
    presionar_boton_continuar(driver)



#Para correr solamente este test: pytest test\modulo_estructuras_de_personal\02_solicitar_nueva_posicion\01_test_solicitar_nueva_posicion.py::test_crear_nueva_posicion -v -s
