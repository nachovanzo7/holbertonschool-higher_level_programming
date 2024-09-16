# Clases/Objetos de Python

Una clase es como un constructor de objetos o un "modelo" para crear objetos.

# Crear una clase

Para crear una clase, use la palabra clave `class`:

class MyClass:
  x = 5

# Crear objeto
Ahora podemos usar la clase llamada MyClass para crear objetos:

p1 = MyClass()
print(p1.x)

# La función __init__()

Todas las clases tienen una función llamada `__init__()`, que siempre se ejecuta cuando la clase está siendo iniciada.

Utilice la función `__init__()` para asignar valores a las propiedades del objeto u otras operaciones que son necesarias hacer cuando el objeto se está creando:


### Cree una clase llamada Persona, use la función `__init__()` para asignar valores por nombre y edad:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


> **Nota:** La función `__init__()` se llama automáticamente cada vez que la clase se utiliza para crear un nuevo objeto.

# Métodos de objetos

Los objetos también pueden contener métodos. Los métodos en objetos son funciones que pertenecen al objeto.


Creemos un método en la clase `Persona`:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

> **Nota:** El parámetro `self` es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.