from Classe import Conta

conta = Conta(182, "Natália", 60.00, 2000.00)

conta1 = Conta(1985, "Marco", 150.00, 18000.00)

conta3 = Conta(2020, "Dilma", 1500.00, 500.00)

conta1.transfere(50.00, conta)

conta.extrato()
