from Helpers.posiciones.buscador_posicion.buscador_helpers import (
    seleccionar_posiciones,
)
from Helpers.posiciones.agregar_posicion.agregar_posicion_helpers import (
    boton_agregar_posiciones,
    completar_equivalente_tiempo_completo,
    completar_estado_contratacion,
    completar_fecha_inicio_vigencia,
    completar_frecuencia_estandar,
    completar_frecuencia_horas_laborables,
    completar_horas_laborables,
    completar_horas_laborables_estandar,
    completar_indefinido_temporal,
    completar_nombre,
    completar_plan_compensaciones,
    completar_plantilla,
    completar_puesto,
    completar_tiempo_completo_parcial,
    completar_tipo,
    buscar_posicion_creada,
    esperar_pantalla_buscador_posiciones,
    presionar_boton_agregar_grupos_validos,
    presionar_boton_ejecutar,
    presionar_boton_guardar_grupos_validos,
    saltar_campo_codigo,
    seleccionar_checkbox_perfil_digital,
    seleccionar_departamento,
    seleccionar_estado,
    seleccionar_motivo_accion,
    seleccionar_posicion_principal,
    seleccionar_ubicacion,
    seleccionar_unidad_negocio,
    suprimir_cualquier_grupo_existente,
)


def test_agregar_una_posicion(estructuras_personal, fecha_vigencia, nombre_posicion):

    seleccionar_posiciones(estructuras_personal)
    boton_agregar_posiciones(estructuras_personal)
    completar_fecha_inicio_vigencia(estructuras_personal, fecha_vigencia)
    seleccionar_motivo_accion(estructuras_personal)
    seleccionar_estado(estructuras_personal, "Activa")
    seleccionar_posicion_principal(estructuras_personal)
    seleccionar_unidad_negocio(estructuras_personal)
    completar_nombre(estructuras_personal, nombre_posicion)
    saltar_campo_codigo(estructuras_personal)
    seleccionar_departamento(estructuras_personal)
    completar_puesto(estructuras_personal)
    seleccionar_ubicacion(estructuras_personal)
    completar_tiempo_completo_parcial(estructuras_personal)
    completar_indefinido_temporal(estructuras_personal)
    completar_horas_laborables_estandar(estructuras_personal)
    completar_frecuencia_estandar(estructuras_personal)
    completar_horas_laborables(estructuras_personal)
    completar_frecuencia_horas_laborables(estructuras_personal)
    completar_estado_contratacion(estructuras_personal)
    completar_tipo(estructuras_personal)
    completar_plantilla(estructuras_personal)
    completar_equivalente_tiempo_completo(estructuras_personal)
    completar_plan_compensaciones(estructuras_personal)
    seleccionar_checkbox_perfil_digital(estructuras_personal)
    suprimir_cualquier_grupo_existente(estructuras_personal)
    presionar_boton_agregar_grupos_validos(estructuras_personal)
    presionar_boton_guardar_grupos_validos(estructuras_personal)
    presionar_boton_ejecutar(estructuras_personal)
    esperar_pantalla_buscador_posiciones(estructuras_personal)
    buscar_posicion_creada(estructuras_personal, nombre_posicion)

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\01_posiciones\02_test_agregar_posicion.py::test_agregar_una_posicion -v -s
