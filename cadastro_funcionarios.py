import customtkinter as ctk
from tkinter import *
 
window = ctk.CTk()
 
class Application():
 
    def __init__(self):
        self.window = window
        self.theme()
        self.screen()
        self.login_screen()
        window.mainloop()
 
    def theme(self):
 
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
 
    def screen(self):
 
        window.geometry("440x720")
        window.title("Sistema de Agendamento")
        window.resizable(False, False)
 
    def login_screen(self):
 
        tt_label = ctk.CTkLabel(master=window, text="Roomap", font=("Roboto", 20)).place(x=25, y=5)
 
        stt_label = ctk.CTkLabel(master=window, text="Faça login para entra no sistema", font=("Roboto", 10)).place(x=25, y=35)

        email_entry = ctk.CTkEntry(master=window, placeholder_text="Insira seu e-mail", width=300, font=("Roboto", 14)).place(x=25, y=105)
        email_entry1 = ctk.CTkEntry(master=window, placeholder_text="Insira seu e-mail", width=300, font=("Roboto", 14)).place(x=25, y=400)
        email_entry2 = ctk.CTkEntry(master=window, placeholder_text="Insira seu e-mail", width=300, font=("Roboto", 14)).place(x=25, y=500)

        email_label = ctk.CTkLabel(master=window, text="*O campo e-mail é obrigatorio", text_color="green", font=("Roboto", 8)).place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=window, placeholder_text="Insira sua senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=175)

        password_label = ctk.CTkLabel(master=window, text="*O campo senha é obrigatorio", text_color="green", font=("Roboto", 8)).place(x=25, y=205)

        chekbox = ctk.CTkCheckBox(master=window, text="Lembrar-se de mim").place(x=25, y=235)

        login_button = ctk.CTkButton(master=window, text="Login", width=300).place(x=25, y=285)

        register_button  = ctk.CTkButton(master=window, text="Cadastrar-se", width=150, fg_color="green", hover_color="#2D9334").place(x=175, y=325)

        register_label = ctk.CTkLabel(master=window, text="Se não tiver cadastro").place(x=25, y=325)
 
            
 
 
Application()