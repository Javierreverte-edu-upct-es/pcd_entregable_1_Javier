import pytest
from entregable1 import (
    NaveEstelar,
    ClaseNave,
    Almacen,
    Repuesto,
    Comandante
)


# TEST 1: creación de una nave
def test_creacion_nave():

    nave = NaveEstelar(
        "ID-001",
        1234,
        "Destructor Imperial",
        5000,
        100,
        ClaseNave.EJECUTOR
    )

    assert nave.nombre == "Destructor Imperial"
    assert nave.tripulacion == 5000
    assert nave.clase == ClaseNave.EJECUTOR


# TEST 2: agregar repuesto al almacén
def test_agregar_repuesto():

    almacen = Almacen("Base Imperial", "Espacio")
    motor = Repuesto("Motor", "Proveedor", 10, 1000)

    almacen.agregar_repuesto(motor)

    assert len(almacen.catalogo) == 1
    assert almacen.catalogo[0].nombre == "Motor"


# TEST 3: buscar repuesto existente
def test_buscar_repuesto():

    almacen = Almacen("Base", "Espacio")
    motor = Repuesto("Motor", "Proveedor", 10, 1000)

    almacen.agregar_repuesto(motor)

    encontrado = almacen.buscar_repuesto("Motor")

    assert encontrado.nombre == "Motor"


# TEST 4: comprar repuesto
def test_compra_repuesto():

    almacen = Almacen("Base", "Espacio")
    motor = Repuesto("Motor", "Proveedor", 10, 1000)

    almacen.agregar_repuesto(motor)

    comandante = Comandante("Vader")
    comandante.comprar_repuesto(almacen, "Motor", 2)

    assert motor._cantidad == 8


# TEST 5: excepción si no hay suficiente stock
def test_error_stock():

    repuesto = Repuesto("Motor", "Proveedor", 5, 1000)

    with pytest.raises(ValueError):
        repuesto.retirar_stock(10)


# TEST 6: excepción si el repuesto no existe
def test_repuesto_no_encontrado():

    almacen = Almacen("Base", "Espacio")

    with pytest.raises(ValueError):
        almacen.buscar_repuesto("Laser")