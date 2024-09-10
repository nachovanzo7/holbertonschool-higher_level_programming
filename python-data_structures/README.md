# **Data Structures: Lists, Tuples**

### Listas (`list`)

- **Definición:** Las listas son colecciones ordenadas y mutables de elementos. Se definen usando corchetes `[]`.
- **Características:**
    - **Mutable:** Puedes modificar sus elementos (agregar, eliminar o cambiar).
    - **Tipos de datos mixtos:** Pueden contener elementos de diferentes tipos de datos.
    - **Indexación:** Los elementos se pueden acceder mediante índices (positivos o negativos).
    - **Slicing:** Puedes obtener sublistas usando slicing (`list[start:stop]`).
- **Métodos comunes:**
    - `append(x)`: Agrega un elemento `x` al final de la lista.
    - `insert(i, x)`: Inserta un elemento `x` en la posición `i`.
    - `remove(x)`: Elimina la primera aparición del elemento `x`.
    - `pop(i)`: Elimina y devuelve el elemento en la posición `i`.
    - `sort()`: Ordena la lista en orden ascendente.
    - `reversed()`: Invierte el orden de la lista.
    - `len()`: Devuelve la longitud de la lista.
    - `.copy()` : crea una nueva instancia del objeto, pero los elementos internos (si son objetos mutables) aún están referenciados desde el objeto original. Es decir, si la lista original contiene listas u otros objetos mutables como elementos, las modificaciones a esos elementos internos se reflejarán tanto en la copia como en el original.
    - `deepcopy()` : Para crear una copia completa que incluya copias independientes de los objetos internos, puedes usar el módulo `copy` y la función `deepcopy()`. Esto es útil si necesitas una copia independiente donde los cambios en el nuevo objeto no afecten al original ni a sus elementos internos.
    - `join()` : **`''.join(new_string)`**: Une todos los caracteres en `new_string` en una sola cadena, sin ningún separador entre ellos.

Ejemplo:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0bfdea0-f2d2-4741-9115-17f159793b1a/67f5e434-08d2-4309-86c8-c9ff70647b7c/image.png)

---

### Tuplas (`tuple`)

- **Definición:** Las tuplas son colecciones ordenadas e inmutables de elementos. Se definen usando paréntesis `()`.
- **Características:**
    - **Inmutable:** No se pueden modificar después de su creación.
    - **Tipos de datos mixtos:** Pueden contener elementos de diferentes tipos de datos.
    - **Indexación y Slicing:** Igual que en listas, se puede acceder y obtener subtuplas.
- **Uso:** Ideal para datos que no deben cambiar a lo largo del tiempo, como coordenadas (x, y) o días de la semana.
- **Métodos comunes:**
    - `count(x)`: Devuelve el número de veces que `x` aparece en la tupla.
    - `index(x)`: Devuelve la primera posición de `x` en la tupla.
    - **Nota:** No hay métodos como `append()` o `remove()` ya que las tuplas son inmutables.
- **Ejemplo:**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0bfdea0-f2d2-4741-9115-17f159793b1a/5d87153a-e6e4-43a5-9de2-7992ed4b3357/image.png)

### Diferencias clave entre listas y tuplas:

- **Mutabilidad:** Las listas son mutables, las tuplas no.
- **Rendimiento:** Las tuplas pueden ser más rápidas y usan menos memoria que las listas debido a su inmutabilidad.
- **Uso:** Las listas se usan para colecciones de datos que pueden cambiar, mientras que las tuplas se usan para datos fijos.

### Ejemplo de uso:

- **Lista:** Usada para una lista de tareas donde puedes agregar o eliminar elementos.
- **Tupla:** Usada para representar una fecha (año, mes, día), que no cambiará.