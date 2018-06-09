# Calcular la suma de todos los valores de una matriz de nxmy determinar el valor promedio de estos.

def  PromedioMatriz ( matriz ):
    if  isinstance (matriz, list ):
        return PromedioMatriz_aux (matriz, 0 , 0 , 0 , len (matriz), len (matriz [ 0 ]))
    else : devuelve  " Error "

def  PromedioMatriz_aux ( matriz , fila , columna , resultado , Longitud_fila , Longitud_columna ):
    if fila == Longitud_fila:
        Resultado de devolución / (Longitud_fila * Longitud_columna)
    elif columna == Longitud_columna:
        return PromedioMatriz_aux (matriz, fila + 1 , 0 , resultado, Longitud_fila, Longitud_columna)
    else :
        return PromedioMatriz_aux (matriz, fila, columna + 1 , resultado + matriz [fila] [columna], Longitud_fila, Longitud_columna)
