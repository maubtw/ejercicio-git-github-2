import math  # Importamos el módulo math

class Operaciones:
    def __init__(self):
        self.base = 0
        self.exponente = 0
        self.resultado = 0

    def leerNumeros(self):
        while True:
            try:
                self.base = float(input("Número base: "))
                self.exponente = float(input("Número exponente: "))
                break
            except ValueError:
                print("Número inválido. Intenta de nuevo.")

    def potencia(self):
        self.resultado = self.base ** self.exponente

    def raizCuadrada(self):
        if self.base < 0:
            print("No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            raiz = math.sqrt(self.base)
            print(f"La raíz cuadrada de {self.base} es {raiz}")

    def mostrarResultado(self):   
        print(f"{self.base} elevado a {self.exponente} es igual a {self.resultado}")
