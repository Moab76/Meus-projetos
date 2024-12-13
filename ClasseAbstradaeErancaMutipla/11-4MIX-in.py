import abc

class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    @property
    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        if valor > 0:
            self._saldo += valor

            print("Valor depositado!")

            return
        
        print("valor invalido!")
    
    @abc.abstractmethod
    def atualiza():
        pass


class TributavelMixIn:
    def get_valor_imposto(self):
        pass



class ContaCorrente(Conta, TributavelMixIn):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
    
    def deposita(self, valor, trans=0):
        self._saldo += valor - 0.10
    
    def get_valor_imposto(self):
        return self._saldo * 0.01

class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice
    
    def get_valor_imposto(self):
        return 42 + self._valor * 0.05

class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()

        return total
        

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
    

class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


if __name__ == '__main__':
    
    cc1 = ContaCorrente('123-4', 'João', 1000.0)
    cc2 = ContaCorrente('123-4', 'José', 1000.0)
    seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')
    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)
    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)
    print(total)