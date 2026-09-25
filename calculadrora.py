class calculadora:
    def __init__(self, funcion, funcionderivada, aproxinicial, error):
        self.funcion = funcion
        self.funcionderivada = funcionderivada
        self.aproxinicial = aproxinicial
        self.error = error
    
    def newtonraphson(self):
        iteracion = 0

        errorAbsoluto = float('inf')

        if iteracion <= 30:
            while errorAbsoluto > error:
                ra = aproxinicial - ((funcion(aproxinicial)))/((funcionderivada(aproxinicial)))
                errorAbsoluto = abs(ra - aproxinicial)
                aproxinicial = ra
                iteracion += 1

            print("La raiz es: ", self.aproxinicial)

        else:
            print("Eror, el metodo no converge")
