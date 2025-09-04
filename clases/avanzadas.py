class Operaciones:
    def __init__(self):
        self.base = 0
        self.exponente = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.base = float(input("Número base: "))
                self.exponente = float(input("Numero exponente: "))
                break
            except ValueError:
                print("Número inválido. Intenta de nuevo.")
    
    def potencia(self):
        self.resultado = self.base ** self.exponente
    
    def mostrarResultado(self):   
        print(f"{self.base} elevado a {self.exponente} es igual a {self.resultado}")
