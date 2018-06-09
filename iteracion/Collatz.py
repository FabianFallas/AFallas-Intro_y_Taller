clase  Collatz :
    def  conjetura ( yo ):
        secuencia =  " "
        Inicio =  int ( input ( " Ingrese el valor de n: " ))
        secuencia = secuencia +  str (Inicio)
        imprimir ( " n: " , Inicio)
        mientras Inicio ! =  1 :
            si Inicio %  2  ==  0 :
                Inicio = Inicio //  2
                secuencia = secuencia +  "  "  +  str (Inicio)
            else :
                Inicio = Inicio *  3  +  1
                secuencia = secuencia +  "  "  +  str (Inicio)
        imprimir (secuencia)
    def  Imprimir ( auto ):
        Inicio =  int ( input ( " Ingrese el valor de n: " ))
        secuencia =  " "
        imprimir ( " n: " , Inicio)
        para g en  rango (Inicio):
            secuencia = secuencia +  " * "
        print ( str (Inicio), secuencia)
        secuencia =  " "
        mientras Inicio ! =  1 :
            si Inicio %  2  ==  0 :
                Inicio = Inicio //  2
                para g en  rango (Inicio):
                    secuencia = secuencia +  " * "
                print ( str (Inicio), secuencia)
                secuencia =  " "
            else :
                Inicio = Inicio *  3  +  1
                para g en  rango (Inicio):
                    secuencia = secuencia +  " * "
                print ( str (Inicio), secuencia)
                secuencia =  " "
