from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
)
from Helpers.posiciones.boton_filtro_posicion.boton_filtro_posicion_helpers import (
    abrir_boton_filtros,
    presionar_ver_resultados,
    seleccionar_departamento,
    seleccionar_estado_activa,
    seleccionar_estado_contratacion,
    seleccionar_fecha_vigencia_filtro,
    seleccionar_posicion,
    seleccionar_posicion_principal,
    seleccionar_puesto,
    seleccionar_tipo,
    seleccionar_titulares,
    seleccionar_ubicacion,
    seleccionar_unidad_negocio,
)


def test_boton_filtro_posicion(estructuras_personal):

    seleccionar_posiciones(estructuras_personal)
    abrir_boton_filtros(estructuras_personal)
    seleccionar_fecha_vigencia_filtro(estructuras_personal, "01/01/2024")
    seleccionar_estado_activa(estructuras_personal)
    seleccionar_titulares(estructuras_personal)
    seleccionar_posicion_principal(estructuras_personal)
    seleccionar_puesto(estructuras_personal)
    seleccionar_departamento(estructuras_personal)
    seleccionar_ubicacion(estructuras_personal)
    seleccionar_unidad_negocio(estructuras_personal)
    seleccionar_estado_contratacion(estructuras_personal)
    seleccionar_tipo(estructuras_personal)
    seleccionar_posicion(estructuras_personal)
    presionar_ver_resultados(estructuras_personal)

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\04_test_boton_filtro_posicion.py::test_boton_filtro_posicion -v -s
