import pandas as pd
import os
from datetime import datetime


dicionarioDados = {'Nome': 'Digite o nome do entrevistado: ', 'Gênero': 'Escolha Gênero do entrevistado: '}
dicionárioPerguntas = {'Pergunta 1': '\nVocê enfrenteu algum tipo impacto na sua saúde financeira? (Ex: redução salarial, demissão, necessidade de fazer horas extras para complementar a renda) ',
 'Pergunta 2': '\nVocê enfrentou algum tipo de impacto na sua saúde mental durante a pandemia? (Ex: desenvolvimento de transtornos mentais, ansiedade, depressão, dificuldade de relacionamento) ',
  'Pergunta 3': '\nVocê enfrentou algum tipo de impacto na sua saúde física durante a pandemia? (Ex: Aumento de peso, Hipertensão, Diabetes) ',
   'Pergunta 4': '\nVocê enfrentou algum tipo de impacto na sua educação ou da sua família durante a pandemia? (ex: ausência de aulas, ausência de recursos para estudar online, escolas sem preparo para aulas online) '
        }


class Questionario:


    def to_csv(self, item):
        self.item = item

        with open('teste.csv', 'w'):
            item_df = pd.DataFrame(item, columns=['Nome', 'Gênero', 'Idade', 'Pergunta 1', 'Pergunta 2', 'Pergunta 3', 'Pergunta 4', 'Hora', 'Data'])
            item_df.to_csv('teste.csv')
     
    def checkRespostas(self,chave):
        self.chave = chave
        pergunta = int(input(valor))

        while True:

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
                print('Escolha inválida, coloque um número que corresponde aos dados pelo sistema')
                pesquisa.checkRespostas(self.chave)
            break

    def checkGenero(self,chave):
        self.chave = chave
        while True:
            genero = int(input('\n\n[1] Masculino\n[2] Feminino\n[3] Outros\n[4] Prefiro não informar\n\nEscolha: '))
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
            break
    
    
    def checkNome(self, chave):
        self.chave = chave
        nome = input(valor) 
        while True:

            if self.chave == 'Nome':
                if nome not in dados[self.chave]:
                    dados[self.chave].append(nome)

                else:
                    print('Essa pessoa já respondeu a pesquisa, coloque um novo candidato.\n\n')
                    pesquisa.checkNome(self.chave)
            break
        
                
pesquisa = Questionario()

while True:
    time = datetime.now()
    idade = int(input("Digite a idade: "))

    if idade == 00:
        print('Encerrando a pesquisa')
 
    else:
        if os.path.exists('teste.csv'):
            df = pd.read_csv('teste.csv')
            dados = {'Nome': df['Nome'].tolist(), 'Gênero':df['Gênero'].tolist(), 'Idade': df['Idade'].tolist(), 'Pergunta 1':df['Pergunta 1'].tolist(), 'Pergunta 2': df['Pergunta 2'].tolist(), 'Pergunta 3':df['Pergunta 3'].tolist(), 'Pergunta 4':df['Pergunta 4'].tolist(), 'Hora':df['Hora'].tolist(), 'Data': df['Data'].tolist()}   
        else:
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


        for chave, valor in dicionarioDados.items():
            
            if chave == 'Gênero':
                print(valor)
                pesquisa.checkGenero(chave)
            if chave == 'Nome':
                pesquisa.checkNome(chave)


        print('\n\n Digite o número correspondente a resposta para a pergunta\n\n[1] Sim\n[2] Não\n[3] Não soube responder.\n')
        
        for chave, valor in dicionárioPerguntas.items():
            pesquisa.checkRespostas(chave)


        dados["Data"].append(time.strftime('%d/%m/%Y'))
        dados['Hora'].append(time.strftime('%H:%M:%S'))

        pesquisa.to_csv(dados)

