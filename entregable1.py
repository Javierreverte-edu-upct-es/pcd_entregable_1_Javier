from abc import ABCMeta, abstractmethod
from enum import Enum


# ENUMERACIONES

class Ubicacion(Enum):
    ENDOR = "Endor"
    CUMULO_RAIMOS = "Cúmulo Raimos"
    NEBULOSA_KALIIDA = "Nebulosa Kaliida"


class ClaseNave(Enum):
    EJECUTOR = "Ejecutor"
    ECLIPSE = "Eclipse"
    SOBERANO = "Soberano"


# CLASES BASE

class UnidadCombate(metaclass=ABCMeta):

    def __init__(self, identificador_combate, clave_cifrada):
        self.identificador_combate = identificador_combate
        self.clave_cifrada = clave_cifrada

    @abstractmethod
    def mostrar_info(self):
        pass


class Nave(UnidadCombate):

    def __init__(self, identificador_combate, clave_cifrada, nombre):
        super().__init__(identificador_combate, clave_cifrada)
        self.nombre = nombre
        self.catalogo_repuestos = []

    def agregar_repuesto(self, repuesto):
        self.catalogo_repuestos.append(repuesto)

    def mostrar_catalogo(self):
        return self.catalogo_repuestos


# TIPOS DE NAVE

class EstacionEspacial(Nave):

    def __init__(self, identificador_combate, clave_cifrada, nombre, tripulacion, pasaje, ubicacion):
        super().__init__(identificador_combate, clave_cifrada, nombre)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

    def mostrar_info(self):
        print(f"Estación {self.nombre} en {self.ubicacion.value}")


class NaveEstelar(Nave):

    def __init__(self, identificador_combate, clave_cifrada, nombre, tripulacion, pasaje, clase):
        super().__init__(identificador_combate, clave_cifrada, nombre)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

    def mostrar_info(self):
        print(f"Nave estelar {self.nombre} clase {self.clase.value}")


class CazaEstelar(Nave):

    def __init__(self, identificador_combate, clave_cifrada, nombre, dotacion):
        super().__init__(identificador_combate, clave_cifrada, nombre)
        self.dotacion = dotacion

    def mostrar_info(self):
        print(f"Caza {self.nombre} con dotación {self.dotacion}")


# SISTEMA DE REPUESTOS

class Repuesto:

    def __init__(self, nombre, proveedor, cantidad, precio):
        self.nombre = nombre
        self.proveedor = proveedor
        self._cantidad = cantidad
        self.precio = precio

    def agregar_stock(self, cantidad):
        self._cantidad += cantidad

    def retirar_stock(self, cantidad):

        if cantidad > self._cantidad:
            raise ValueError("No hay suficiente stock")

        self._cantidad -= cantidad

    def __str__(self):
        return f"{self.nombre} - stock:{self._cantidad}"


class Almacen:

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.catalogo = []

    def agregar_repuesto(self, repuesto):
        self.catalogo.append(repuesto)

    def buscar_repuesto(self, nombre):

        for r in self.catalogo:
            if r.nombre == nombre:
                return r

        raise ValueError("Repuesto no encontrado")

    def mostrar_catalogo(self):

        for r in self.catalogo:
            print(r)


# USUARIOS

class Usuario(metaclass=ABCMeta):

    def __init__(self, nombre):
        self.nombre = nombre


class Comandante(Usuario):

    def comprar_repuesto(self, almacen, nombre_repuesto, cantidad):

        repuesto = almacen.buscar_repuesto(nombre_repuesto)
        repuesto.retirar_stock(cantidad)

        print(f"{self.nombre} compró {cantidad} de {nombre_repuesto}")


class OperarioAlmacen(Usuario):

    def agregar_repuesto(self, almacen, repuesto):
        almacen.agregar_repuesto(repuesto)


# CÓDIGO DE PRUEBA

if __name__ == "__main__":

    # crear nave
    nave = NaveEstelar(
        "ID-001",
        1234,
        "Destructor Imperial",
        5000,
        100,
        ClaseNave.EJECUTOR
    )

    nave.mostrar_info()

    # crear almacen
    almacen = Almacen("Base Imperial", "Espacio")

    # crear repuestos
    motor = Repuesto("Motor Hiperespacial", "Pedro", 10, 50000)

    # operario
    operario = OperarioAlmacen("Operario")
    operario.agregar_repuesto(almacen, motor)

    almacen.mostrar_catalogo()

    # comandante compra
    comandante = Comandante("Darth Vader")
    comandante.comprar_repuesto(almacen, "Motor Hiperespacial", 2)

    almacen.mostrar_catalogo()