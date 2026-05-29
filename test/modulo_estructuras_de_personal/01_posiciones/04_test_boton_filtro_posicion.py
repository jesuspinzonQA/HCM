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
    seleccionar_posiciones
)

from Helpers.posiciones.boton_filtro_posicion.boton_filtro_posicion_helpers import (
    abrir_boton_filtros,
    seleccionar_fecha_vigencia_filtro,
    seleccionar_estado_activa,
    seleccionar_titulares,
    seleccionar_posicion_principal,
    seleccionar_puesto,
    seleccionar_departamento,
    seleccionar_ubicacion,
    seleccionar_unidad_negocio,
    seleccionar_estado_contratacion,
    seleccionar_tipo,
    seleccionar_posicion,
    presionar_ver_resultados
)

def test_boton_filtro_posicion(driver, credenciales_hcm):

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

    # SELECCINAR EL BOTON FILTROS
    abrir_boton_filtros(driver)

    # SELECCIONAR LA SECCION: FECHA DE VIGENCIA
    seleccionar_fecha_vigencia_filtro(driver, "01/01/2024")

    # SELECCIONAR LA SECCION: ESTADO - ACTIVA
    seleccionar_estado_activa(driver)

    # SELECCIONAR LA SECCION: TITULARES
    seleccionar_titulares(driver)

    # SELECCIONAR POSICION PRINCIPAL: CODIGO Y NOMBRE DE POSICION PRINCIPAL
    seleccionar_posicion_principal(driver)

    # SELECCIONAR PUESTO: CODIGO Y NOMBRE DE PUESTO
    seleccionar_puesto(driver)

    # SELECCIONAR DEPARTAMENTO: 
    seleccionar_departamento(driver)

    # SELECCIONAR UBICACION: CODIGO Y NOMBRE DE UBICACION
    seleccionar_ubicacion(driver)

    # SELECCIONAR UNIDAD DE NEGOCIO
    seleccionar_unidad_negocio(driver)

    # SELECCIONAR ESTADO DE CONTRATACION: APROBADA
    seleccionar_estado_contratacion(driver)

    # SELECCIONAR TIPO: TITULAAR INDIVIDUAL
    seleccionar_tipo(driver)

    # SELECCIONAR POSICION: CODIGO Y NOMBRE
    seleccionar_posicion(driver)

    # PRESIONAR BOTON VER RESULTADOS
    presionar_ver_resultados(driver)


#Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\04_test_boton_filtro_posicion.py::test_boton_filtro_posicion -v -s
