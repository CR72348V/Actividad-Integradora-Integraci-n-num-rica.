print("Hola soy alexis")

nombre = "Alexis"

if nombre == "Alexis":
    print("Alexis bienvenido a python echale ganas!")




Stock = 200
if Stock > 0:
    print("El producto esta disponible en stock")
else:
    print("el producto no esta disponible en stock")


class producto:
    def __init__(self):
        self.nombre = "Donas Bimbo"
        self.precio = 18
    def mostrarinformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")

producto1 = producto()
producto1.mostrarinformacion()
p

