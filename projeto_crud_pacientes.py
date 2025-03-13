import tkinter as tk
from tkinter import Image, PhotoImage, messagebox
from PIL import Image, ImageTk
import sqlite3
import time

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
        c.execute("INSERT INTO pacientes (nome, idade, telefone) VALUES (?,?,?)", (nome, idade, telefone))
        conn.commit()
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
        
        # Limpar os campos do formulário
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
        tk.Button(frame, text="Excluir", command=lambda pid=paciente[0]: excluir_paciente(pid)).pack(side="right")

def excluir_paciente(paciente_id):
    c.execute("DELETE FROM pacientes WHERE id = ?", (paciente_id,))
    conn.commit()
    messagebox.showinfo("Sucesso", "Paciente excluído!")
    listar_pacientes()

def editar_paciente(paciente_id):
    global entry_nome, entry_idade, entry_telefone, btn_enviar
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

def alternar_tema():
    # Alternar entre modo claro e escuro
    if root.cget("bg") == "white":
        root.config(bg="black")
        frame_lista.config(bg="black")
        btn_tema.config(bg="gray", fg="white", text="Modo Claro")
        btn_enviar.config(bg="gray", fg="white")
        for widget in root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Entry)):
                widget.config(bg="black", fg="white", insertbackground="white")
    else:
        root.config(bg="white")
        frame_lista.config(bg="white")
        btn_tema.config(bg="SystemButtonFace", fg="black", text="Modo Escuro")
        btn_enviar.config(bg="SystemButtonFace", fg="black")
        for widget in root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Entry)):
                widget.config(bg="white", fg="black", insertbackground="black")

# Tela de carregamento
def splash_screen():
    splash = tk.Toplevel()
    splash.geometry("400x300")
    splash.title("Carregando...")
    splash.configure(bg="white")

    # Carregar e redimensionar a imagem usando Pillow
    imagem_original = Image.open("logo.png")  # Substitua "logo.png" pelo caminho da sua imagem
    imagem_redimensionada = imagem_original.resize((200, 200))  # Alterar para altura e largura desejadas
    imagem = ImageTk.PhotoImage(imagem_redimensionada)

    # Exibir a imagem redimensionada no centro
    tk.Label(splash, image=imagem, bg="white").pack(expand=True)

    # Atualizar tela e pausar por 2 segundos
    splash.update()
    time.sleep(2)

    splash.destroy()

    # Garantir que a imagem não seja coletada pelo garbage collector
    splash.imagem = imagem

# Início do programa
root = tk.Tk()
root.withdraw()  # Esconde a janela principal temporariamente
splash_screen()
root.deiconify()  # Mostra a janela principal

root.title("Cadastro de Pacientes")
root.geometry("400x400")

label_nome = tk.Label(root, text="Nome")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_idade = tk.Label(root, text="Idade")
label_idade.pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

label_telefone = tk.Label(root, text="Telefone")
label_telefone.pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

btn_enviar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_enviar.pack(pady=10)

# Botão para alternar tema no topo direito
btn_tema = tk.Button(root, text="Modo Escuro", command=alternar_tema)
btn_tema.place(relx=1.0, rely=0.0, anchor="ne")

frame_lista = tk.Frame(root)
frame_lista.pack()

listar_pacientes()

root.mainloop()
