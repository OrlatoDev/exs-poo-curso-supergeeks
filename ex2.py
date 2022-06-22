class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_peso(self):
        return self.peso
    def get_altura(self):
        return self.altura

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, metros):
        self.altura += metros

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)

        self.idade += anos

p = Pessoa("Jorge", 16, 50, 1.7)

print(p.get_idade())
print(p.get_altura())

p.envelhecer(1)

print(p.get_idade())
print(p.get_altura())
