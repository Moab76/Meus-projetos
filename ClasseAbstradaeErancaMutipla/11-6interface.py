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


class Tributavel(abc.ABC):
    
    """ Classe que contém operações de um objeto autenticável
    As subclasses concretas devem sobrescrever o método get_valor_imposto.
    """
    @abc.abstractmethod
    def get_valor_imposto(self, valor):
        """ aplica taxa de imposto sobre um determinado valor do objeto """
        pass



class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
    
    def deposita(self, valor, trans=0):
        self._saldo += valor - 0.10
    
    def get_valor_imposto(self):
        return self._saldo * 0.01

class SeguroDeVida:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice
    
    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if (isinstance(t, Tributavel)):
                total += t.get_valor_imposto()
            else:
                print(t.__repr__(), "não é um tributavel")

        return total
        

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
    

class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


if __name__ == '__main__':
    cc = ContaCorrente('João', '123-4')
    cc.deposita(1000.0)
    seguro = SeguroDeVida(100.0, 'José', '345-77')
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    lista_tributaveis = []
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)
    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    cp = ContaPoupanca('123-6', 'Maria')
    lista_tributaveis.append(cp)
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)