import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("clinica.db")
c = conn.cursor()

# Criar tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                telefone TEXT
            )''')
conn.commit()

def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()

    if nome and idade and telefone:

        c.execute("INSERT INTO pacientes (nome, idade, telefone) VALUES (?,?,?)", (nome,idade,telefone))
        conn.commit()
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
        
        #limpar os campos do formulário
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        listar_pacientes()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")


def listar_pacientes():
    for widget in frame_lista.winfo_children():
        widget.destroy()
    
    c.execute("SELECT * FROM pacientes")
    pacientes = c.fetchall()
    
    for paciente in pacientes:
        frame = tk.Frame(frame_lista)
        frame.pack()
        tk.Label(frame, text=f"ID: {paciente[0]} - Nome: {paciente[1]} - Idade: {paciente[2]} - Telefone: {paciente[3]}").pack(side="left")
        tk.Button(frame, text="Editar", command=lambda pid=paciente[0]: editar_paciente(pid)).pack(side="right")
        #tk.Button(frame, text="Excluir", command=lambda pid=paciente[0]: excluir_paciente(pid)).pack(side="right")

def editar_paciente(paciente_id):
    global entry_nome, entry_idade, entry_telefone, btn_cadastrar
    c.execute("SELECT * FROM pacientes WHERE id = ?", (paciente_id,))
    paciente = c.fetchone()
    
    if paciente:
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        
        entry_nome.insert(0, paciente[1])
        entry_idade.insert(0, paciente[2])
        entry_telefone.insert(0, paciente[3])
        
        btn_enviar.config(text="Atualizar", command=lambda: atualizar_paciente(paciente_id))

def atualizar_paciente(paciente_id):
    nome = entry_nome.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()
    
    if nome and idade and telefone:
        c.execute("UPDATE pacientes SET nome=?, idade=?, telefone=? WHERE id=?", (nome, idade, telefone, paciente_id))
        conn.commit()
        messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        btn_enviar.config(text="Cadastrar", command=salvar_dados)
        listar_pacientes()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

root = tk.Tk()
root.title("Cadastro de Pacientes")
root.geometry("400x400")


label_nome = tk.Label(root, text="Nome").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_idade = tk.Label(root, text="Idade").pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

label_telefone = tk.Label(root, text="Telefone").pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

btn_enviar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_enviar.pack(pady=10)

frame_lista = tk.Frame(root)
frame_lista.pack()

listar_pacientes()

root.mainloop()