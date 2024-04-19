class Aluno:
      #Declarando os atributos da classe
    def __init__(self, nome, RA, idade):
        self.nome = nome
        self.RA = RA
        self.idade = idade
       
        #Declarando o metodo str que passara os atributos para string
    def __str__(self):
        return f"Nome: {self.nome}\nRA: {self.RA}\nIdade: {self.idade}"
    
    #Criando classe validação para verificar nome,RA e iadade
class Validacao:
    def __init__(self, nome, RA, idade):
        # Conferindo o nome
        if nome == "matheus":
            print("Nome correto:", nome)
        else:
            print("Nome incorreto")
        # Conferindo o RA
        if RA == "f354644":
            print("RA correto:", RA)
        else:
            print("RA incorreto")
        # Conferindo a idade
        if idade == 19:
            print("Idade correta:", idade)
        else:
            print("Idade incorreta")

# Solicitando informações do usuário
nome_usuario = input("Digite o nome do aluno: ")
RA_usuario = input("Digite o RA do aluno: ")
idade_usuario = int(input("Digite a idade do aluno: "))

#Instanciando a classe aluno com os valores das variaveis do input
aluno_matheus = Aluno(nome=nome_usuario, RA=RA_usuario, idade=idade_usuario)

# Instanciando a classe validação,passando as variaveis do input
validador = Validacao(nome=aluno_matheus.nome, RA=aluno_matheus.RA, idade=aluno_matheus.idade)

    












