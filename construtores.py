##Construtores e Destrutores

# O que são Construtores e Destrutores?

# Os construtores e destrutores são métodos especiais de uma classe que são 
# chamados automaticamente quando um objeto é criado ou destruído.

##Construtor (__init__)

#O método __init__ é chamado automaticamente quando um novo objeto da classe é 
# instanciado. Ele é utilizado para inicializar variáveis e preparar o objeto 
# para uso.

##Destrutor (__del__)

#O método __del__ é chamado automaticamente quando um objeto está prestes a ser 
# destruído. Ele é útil para liberar recursos, fechar conexões ou executar qualquer 
# tarefa de limpeza necessária.

#Exemplo:
class Robo:
    def __init__(self, nome):
        print(f"Iniciando o robô {nome}")
        self.nome = nome
    
    def __del__(self):
        print(f"Destruindo o robô {self.nome}")

# Criando e destruindo um objeto
robo1 = Robo("Wall-E")
del robo1  # Chama o destrutor explicitamente

## Exercícios

#1.Criando um Construtor
#Crie uma classe Carro com um construtor que recebe marca e modelo como parâmetros e imprime uma mensagem ao inicializar o objeto.

##2.Criando um Destrutor
#Modifique a classe Carro para incluir um destrutor que exibe uma mensagem quando o objeto for destruído.

##3. Gerenciando Recursos
#Crie uma classe ConexaoBD que simula uma conexão com um banco de dados. O construtor deve exibir uma mensagem ao conectar e o destrutor ao desconectar.
