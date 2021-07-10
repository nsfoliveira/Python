from Classe import Conta
conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)
conta.titular
conta2.titular

conta.extrato()

conta2.extrato()

conta.deposita(15.0)

conta.extrato()

conta.saca(10.0)
conta.extrato()

