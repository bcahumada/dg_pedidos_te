# Desafío de Programación Orientada a Objetos en Python

## Descripción del Proyecto

Este proyecto es una solución a un desafío de programación orientada a objetos (OOP) en Python. El objetivo es desarrollar una aplicación que permita a los usuarios generar un pedido de té de hoja artesanal. La aplicación permite seleccionar entre distintos sabores de té, elegir el formato deseado, y obtener detalles sobre el tiempo de preparación, recomendación de consumo, y el precio.

## Requerimientos

1. **Definición de la Clase `Te`:**
   - Crear una clase que permita instanciar objetos de tipo "Te".
   - Incluir atributos de clase y métodos estáticos para obtener tiempo de preparación, recomendación de consumo, y precio según el sabor y formato elegido por el usuario.

2. **Instancias de la Clase `Te`:**
   - Crear un archivo `instancias.py` donde se importará la clase `Te` y se crearán dos instancias.
   - Determinar y mostrar los tipos de datos de las instancias creadas.

3. **Generación de un Pedido:**
   - Crear un archivo `pedido.py` que permita al usuario ingresar los datos necesarios para generar un pedido de té.
   - Mostrar el resumen del pedido, incluyendo sabor, formato, precio, tiempo de preparación, y recomendación de consumo.

## Archivos

- `te.py`: Contiene la definición de la clase `Te` con métodos estáticos para obtener los detalles del té.
- `instancias.py`: Script que crea dos instancias de la clase `Te` y compara sus tipos de datos.
- `pedido.py`: Programa que permite al usuario ingresar los detalles de un pedido y muestra el resumen del mismo.

## Ejecución del Proyecto

### 1. Instancias de la Clase `Te`

Ejecuta `instancias.py` para ver cómo se crean y comparan las instancias de la clase `Te`.

```bash
python instancias.py
```

### 2. Generación de un pedido

Ejecución

```bash
python pedido.py
```

## Consideraciones
Se asume que el usuario siempre ingresará un valor válido (no se realizan validaciones adicionales).
Los valores de sabor y formato deben coincidir con las opciones proporcionadas por la aplicación.

### Ejemplo de Uso
Al ejecutar pedido.py, se le pedirá al usuario que seleccione un sabor y un formato de té. Luego, se le mostrará un resumen del pedido, incluyendo detalles como el tiempo de preparación y la recomendación de consumo.

```text
¿Qué sabor de té desea? (Ingrese número de la opción)
1. Té negro 
2. Té verde 
3. Té de hierbas

¿Qué formato desea?. Tenemos disponible 300 y 500 gramos. Ingrese la cantidad de gramos deseada
```

## Autor
Bárbara HA

### Github link
https://github.com/bcahumada/dg_pedidos_te
