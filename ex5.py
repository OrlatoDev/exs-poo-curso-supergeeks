class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

f = Funcionario("Pedro", 10000)

print(f.get_nome())
print(f.get_salario())
