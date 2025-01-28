# Encapsulamento em Python

#Encapsulamento é o princípio que define como os atributos e métodos 
# de uma classe podem ser acessados, permitindo proteger dados 
# sensíveis e restringir alterações indesejadas.

#Público (public): Pode ser acessado de qualquer lugar.
#Protegido (protected): Deve ser acessado apenas pela classe e subclasses (indicado com um _ antes do nome).
#Privado (private): Só pode ser acessado dentro da própria classe (indicado com __ antes do nome).

#Exemplo
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público
        self._saldo = saldo  # Protegido
        self.__senha = "1234"  # Privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self._saldo}")

# Criando um objeto
conta = ContaBancaria("João", 500)

# Acessando atributos e métodos
conta.exibir_saldo()
conta.depositar(200)
conta.sacar(100)
conta.sacar(200)
conta.depositar(1000)
print(conta._saldo)  # Acessando atributo protegido (não recomendado)
# print(conta.__senha)  # Gerará erro, pois o atributo é privado.
