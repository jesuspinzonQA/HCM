from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
)
from Helpers.posiciones.eliminar_posicion.eliminar_posicion_helpers import (
    eliminar_posicion,
    posicion_sigue_visible,
)


def test_eliminar_posicion(estructuras_personal, posicion_eliminar):
    seleccionar_posiciones(estructuras_personal)
    eliminar_posicion(estructuras_personal, posicion_eliminar)

    if posicion_sigue_visible(estructuras_personal, posicion_eliminar):
        print(f"La posicion '{posicion_eliminar}' sigue visible. El test fallo al no eliminarla.")
        assert False, f"La posicion '{posicion_eliminar}' sigue visible luego de intentar eliminarla."

    # Para correr solamente este test:
    # pytest test\modulo_estructuras_de_personal\01_posiciones\05_test_eliminar_posicion.py::test_eliminar_posicion -v -s --posicion-eliminar "Prueba QA Jesus"
