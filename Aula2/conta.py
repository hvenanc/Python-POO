class Conta:
    def __init__(self,numero,titular,saldo,limite):

        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self,valor_deposito):
        self.saldo += valor_deposito

    def sacar(self,valor_saque):
        if self.saldo < valor_saque:
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor_saque

    def extrato(self):
        print(f'A conta de número {self.numero} é de R$ {self.saldo}')

### Para verificar um atributo de objeto devemos usar seguinte sintaxe: objeto.nome_atributo