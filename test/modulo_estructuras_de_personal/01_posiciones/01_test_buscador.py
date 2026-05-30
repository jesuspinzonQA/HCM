from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    buscador_posiciones,
    seleccionar_posiciones,
)


def test_buscador_posiciones(estructuras_personal, posicion_busqueda):

    seleccionar_posiciones(estructuras_personal)

    resultado = buscador_posiciones(estructuras_personal, posicion_busqueda)

    assert posicion_busqueda in resultado.text

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\01_test_buscador.py::test_buscador_posiciones -v -s
