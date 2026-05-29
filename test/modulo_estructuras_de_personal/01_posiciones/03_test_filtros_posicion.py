from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
)
from Helpers.posiciones.filtros_posicion.filtros_posicion_helpers import (
    presionar_boton_borrar,
    seleccionar_filtro_codigo_posicion_principal,
    seleccionar_filtro_estado_activa,
    seleccionar_filtro_estado_contratacion_aprobada,
    seleccionar_filtro_fecha_vigencia,
    seleccionar_filtro_nombre_posicion_principal,
    seleccionar_filtro_tipo_titular_individual,
    seleccionar_filtro_titular_posiciones_con_titulares,
)


def test_filtros_posicion(estructuras_personal):

    seleccionar_posiciones(estructuras_personal)
    seleccionar_filtro_fecha_vigencia(estructuras_personal, "01/01/2024")
    seleccionar_filtro_estado_activa(estructuras_personal)
    seleccionar_filtro_titular_posiciones_con_titulares(estructuras_personal)
    seleccionar_filtro_codigo_posicion_principal(estructuras_personal, "300016")
    seleccionar_filtro_nombre_posicion_principal(
        estructuras_personal,
        "Relaciones Laborales, Liquidaciones y Servicios de Salud - Resp. Relaciones Laborales, Liquidaci\u00f3n y Servicios de Salud",
    )
    seleccionar_filtro_estado_contratacion_aprobada(estructuras_personal)
    seleccionar_filtro_tipo_titular_individual(estructuras_personal)
    presionar_boton_borrar(estructuras_personal)

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\03_test_filtros_posicion.py::test_filtros_posicion -v -s
