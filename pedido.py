from te import Te  

# Solicitar el sabor del té al usuario
sabor = int(
    input(
        "¿Qué sabor de té desea? (Ingrese número de la opción)"
        "\n1. Té negro \n2. Té verde \n3. Té de hierbas\n"
    )
)

# Solicitar el formato al usuario
formato = int(
    input(
        "¿Qué formato desea?. Tenemos disponible"
        " 300 y 500 gramos. Ingrese la cantidad de gramos deseada\n"
    )
)

# Observación: Se está utilizando el método incorrecto para obtener tiempo y recomendación
# porque se está llamando a 'retorna_precio' en lugar de 'retorna_tiempo_y_recomendacion'

# Corrección
tiempo, recomendacion = Te.retorna_tiempo_y_recomendacion(sabor)  
precio = Te.retorna_precio(formato)  


# Observación: En la comparación de sabor, se menciona "Té rojo" en lugar de "Té verde".
# También hay una pequeña inconsistencia en los nombres de los tipos de té según lo indicado en la descripción del problema.

if sabor == 1:
    sabor_texto = "Té negro"  
elif sabor == 2:
    sabor_texto = "Té verde"  #  "Té rojo" a "Té verde"
elif sabor == 3:
    sabor_texto = "Infusión de hierbas"  

# Mostrar el resumen del pedido utilizando los valores correctos
print(
    "Se ingresó su pedido de {}, en formato de {} gramos,"
    "el cual tiene un valor de ${}. Este té tiene un tiempo "
    "de preparación de {} minutos, y se recomienda su uso {}.".format(
        sabor_texto, formato, precio, tiempo, recomendacion
    )
)
