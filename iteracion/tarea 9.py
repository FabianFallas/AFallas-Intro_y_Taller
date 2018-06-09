class Suma:
    def Sumaringresados(self):
        resultado= 0
        valoringresado = 0
        termina = True
        while termina:
            valoringresado = int(input("Ingrese valor:"))
            resultado += valoringresado
            if valoringresado == 0:
                termina = False
        print(resultado)
