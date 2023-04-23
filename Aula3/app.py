from conta import Conta

conta1 = Conta(123,'Henrique',50.0,150.50)
conta1.depositar(50)
conta1.sacar(30)

conta2 = Conta(565,'Joao',30.50,800.00)
conta2.depositar(34.50)
conta2.sacar(10)

conta1.transferir(conta2,70)

conta1.extrato()
conta2.extrato()
conta1.set_limite(2000)
x = conta1.get_limite()
print(x)

