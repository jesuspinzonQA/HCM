from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
)

from Helpers.posiciones.eliminar_posicion.eliminar_posicion_helpers import (
    buscar_posicion_a_eliminar,
    buscar_posicion_eliminada,
    confirmar_suprimir_posicion,
    posicion_sigue_visible,
    presionar_boton_mas_acciones,
    seleccionar_posicion_a_eliminar,
    seleccionar_suprimir_posicion,
)


def test_eliminar_posicion(estructuras_personal, posicion_eliminar):

    # INGRESAR A POSICIONES
    seleccionar_posiciones(estructuras_personal)

    # BUSCAR LA POSICION A ELIMINAR
    buscar_posicion_a_eliminar(estructuras_personal, posicion_eliminar)

    # SELECCIONAR LA POSICION A ELIMINAR
    seleccionar_posicion_a_eliminar(estructuras_personal, posicion_eliminar)

    # PRESIONAR EL BOTON DE LOS TRES PUNTOS
    presionar_boton_mas_acciones(estructuras_personal)

    # SELECCIONAR LA OPCION SUPRIMIR POSICION
    seleccionar_suprimir_posicion(estructuras_personal)

    # CONFIRMAR LA SUPRESION DE LA POSICION
    confirmar_suprimir_posicion(estructuras_personal)

    # BUSCAR NUEVAMENTE LA POSICION ELIMINADA
    buscar_posicion_eliminada(estructuras_personal, posicion_eliminar)

    # VALIDAR QUE LA POSICION YA NO SE ENCUENTRE VISIBLE
    if posicion_sigue_visible(estructuras_personal, posicion_eliminar):
        print(f"La posicion '{posicion_eliminar}' sigue visible. El test fallo al no eliminarla.")
        assert False, f"La posicion '{posicion_eliminar}' sigue visible luego de intentar eliminarla."

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\05_test_eliminar_posicion.py::test_eliminar_posicion -v -s --posicion-eliminar "Prueba QA Jesus"
