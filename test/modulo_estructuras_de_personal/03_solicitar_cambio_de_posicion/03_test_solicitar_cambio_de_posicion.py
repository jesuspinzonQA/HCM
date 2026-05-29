from Helpers.solicitar_nueva_posicion.solicitar_nueva_posicion_helpers import (
    buscar_posicion,
    presionar_boton_continuar_cambio_posicion,
    presionar_boton_continuar_cambio_posicion_final,
    seleccionar_fecha_inicio_cambio_posicion,
    seleccionar_informacion_adicional_cambio_posicion,
    seleccionar_informacion_legislativa_cambio_posicion,
    seleccionar_motivo_solicitud_cambio_posicion,
    seleccionar_posicion,
    seleccionar_solicitar_cambio_posicion,
)


def test_solicitar_cambio_posicion(estructuras_personal):

    seleccionar_solicitar_cambio_posicion(estructuras_personal)
    buscar_posicion(estructuras_personal, "Prueba QA Jesus")
    seleccionar_posicion(estructuras_personal)
    seleccionar_informacion_adicional_cambio_posicion(estructuras_personal)
    seleccionar_informacion_legislativa_cambio_posicion(estructuras_personal)
    presionar_boton_continuar_cambio_posicion(estructuras_personal)
    seleccionar_fecha_inicio_cambio_posicion(estructuras_personal)
    seleccionar_motivo_solicitud_cambio_posicion(estructuras_personal)
    presionar_boton_continuar_cambio_posicion_final(estructuras_personal)

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\03_solicitar_cambio_de_posicion\03_test_solicitar_cambio_posicion.py::test_solicitar_cambio_posicion -v -s
