class ContaCorrente:
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def get_conta(self):
        return self.conta
    def get_nome(self):
        return self.nome
    def get_saldo(self):
        return self.saldo

    def set_nome(self, nome):
        print(f"O nome de {self.nome}, dono(a) da conta {self.conta}, alterado para {nome}")
        self.nome = nome

    def deposito(self, brl):
        self.saldo += brl
        print(f"{self.nome}: Depósito de R${brl} realizado com sucesso")
    
    def saque(self, brl):
        if self.saldo < brl:
            print(f"{self.nome}: Saldo insuficiente! Não foi possível realizar um saque de R${brl}")
            return

        self.saldo -= brl
        print(f"{self.nome}: Saque de R${brl} realizado com sucesso")
