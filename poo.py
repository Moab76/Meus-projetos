import csv
import os

class BD:
    def __init__(self, nome: str, colunas: list):
        self.nome = nome
        self.bancoExiste = os.path.isfile(self.nome)
        self.colunas = colunas

        if not self.bancoExiste:
            with open(self.nome, mode="w", newline='', encoding='utf-8') as bancoDeDados:

                escritor = csv.DictWriter(bancoDeDados, fieldnames=self.colunas)
                escritor.writeheader()
                print("Banco criado\n")

    def estarBanco(self, dados: list, tipo: str):
        #Saber se o usuario já esta no banco de dados
        
        with open(self.nome, mode='r', newline='', encoding='utf-8') as bancoDeDaos:
            leitor = csv.DictReader(bancoDeDaos)
            for linha in leitor:
                if linha[tipo] in dados:
                    return True
        return False


    def procurar(self,  dados):
            
        resultados = []

        with open(self.nome, mode='r', newline='', encoding='utf-8') as bancoDeDaos:
            leitor = csv.DictReader(bancoDeDaos)
            for linha in leitor:
                if any(item in list(linha.values()) for item in dados):
                    resultados.append(linha)
        
            return resultados 
        
        
    
    def escrever(self, dados: list):
        dados = dict(zip(self.colunas, dados))

        with open(self.nome, mode='a', newline='', encoding='utf-8') as bancoDeDados:
            
            escritor = csv.DictWriter(bancoDeDados, fieldnames=self.colunas)
            escritor.writerow(dados)


    def retornarID(self):
        with open(self.nome, mode='r', newline='', encoding='utf-8') as bancoDeDaos:
            leitor = csv.DictReader(bancoDeDaos)

            lastID = 0
            for linha in leitor:
                lastID = max(lastID, int(linha["ID"]))

            return lastID

class Usuarios:
    def __init__(self, nome: str, CPF: str, idade: int, login: str, senha: str):

        self.nome = nome
        self.CPF = CPF
        self.idade = idade
        self.login = login
        self.senha = senha

    def cadastrarUsuario(self, banco):

        Id = banco.retornarID() + 1
        dados = [
            Id,
            self.nome,
            self.CPF,
            self.idade,
            self.login,
            self.senha,
            self.adm
            ]
        
        if not banco.procurar(dados[1:5], True):
            banco.escrever(dict(zip(banco.colunas, dados)))
            print("Usuario cadastrado")
        else:
            print('Usuario ja cadastrado')
        
class Jogos:
    def __init__(self, nome: str, categoria: str, quantidade: int, lancamento: str):
        self.nome = nome
        self.categoria = categoria
        self.disponibilidade = True
        self.quantidade = quantidade
        self.lancamento = lancamento

    def cadrastrarJogo(self, BD):
        Id = BD.retornarID() + 1

        dados = [
           Id,
           self.nome,
           self.categoria,
           self.disponibilidade,
           self.quantidade,
           self.lancamento
        ]
        if not BD.procurar(dados[1:5]):
            BD.escrever(dados)

class Historico:
    def __init__(self, nomeUsuario: str):
        self.nomeUsuario = nomeUsuario 
        self.banco = BD(self.nomeUsuario + ".csv", ["Nome do Jogo", "Data do Aluguel", "Data da Entrega"])
        
    def registrarHistorico(self, nomeJogo: str, dataAluguel: str, entregaAliguel: str):
        self.nomeJogo = nomeJogo 
        self.dataAluguel = dataAluguel 
        self.entregaAluguel = entregaAliguel
        self.banco.escrever([self.nomeJogo, self.dataAluguel, self.entregaAluguel])
        print("Registrado!\n")


class Cliente(Usuarios):
    def __init__(self, nome: str, CPF: str, idade: int, login: str, senha: str):
        super().__init__(nome, CPF, idade, login, senha)
    
    def alugarJogo(self, nome: str, data: str):
        historico = Historico(self.nome)
        historico.registrarHistorico(nome, data, "não entregue")
    
    def devolverJogo(self):
        pass



        

class Adm(Usuarios):
    def __init__(self, nome: str, CPF: str, idade: int, login: str, senha: str):
        super().__init__(nome, CPF, idade, login, senha)
        
        
        
        

bancoUsuarios = BD("bancoUsuarios.csv", ["ID", "Nome", "CPF", "Idade", "Login", "Senha", "Adm"])
bancoJogos = BD("bancoJogos.csv", ["ID", "Nome", "Categoria", "Disponibilidade", "Quantidade", "Lançamento"])

chess = Jogos("Chess", "Quebra cabeças", 2, "10/11/2023")
chess.cadrastrarJogo(bancoJogos)

cliente = Cliente("Antonio", "08156516056", 18, "antonios.ud", "1956dfg")
if bancoJogos.estarBanco(["Chess"], 'Nome'):
    cliente.alugarJogo("Chess", "07/11/2024")


#Tema de cadastro de usuario

