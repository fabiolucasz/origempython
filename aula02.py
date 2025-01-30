import tkinter as tk
from tkinter import messagebox 

#Tela inicial
root = tk.Tk()
root.title("Formulário")

#Campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

#Botão enviar
botao_enviar = tk.Button(root, text="Enviar", command=enviar_dados)
botao_enviar.pack()








#iniciar a interface
root.mainloop()