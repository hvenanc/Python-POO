class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print(f'Criando objeto: {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self,valor_deposito):
        self.__saldo += valor_deposito

    def sacar(self,valor_saque):
        if self.__saldo < valor_saque:
            print('Saldo Insuficiente')
        else:
            self.__saldo -= valor_saque

    def transferir(self,destino,valor_transferencia):
        if self.__saldo < valor_transferencia:
            print('Saldo Insuficiente')
        else:
            self.sacar(valor_transferencia)
            destino.depositar(valor_transferencia)

    def get_limite(self):
        return self.__limite

    def set_limite(self,limite):
        self.__limite = limite

    def extrato(self):
        print(f'A conta de número {self.__numero} é de R$ {self.__saldo}')

### Para verificar um atributo de objeto devemos usar seguinte sintaxe: objeto.nome_atributo