from Helpers.solicitar_nueva_posicion.solicitar_nueva_posicion_helpers import (
    presionar_boton_continuar_nueva_posicion,
    saltar_boton_agregar,
    saltar_campo_codigo,
    saltar_grupo_registro,
    saltar_plan_compensaciones,
    seleccionar_departamento,
    seleccionar_equivalente_tiempo_completo,
    seleccionar_estado,
    seleccionar_estado_contratacion,
    seleccionar_fecha_inicio_nueva_posicion,
    seleccionar_frecuencia,
    seleccionar_horas_laborables,
    seleccionar_horas_laborables_estandar,
    seleccionar_indefinido_temporal,
    seleccionar_informacion_adicional_nueva_posicion,
    seleccionar_informacion_legislativa_nueva_posicion,
    seleccionar_motivo_solicitud,
    seleccionar_nombre,
    seleccionar_plantilla,
    seleccionar_posicion_principal,
    seleccionar_puesto,
    seleccionar_solicitar_nueva_posicion,
    seleccionar_tiempo_completo_parcial,
    seleccionar_tipo,
    seleccionar_ubicacion,
    seleccionar_unidad_negocio,
)


def test_crear_nueva_posicion(estructuras_personal):

    seleccionar_solicitar_nueva_posicion(estructuras_personal)
    seleccionar_informacion_adicional_nueva_posicion(estructuras_personal)
    seleccionar_informacion_legislativa_nueva_posicion(estructuras_personal)
    presionar_boton_continuar_nueva_posicion(estructuras_personal)
    seleccionar_fecha_inicio_nueva_posicion(estructuras_personal)
    seleccionar_motivo_solicitud(estructuras_personal)
    presionar_boton_continuar_nueva_posicion(estructuras_personal)
    seleccionar_posicion_principal(estructuras_personal)
    seleccionar_estado(estructuras_personal)
    seleccionar_unidad_negocio(estructuras_personal)
    seleccionar_nombre(estructuras_personal)
    saltar_campo_codigo(estructuras_personal)
    seleccionar_departamento(estructuras_personal)
    seleccionar_puesto(estructuras_personal)
    seleccionar_ubicacion(estructuras_personal)
    seleccionar_tiempo_completo_parcial(estructuras_personal)
    seleccionar_indefinido_temporal(estructuras_personal)
    seleccionar_horas_laborables_estandar(estructuras_personal)
    seleccionar_frecuencia(estructuras_personal)
    seleccionar_horas_laborables(estructuras_personal)
    seleccionar_frecuencia(estructuras_personal)
    seleccionar_estado_contratacion(estructuras_personal)
    seleccionar_tipo(estructuras_personal)
    saltar_plan_compensaciones(estructuras_personal)
    seleccionar_plantilla(estructuras_personal)
    seleccionar_equivalente_tiempo_completo(estructuras_personal)
    saltar_boton_agregar(estructuras_personal)
    saltar_grupo_registro(estructuras_personal)
    presionar_boton_continuar_nueva_posicion(estructuras_personal)

    # Para correr solamente este test: pytest test\modulo_estructuras_de_personal\02_solicitar_nueva_posicion\01_test_solicitar_nueva_posicion.py::test_crear_nueva_posicion -v -s
