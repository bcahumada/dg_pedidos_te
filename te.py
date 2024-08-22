class Te:
    duracion = 365  

    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor):
        # Observaciones
        #1 Los tiempos de preparación y recomendaciones no son correctos según el enunciado.
        #2 El té negro (sabor 1) tiene un tiempo de preparación de 3 minutos y no 5.
        #3 El té verde (sabor 2) tiene un tiempo de preparación de 5 minutos y no de 4.
        #4 El agua de hierbas (sabor 3) tiene un tiempo de preparación de 6 minutos, no 7.
        #5 Las recomendaciones deben ser: 
        #6 para el té negro, "Se recomienda consumir al desayuno." 
        #7 para el té verde,"Se recomienda consumir al medio día."
        #8 y para el agua de hierbas, "Se recomienda consumir al atardecer."

        if sabor == 1:
            return (
                3,  # preparación del té negro es 3 minutos
                "Se recomienda consumir al desayuno.",  # Corregido: recomendación adecuada para el té negro
            )
        elif sabor == 2:
            return (
                5,  # preparación del té verde es 5 minutos
                "Se recomienda consumir al medio día.",  # recomendación para el té verde
            )
        elif sabor == 3:
            return (
                6,  # preparación del agua de hierbas es 6 minutos
                "Se recomienda consumir al atardecer.",  # recomendación para el agua de hierbas
            )
        else:
            return 0, "Sabor no válido"  

    @staticmethod
    def retorna_precio(formato):
        # Observaciones: 
        # Los precios para los formatos están invertidos.
        # El formato de 300 gramos debería costar $3,000 y el de 500 gramos $5,000.

        if formato == 500:
            return 5000  # formato de 500 gramos es $5,000
        elif formato == 300:
            return 3000  # formato de 300 gramos es $3,000
        else:
            return 0  
