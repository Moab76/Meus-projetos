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

class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
    
    def deposita(self, valor, trans=0):
        self._saldo += valor - 0.10

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
    

class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

        


if __name__ == '__main__':
    #c = Conta()
    #Traceback (most recent call last):
    #File "/home/andersson/Área de trabalho/atividade 13-12/10-9classeabstrata.py", line 32, in <module>
    #c = Conta()
    #    ^^^^^^^
    # TypeError: Can't instantiate abstract class Conta without an implementation for abstract method 'atualiza',

    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    print(cc.saldo)
    print(cp.saldo)

    ci = ContaInvestimento('123-6', 'Maria', 1000)
    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print(ci.saldo)