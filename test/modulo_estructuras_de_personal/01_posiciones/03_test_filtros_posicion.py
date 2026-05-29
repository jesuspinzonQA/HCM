from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Helpers.login.login_helpers import login

from Helpers.navegacion_a_estructuras_de_personal.navegacion_estructuras_helpers import (
    ir_a_pagina_inicial,
    seleccionar_mis_grupos_clientes,
    seleccionar_estructuras_personal
)

from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones
)

from Helpers.posiciones.filtros_posicion.filtros_posicion_helpers import (
    seleccionar_filtro_fecha_vigencia,
    seleccionar_filtro_estado_activa,
    seleccionar_filtro_titular_posiciones_con_titulares,
    seleccionar_filtro_codigo_posicion_principal,
    seleccionar_filtro_nombre_posicion_principal,
    seleccionar_filtro_estado_contratacion_aprobada,
    seleccionar_filtro_tipo_titular_individual,
    presionar_boton_borrar
)

def test_filtros_posicion(driver, credenciales_hcm):

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

    # AGREGAR EL FILTRO FECHA DE VIGENCIA
    seleccionar_filtro_fecha_vigencia(driver, "01/01/2024")

    # AGREGAR EL FILTRO ESTADO: ACTIVA
    seleccionar_filtro_estado_activa(driver)

    # AGREGAR EL FILTRO TITULAR: POSICIONES CON TITULARES
    seleccionar_filtro_titular_posiciones_con_titulares(driver)

    # AGREGAR EL FILTRO CODIGO DE POSICION PRINCIPAL: 300043
    seleccionar_filtro_codigo_posicion_principal(driver, "300016")

    # AGREGAR EL FILTRO CODIGO DE POSICION PRINCIPAL: Relaciones Laborales, Liquidaciones y Servicios de Salud - Resp. Relaciones Laborales, Liquidación y Servicios de Salud
    seleccionar_filtro_nombre_posicion_principal(driver, "Relaciones Laborales, Liquidaciones y Servicios de Salud - Resp. Relaciones Laborales, Liquidación y Servicios de Salud")

    # AGREGAR EL FILTRO ESTADO DE CONTRATACION: APROBADA
    seleccionar_filtro_estado_contratacion_aprobada(driver)

    # AGREGAR EL FILTRO TIPO: TITULAR INDIVIDUAL
    seleccionar_filtro_tipo_titular_individual(driver)

    # BOTON ELIMINAR FILTROS
    presionar_boton_borrar(driver)


#Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\03_test_filtros_posicion.py::test_filtros_posicion -v -s
