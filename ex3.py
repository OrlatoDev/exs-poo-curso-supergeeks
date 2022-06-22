from ex3_classe import ContaCorrente

cc1 = ContaCorrente("00000-0", "Cleiton Silva Ronto")
cc2 = ContaCorrente("00001-0", "Maria Claudete Campos", 2000)

cc1.deposito(500)
print(cc1.get_saldo())

cc2.saque(250)
print(cc2.get_saldo())

cc1.set_nome("Cleiton Silva")
cc1.saque(537925738253)
print(cc1.get_saldo())
