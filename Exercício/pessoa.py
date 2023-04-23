from datetime import datetime

class Pessoa:
    def __init__(self,nome,nascimento,sexo,altura):

        self.__nome = nome
        self.__nascimento = nascimento
        self.__sexo = sexo
        self.__altura = altura


    def imprimir(self):
        print(f'Nome: {self.__nome}\nData de Nascimento: {self.__nascimento}\nSexo: {self.__sexo}\nAltura: {self.__altura}')

    def idade(self):
        ano_nascimento = self.__nascimento.split('/')
        ano_atual = datetime.today().year
        idade = ano_atual - int(ano_nascimento[2])
        print(f'Idade: {idade}')


