class Produto:

    def __init__(self,codigo,descricao,preco,estoque):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self,descricao):
        self.__descricao = descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self,preco):
        self.__preco = preco

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self,estoque):
        self.__estoque = estoque

    def __exibe_produto(self):
        print(f'******* PRODUTO *******\nCódigo: {self.__codigo}\nDescrição: {self.__descricao}\nPreço: {self.__preco}')

    def __pode_vender(self,quantidade):
        return quantidade < self.__estoque

    def venda(self,quantidade):
        if(self.__pode_vender(quantidade)):
            self.__estoque -= quantidade
            self.__exibe_produto()
            print(f'Quantidade: {quantidade}\nTotal a pagar RS: {self.__preco*quantidade}')
            print('Obrigado, Volte Sempre!')
        else:
            print('Estoque Indisponível!')