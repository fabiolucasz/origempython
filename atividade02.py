import tkinter as tk
from tkinter import messagebox

def enviar_dados():
    nome = entry_nome.get()

    #mensagem
    messagebox.showinfo("Dados enviados", f"Nome: {nome}")

#Janela principal
root = tk.Tk()
root.title("Formulário")

#Itens do formulário
label_nome = tk.Label(root, text="Nome: ")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

#Botão enviar
botao_enviar = tk.Button(root, text="Enviar", command = enviar_dados)
botao_enviar.pack()


























#loop para iniciar
root.mainloop()
