# Crear la traspuesta de una matriz de nx m.

def  MatrizTraspuesta ( Matriz ):
    if  isinstance (Matriz, list ) y Matriz ! = []:
        return MatrizTraspuesta_aux (Matriz, [], [], 0 , 0 , len (Matriz), len (Matriz [ 0 ]))
    else : devuelve  " Error "

def  MatrizTraspuesta_aux ( matriz , resultado , nueva_fila , fila , columna , longitud_fila , longitud_columna ):
    si columna == longitud_columna:
        resultado de devolución
    elif fila == longitud_fila:
        return MatrizTraspuesta_aux (matriz, resultado + [nueva_fila], [], 0 , columna + 1 , longitud_fila, longitud_columna)
    else :
        return MatrizTraspuesta_aux (matriz, resultado, nueva_fila + [matriz [fila] [columna]], fila +  1 , columna, longitud_fila, longitud_columna)
