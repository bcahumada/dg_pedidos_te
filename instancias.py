from te import Te  

# Obs: 
# te_2 no es una instancia de la clase Te, es un str con el valor "Te".
# Para cumplir con los requerimientos, te_2 debe ser otra instancia de la clase Te.

te_1 = Te()  
te_2 = Te()  # instancia de la clase Te

# Obs
# Almacenamos el tipo de dato de te_2, que es incorrecto en el código original
# ya que te_2 era un string. Con la corrección, te_2 es una instancia de la clase Te.

tipo_1 = type(te_1)  
tipo_2 = type(te_2)  # ahora almacena el tipo de dato de te_2, que es <class 'Te'>

print(tipo_1)  
print(tipo_2)  



if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")  
else:
    print("Los objetos no son del mismo tipo")  
