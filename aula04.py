import tkinter as tk
import sqlite3

def salvar_dados():
    nome = entry_nome.get()
    email = entry_email.get()

    conn =  sqlite3.connect('formulario.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL
                   )
                   ''')
    
    cursor.execute('''
        INSERT INTO usuarios (nome, email)
        VALUES(?,?)
    ''', (nome,email))

    conn.commit()
    conn.close()

    


    

root = tk.Tk()
root.title("Formulário")

label_nome = tk.Label(root, text="Nome")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=2, column=5)

label_email = tk.Label(root, text="Email")
label_email.grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=5)

btn_enviar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_enviar.grid(row=5, column=0)

root.mainloop()