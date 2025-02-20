import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("lanchonete.db")
c = conn.cursor()

# Criar tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                validade TEXT,
                preco TEXT
            )''')
conn.commit()

def salvar_dados():
    nome = entry_nome.get()
    validade = entry_validade.get()
    preco = entry_preco.get()

    if nome and validade and preco:

        c.execute("INSERT INTO produtos (nome, validade, preco) VALUES (?,?,?)", (nome,validade,preco))
        conn.commit()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        
        #limpar os campos do formulário
        entry_nome.delete(0, tk.END)
        entry_validade.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        listar_produtos()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")


def listar_produtos():
    for widget in frame_lista.winfo_children():
        widget.destroy()
    
    c.execute("SELECT * FROM produtos")
    produtos = c.fetchall()
    
    for produto in produtos:
        frame = tk.Frame(frame_lista)
        frame.pack()
        tk.Label(frame, text=f"ID: {produto[0]} - Nome: {produto[1]} - Validade: {produto[2]} - Preço: {produto[3]}").pack(side="left")
        tk.Button(frame, text="Editar", command=lambda pid=produto[0]: editar_produto(pid)).pack(side="right")
        #tk.Button(frame, text="Excluir", command=lambda pid=produto[0]: excluir_paciente(pid)).pack(side="right")

def editar_produto(produto_id):
    global entry_nome, entry_validade, entry_preco, btn_cadastrar
    c.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = c.fetchone()
    
    if produto:
        entry_nome.delete(0, tk.END)
        entry_validade.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        
        entry_nome.insert(0, produto[1])
        entry_validade.insert(0, produto[2])
        entry_preco.insert(0, produto[3])
        
        btn_enviar.config(text="Atualizar", command=lambda: atualizar_produto(produto_id))

def atualizar_produto(paciente_id):
    nome = entry_nome.get()
    validade = entry_validade.get()
    preco = entry_preco.get()
    
    if nome and validade and preco:
        c.execute("UPDATE produtos SET nome=?, validade=?, preco=? WHERE id=?", (nome, validade, preco, paciente_id))
        conn.commit()
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_validade.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        btn_enviar.config(text="Cadastrar", command=salvar_dados)
        listar_produtos()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

root = tk.Tk()
root.title("Cadastro de Pacientes")
root.geometry("400x400")


label_nome = tk.Label(root, text="Nome").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_validade = tk.Label(root, text="Validade").pack()
entry_validade = tk.Entry(root)
entry_validade.pack()

label_preco = tk.Label(root, text="Preço").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

btn_enviar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_enviar.pack(pady=10)

frame_lista = tk.Frame(root)
frame_lista.pack()

listar_produtos()

root.mainloop()
