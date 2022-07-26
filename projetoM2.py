import pandas as pd
import os
from datetime import datetime
from time import sleep

class Questionario:

    # Método que quando instanciado, cria o arquivo csv com o cabeçalho definido na linha 14.
    def to_csv(self, item):
        self.item = item

        with open('pesquisa.csv', 'w'):
            item_df = pd.DataFrame(item, columns=['Nome', 'Gênero', 'Idade', 'Pergunta 1', 'Pergunta 2', 'Pergunta 3', 'Pergunta 4', 'Hora', 'Data'])
            item_df.to_csv('pesquisa.csv')
     
    # Método que quando instanciado, avalia as respostas do usuário às perguntas da pesquisa, certificando que apenas os valores válidos sejam inseridos.
    def checkRespostas(self,chave):
        self.chave = chave
        pergunta = int(input(valor))
        ciclo = True

        while ciclo == True:

            if pergunta == 1:
                dados[self.chave].append('Sim')
                pass
            elif pergunta == 2:
                dados[self.chave].append('Não')
                pass
            elif pergunta == 3:
                dados[self.chave].append('Não soube responder')
                pass
            else:
                print('\nEscolha inválida, coloque um número que corresponde aos dados pelo sistema.')
                sleep(1)
                pesquisa.checkRespostas(self.chave)
            ciclo = False

    # Método que quando instanciado, checa se o input do usuário para seleção de gênero está dentro dos valores válidos definidos.
    def checkGenero(self,chave):
        self.chave = chave
        ciclo = True

        while ciclo == True:
            genero = int(input('\n[1] Masculino\n[2] Feminino\n[3] Outros\n[4] Prefiro não informar\n\nEscolha: '))
            if genero == 1:
                dados[chave].append('Masculino')
            elif genero == 2:
                dados[chave].append('Feminino')
            elif genero == 3:
                dados[chave].append('Outros')
            elif genero == 4:
                dados[chave].append('Preferiu não informar')
            else:
                print('Escolha inválida!')
                pesquisa.checkGenero(self.chave)
            ciclo = False
    
    # Método que quando instanciado, checa se o arquivo da pesquisa já contém um registro da mesma pessoa, garantindo apenas um registro por pessoa, evitando duplicatas.
    def checkNome(self, chave):
        self.chave = chave
        nome = input(valor) 
        ciclo = True

        while ciclo == True:

            if self.chave == 'Nome':
                if nome not in dados[self.chave]:
                    dados[self.chave].append(nome)

                else:
                    print('Essa pessoa já respondeu a pesquisa. Será aceito apenas um registro por pessoa.\n\n')
                    pesquisa.checkNome(self.chave)
            ciclo = False
 
#============================================================================================================================================================================================================================================#
# Dicionário que vai abrigar o nome e a idade das pessoas entrevistadas
dicionarioDados = {
    'Nome': 'Insira seu nome: ', 
    'Gênero': 'Insira seu Gênero: '
    }

# Dicionário que vai abrigar as respostas as 4 perguntas da pesquisa sobre impactos da pandemia de Covid-19 na vida pessoal do entrevistado.
dicionarioPerguntas = {
    'Pergunta 1': '\nSuas finanças foram impactadas de maneira significativa devido a pandemia de Covid-19?\n(Ex: redução salarial, demissão, necessidade de fazer horas extras para complementar a renda)\nEscolha: ',
    'Pergunta 2': '\nVocê sofreu com algum tipo de impacto na sua saúde mental durante a pandemia de Covid-19?\n(Ex: desenvolvimento de transtornos mentais, ansiedade, depressão, dificuldade em relacionamentos interpessoais)\nEscolha: ',
    'Pergunta 3': '\nVocê enfrentou algum tipo de complicação ou debilitação na sua saúde física devido a pandemia de Covid-19?\n(Ex: Aumento de peso, Hipertensão, Diabetes)\nEscolha: ',
    'Pergunta 4': '\nA sua vida escolar/sua educação ou a da sua família foi afetada em meio a pandemia de Covid-19?\n(ex: ausência de aulas, ausência de recursos para estudar online, escolas sem preparo para aulas online)\nEscolha: '
    }

