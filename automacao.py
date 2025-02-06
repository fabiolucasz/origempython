# Aula 1: Introdução à Automação com Python



## 1. O que é Automação de Processos?
#Automação de processos consiste no uso de tecnologia para realizar tarefas repetitivas sem a necessidade de intervenção humana. Isso pode incluir:
#- Manipulação de arquivos
#- Envio de e-mails automáticos
#- Coleta e processamento de dados
#- Interação com sites e APIs

### Exemplos de Aplicações
#- Preenchimento automático de formulários
#- Extração de dados de planilhas
#- Agendamento de tarefas recorrentes



## 2. Benefícios da Automação
#A automação pode trazer diversas vantagens, como:
#- **Economia de tempo**: Reduz tarefas manuais repetitivas.
#- **Redução de erros**: Minimiza falhas humanas.
#- **Aumento da produtividade**: Libera tempo para tarefas mais estratégicas.
#- **Escalabilidade**: Permite o processamento de grandes volumes de dados rapidamente.


## 3. Estrutura Básica de um Script de Automação
#Todo script de automação segue uma estrutura básica:


# Importação de bibliotecas necessárias
import time

# Definição das funções principais
def tarefa_automatica():
    print("Executando tarefa automática...")
    time.sleep(2)  # Simula um processo
    print("Tarefa concluída!")

# Execução do script
tarefa_automatica()


#Explicação do código:
#- Importamos a biblioteca `time` para simular um atraso na execução.
#- Criamos uma função `tarefa_automatica` que imprime mensagens simulando um processo automático.
#- Chamamos a função para executar a automação.



## 4. Uso do Jupyter Notebook para Testes e Prototipação
#O Jupyter Notebook é uma ferramenta ideal para testar pequenos trechos de código antes de implementá-los em scripts maiores. Algumas vantagens incluem:
#- Execução de código em células
#- Visualização organizada dos resultados
#- Facilidade na depuração de erros

#Para iniciar um Jupyter Notebook, siga os passos:
#1. Instale o Jupyter se ainda não tiver:

#   pip install jupyter

#2. Execute o comando para abrir o ambiente:

#   jupyter notebook

#3. No navegador, crie um novo notebook e teste o código abaixo:

print("Teste de automação no Jupyter Notebook")


## Exercícios Práticos

### 1. Criando um Script de Automação Simples
#**Objetivo:** Criar um script que exiba uma mensagem automática de boas-vindas após um pequeno intervalo de tempo.


import time

def mensagem_automatica():
    print("Processando...")
    time.sleep(3)
    print("Bem-vindo ao curso de automação com Python!")

mensagem_automatica()


#**Pergunta:** O que acontece se mudarmos o valor dentro de `time.sleep(3)` para `time.sleep(1)`?


### 2. Criando uma Automação com Entrada do Usuário
#**Objetivo:** Criar um script que peça o nome do usuário e exiba uma mensagem personalizada após um intervalo de tempo.


import time

def saudacao_personalizada():
    nome = input("Digite seu nome: ")
    print("Processando...")
    time.sleep(2)
    print(f"Olá, {nome}! Seja bem-vindo à automação com Python.")

saudacao_personalizada()


#**Pergunta:** O que acontece se o usuário não digitar nada e pressionar "Enter"?


### 3. Criando uma Automação de Contagem Regressiva
#**Objetivo:** Criar um script que faça uma contagem regressiva automática antes de exibir uma mensagem final.


import time

def contagem_regressiva():
    for i in range(5, 0, -1):
        print(f"Contagem: {i}")
        time.sleep(1)
    print("Tempo esgotado!")

contagem_regressiva()


#**Pergunta:** Como podemos modificar o código para permitir que o usuário escolha o tempo inicial da contagem?





