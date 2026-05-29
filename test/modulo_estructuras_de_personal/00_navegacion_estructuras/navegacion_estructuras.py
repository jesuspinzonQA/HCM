def test_navegacion_estructuras_personal(estructuras_personal):
    assert "workforce_structures" in estructuras_personal.current_url


# Para correr solamente este test: pytest test\modulo_estructuras_de_personal\00_navegacion_estructuras\navegacion_estructuras.py::test_navegacion_estructuras_personal -v -s