# Instanciando a Classe Questionário e iniciando o sistema.
pesquisa = Questionario()
sistema = True
num_registro = 0

print("=*"*60)
print('Pesquisa sobre o impacto da pandemia de Covid-19 na sociedade.'.center(120))
print('A seguir, leia com atenção e responda com honestidade as perguntas do questionário.'.center(120))
print('Agradeçemos a sua colaboração nessa pesquisa!'.center(120))

while sistema == True:
    num_registro += 1
    time = datetime.now() # Método built-in da biblioteca datetime do Python que grava a hora exata em que o questionário começa a ser respondido pelo usuário.
    print("=*"*60)
    sleep(1)
    print(f'<<< Registro {num_registro} >>> \n')
    idade = int(input("Insira sua idade (apenas com números): "))

    if idade == 00:
        print('Encerrando a pesquisa...')
        sleep(1)
        print('Pesquisa encerrada! Para analisar os resultados, abra o arquivo "pesquisa.csv" num programa de visualização compatível (Excel, Planilhas Google, etc.)')
        sistema = False

    else:

        if os.path.exists('pesquisa.csv'): # Checa se o arquivo 'pesquisa.csv' já existe, caso sim, o programa lê o arquivo e aloja os valores no dicionario de dados.
            df = pd.read_csv('pesquisa.csv')
            dados = {'Nome': df['Nome'].tolist(), 'Gênero':df['Gênero'].tolist(), 'Idade': df['Idade'].tolist(), 'Pergunta 1':df['Pergunta 1'].tolist(), 'Pergunta 2': df['Pergunta 2'].tolist(), 'Pergunta 3':df['Pergunta 3'].tolist(), 'Pergunta 4':df['Pergunta 4'].tolist(), 'Hora':df['Hora'].tolist(), 'Data': df['Data'].tolist()}   
       
        else: # Caso o arquivo não exista, o programa cria o dicionário dados vazio, para poder alojar os participantes da pesquisa.
            dados = {'Nome': [],
            'Gênero':[],
            'Idade': [], 
            'Pergunta 1':[],
            'Pergunta 2':[],
            'Pergunta 3':[], 
            'Pergunta 4':[], 
            'Hora':[], 
            'Data':[]}
        
        dados['Idade'].append(idade)

        # Loop for que percorre os items do dicionarioDados, para depois chaamr os métodos de validação de nome e gênero.
        for chave, valor in dicionarioDados.items():
            if chave == 'Gênero':
                print(valor)
                pesquisa.checkGenero(chave)
            if chave == 'Nome':
                pesquisa.checkNome(chave)

        print('\nRegistrando dados...')
        sleep(1)
        print('Participante adicionado com sucesso!\n')
        print("=*"*60)
        sleep(1)
        print('\nDigite o número correspondente à resposta para as perguntas a seguir.\n[1] Sim\n[2] Não\n[3] Não soube responder.\n')
        print("=*"*60)
        sleep(1)
        # Loop for que percorre os items do dicionarioPerguntas, para depois chamar o método de avaliar as resposatas dadas as perguntas. 
        # Caso as respostas sejam válidas, serão atribuídas ao valor da chave da pergunta respondinda.
        for chave, valor in dicionarioPerguntas.items():
            pesquisa.checkRespostas(chave)

        # Com todas as perguntas respondidas, o programa insere no dicionário a data e a hora em que a pesquisa foi realizada.
        dados["Data"].append(time.strftime('%d/%m/%Y'))
        dados['Hora'].append(time.strftime('%H:%M:%S'))

        # Com tudo feito, o programa cria o arquivo csv caso não exista, ou apenas envia os dados coletados do dicionário 'dados' para o arquivo csv, utilizando
        # o método criar_csv.
        pesquisa.to_csv(dados)