from datetime import date

class Funcionario:
    def __init__(self,nome,data_nascimento,salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_de_nascimento_quebrada = self._data_nascimento.split("/")
        ano_nascimento = data_de_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return  nome_quebrado[-1]


    def eh_socio(self):
        sobrenome = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000 and (self.sobrenome() in sobrenome))


    def decrescime_salario(self):
        if self.eh_socio():
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo

    def calcular_bonus(self):
        valor = self._salario *0.1
        if valor > 1000:
            raise Exception('o salario é muito alto para receber bonus')
        return valor

    def __str__(self):
        return f"Funcionario({self._nome},{self._data_nascimento},{self._salario})"