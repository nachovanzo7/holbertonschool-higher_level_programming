# Herencia en Python

La **herencia** es uno de los cuatro pilares de la programación orientada a objetos (POO), junto con la **abstracción**, el **polimorfismo** y el **encapsulamiento**. Permite que una clase "hija" o "derivada" herede atributos y métodos de una clase "padre" o "base". Esto facilita la reutilización de código y crea una relación jerárquica entre clases.

## Conceptos Clave

- **Clase base (padre)**: Es la clase de la que se heredan los atributos y métodos.
- **Clase derivada (hija)**: Es la clase que hereda de la clase base. Puede añadir o modificar los comportamientos heredados.
- **Super**: La función `super()` permite acceder a métodos y atributos de la clase base desde la clase derivada.

## Tipos de Herencia

- **Herencia simple**: Una clase hija hereda de una sola clase base.
- **Herencia múltiple**: Una clase hija hereda de múltiples clases base.
- **Herencia multinivel**: Una clase hija hereda de otra clase hija, creando una cadena de herencias.
- **Herencia jerárquica**: Varias clases hijas heredan de una misma clase base.

## La Función `super()`

La función `super()` es especialmente útil para invocar métodos de la clase base desde la clase hija. Es comúnmente usada cuando sobreescribimos métodos en la clase hija y aún queremos mantener parte del comportamiento de la clase base.

```python
class Vehiculo:
    def mover(self):
        return "El vehículo se está moviendo."

class Coche(Vehiculo):
    def mover(self):
        movimiento_base = super().mover()
        return f"{movimiento_base} El coche está avanzando."

mi_coche = Coche()
print(mi_coche.mover())  # El vehículo se está moviendo. El coche está avanzando.