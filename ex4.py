from ex3_classe import ContaCorrente

class ContaInvestimento(ContaCorrente):
    def __init__(self, conta, nome, taxa_juros, saldo=0):
        super().__init__(conta, nome, saldo)
        self.taxa_juros = taxa_juros

    def add_juros(self):
        self.saldo *= 1 + self.taxa_juros / 100

ci = ContaInvestimento("00000-1", "Joao Carlos Silva", 10, 1000)

ci.add_juros()
ci.add_juros()
ci.add_juros()
ci.add_juros()
ci.add_juros()

print(ci.get_saldo())