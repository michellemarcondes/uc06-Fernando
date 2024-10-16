#Projeto interface-funcionario,diretor e gerente
#funcionario possui as funções de: Consultar lotação, salario, consultar cargo e solicitar aumento
#gerente possui as mesmas funções do funcionario, porem tbm pode mudar lotação, contratar e demitir funcionario
#diretor tem as mesmas funções da classe gerente, porem tbm pode mudar salario, contratar, mudar lotação e demitir funcionario ou gerente 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import customtkinter as ctk

# Configuração inicial do customtkinter
ctk.set_appearance_mode("dark")  # Modo de aparência (System, Light, Dark)
ctk.set_default_color_theme("dark-blue")  # Tema de cor

# Função para abrir a tela de home
def open_inicio_funcionario():
    # Fechar a janela de login
    login_window.destroy()
    
    # Criar a tela de home
    inicio_window = ctk.CTk()
    inicio_window.title("Inicio - Funcionario")
    inicio_window.geometry("300x200")

    # Adicionar uma mensagem de "Olá" na tela de home
    label_home = ctk.CTkLabel(inicio_window, text="Olá!")
    label_home.pack(pady=20)

    # Iniciar a interface gráfica da tela de home
    inicio_window.mainloop()

# Criar a tela de login
login_window = ctk.CTk()
login_window.title("Login")
login_window.geometry("300x200")

# Rótulo e entrada para o nome de usuário
label_usuario = ctk.CTkLabel(login_window, text="Usuário:")
label_usuario.pack(pady=10)
entry_usuario = ctk.CTkEntry(login_window)
entry_usuario.pack(pady=10)

# Rótulo e entrada para a senha
label_password = ctk.CTkLabel(login_window, text="Senha:")
label_password.pack(pady=10)
entry_password = ctk.CTkEntry(login_window, show="*")
entry_password.pack(pady=10)

# Botão de login que chama a função open_home
button_login = ctk.CTkButton(login_window, text="Login", command=open_home)
button_login.pack(pady=20)

# Iniciar a interface gráfica da tela de login
login_window.mainloop()
