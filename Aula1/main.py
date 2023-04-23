def criar_conta(numero, nome, saldo, limite):
    conta = {"numero":numero, "nome":nome, "saldo":saldo, "limite":limite}
    return conta

def depositar(conta,valor_deposito):
    conta['saldo'] += valor_deposito

def sacar(conta,valor_saque):
    conta['saldo'] -= valor_saque

def extrato(conta):
    print('Sua conta de número {}'.format(conta['numero']) + ' possui saldo de {}'.format(conta['saldo']))