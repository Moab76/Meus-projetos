from typing import List

class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._extrato = []
    
    def deposita(self, valor, trans=0):
        if valor > 0:
            self._saldo += valor
            
            if trans == 0:
                modelo = {
                    "Valor": valor,
                    "Tipo": "deposito"
                }

                self._extrato.append(modelo)

            print("Valor depositado!")

            return
        
        print("valor invalido!")

    
    def saca(self, valor):
        if self._saldo > valor and valor > 0:
            self._saldo -= valor

            modelo = {
                "Valor": valor,
                "Tipo": "deposito"
            }

            self._extrato.append(modelo)

            print("saque com sucesso")

            return
        
        print("Valor insuficiente") if valor < 0 else print("Saldo induficiente")

    def transfere_para(self, valor, origem):
        modelo = {
                "Conta-origem": origem._numero,
                "Nome-origem": origem._titular,
                "Valor": valor,
                "Tipo": "transferência"
            }

        origem.saca(valor)
        self.deposita(valor, 1)

        self._extrato.append(modelo)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
    
    def __str__(self):
        return f"Titular: {self._titular}\nNúmero: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite}."

    

class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
    
    def deposita(self, valor, trans=0):
        self._saldo += valor - 0.10

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    #propriedades
    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta:Conta):
        print(f"Saldo {conta._saldo}\n")
        conta.atualiza(self._selic)
        print(f"Saldo atualizado {conta._saldo}\n")
        self._saldo_total += conta._saldo
                
        


        
        
            

    
    


if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)
    adc = AtualizadorDeContas(0.01)
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)
    print('Saldo total: {}'.format(adc.saldo_total))