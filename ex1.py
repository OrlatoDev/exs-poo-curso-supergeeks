class Cafeteira:
    def __init__(self):
        self.capacidade = 500
        self.quantidade = 500
        self.porcao = 30
    
    def servir_cafe(self, porcoes):
        self.quantidade -= self.porcao * porcoes

        if self.quantidade <= 0:
            print("Acabou o café, recarregando...")
            self.quantidade = self.capacidade
            return

        print(f"Servido. Café restante: {self.quantidade}ml")

    def get_cafe(self):
        print(f"Café restante: {self.quantidade}ml")

c = Cafeteira()
c.get_cafe()
c.servir_cafe(7)
c.servir_cafe(20)
c.get_cafe()
