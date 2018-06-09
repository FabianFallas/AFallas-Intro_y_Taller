 Secuencia de clase :
    def  serie ( self ):
        Inicio =  int ( entrada ( " Ingrese numero: " )) +  1
        Final =  int ( entrada ( " Ingrese numero: " ))
        resultado =  0
        mientras Inicio < Final:
            resultado = resultado + Inicio
            Inicio = Inicio +  1
        imprimir ( " La suma es " , resultado)
