class ContaCorrente:
    def __init__(self, conta, nome, saldo = 0):
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
        print(f"Nome do(a) correntista {self.nome}, dono da conta {self.conta}, alterado para {nome}")
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

cc1 = ContaCorrente("00000-0", "Cleiton Silva Ronto")
cc2 = ContaCorrente("00001-0", "Maria Claudete Campos", 2000)

cc1.deposito(500)
print(cc1.get_saldo())

cc2.saque(250)
print(cc2.get_saldo())

cc1.set_nome("Cleiton Silva")
cc1.saque(537925738253)
print(cc1.get_saldo())
