#Aula 1
from main import *

conta1 = criar_conta(123,'Henrique',55.0,150.00)

depositar(conta1,500.00)
sacar(conta1, 350.00)
extrato(conta1)

print(conta1)