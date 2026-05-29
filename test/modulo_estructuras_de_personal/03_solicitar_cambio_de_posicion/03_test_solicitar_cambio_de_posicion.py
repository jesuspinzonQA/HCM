from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from helpers import (
    login,
    ir_a_pagina_inicial,
    seleccionar_mis_grupos_clientes,
    seleccionar_estructuras_personal,
    seleccionar_solicitar_cambio_posicion,
    buscar_posicion,
    seleccionar_posicion,
    seleccionar_informacion_adicional,
    seleccionar_informacion_legislativa,
    presionar_boton_continuar,
    seleccionar_fecha_inicio_cambio_posicion,
    seleccionar_motivo_solicitud_cambio_posicion,
    presionar_boton_continuar
)

def test_solicitar_cambio_posicion(driver, credenciales_hcm):

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

    # SELECCIONAR LA OPCION SOLICITAR CAMBIO DE POSICION
    seleccionar_solicitar_cambio_posicion(driver)

    # BUSCAR LA POSICION
    buscar_posicion(driver, "Prueba QA Jesus")

    # SELECCIONAR LA POSICION
    seleccionar_posicion(driver)

    # SELECCIONAR EL BOTON: INFORMACION ADICIONAL
    seleccionar_informacion_adicional(driver)

    # SELECCIONAR EL BOTON: INFORMACION LEGISLATIVA
    seleccionar_informacion_legislativa(driver)

    # PRESIONAR EL BOTON CONTINUAR
    presionar_boton_continuar(driver)

    # SELECCIONAR EL CAMPO: ¿CUANDO COMIENZA EL CAMBIO DE POSICION?
    seleccionar_fecha_inicio_cambio_posicion(driver)

    # SELECCIONAR EL CAMPO: ¿CUAL ES EL MOTIVO DE ESTA SOLICITUD?
    seleccionar_motivo_solicitud_cambio_posicion(driver)

    # PRESIONAR BOTON: CONTINUAR
    presionar_boton_continuar(driver)


#Para correr solamente este test: pytest test\modulo_estructuras_de_personal\03_solicitar_cambio_de_posicion\03_test_solicitar_cambio_de_posicion.py::test_solicitar_cambio_posicion -v -s
