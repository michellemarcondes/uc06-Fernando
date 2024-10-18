import customtkinter as ctk
from tkinter import messagebox  # Importando messagebox
import os

window = ctk.CTk()

class Cadastro():
    def __init__(self):
        self.window = window
        self.theme()
        self.screen()
        self.cadastro_screen()
        self.criar_frame_secundario()
        window.mainloop()

    # Função para obter o caminho do arquivo
    def get_file_path(self):
        documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
        return os.path.join(documents_folder, "cadastro.txt")

    # Função para salvar os dados do cliente no arquivo .txt
    def salvar_cliente(self):
        name = self.nome_entry.get()  # Pega o nome digitado no campo de entrada de nome
        senha = self.senha_entry.get()
        salario = self.salario_entry.get()
        cargo = self.cargo_entry.get()
        lotacao = self.lotacao_entry.get()
        email = self.email_entry.get()  # Pega o email digitado no campo de entrada de email
        telefone = self.telefone_entry.get()  # Pega o telefone digitado no campo de entrada de telefone

        file_path = self.get_file_path()  # Obtém o caminho do arquivo

        try:
            # Validação dos dados
            if not self.nome_entry.get() or not self.senha_entry.get() or not self.email_entry.get() or not self.telefone_entry.get() or not self.salario_entry.get() or not self.cargo_entry.get() or not self.lotacao_entry.get():
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
    
            # Cria o arquivo se ele não existir
            if not os.path.exists(file_path):
                with open(file_path, "w") as arquivo:
                    arquivo.write("")
            try:
                # Tenta abrir o arquivo .txt para leitura
                with open(file_path, "r") as arquivo:
                    found = False  
                    for line in arquivo.readlines():
                        # Se o nome buscado estiver no arquivo, mostra a linha inteira
                        if self.nome_entry.get() in line and self.email_entry.get() in line and self.senha_entry.get() in line:
                            messagebox.showerror("Erro", "Cliente já cadastrado!")
                            found = True
                            break
                if not found:
                    # Abre o arquivo em modo de escrita
                    with open(file_path, "a") as arquivo:
                        data = f"Nome: {self.nome_entry.get()}, Senha: {self.senha_entry.get()}, Email: {self.email_entry.get()}, Telefone: {self.telefone_entry.get()}, Salario: {self.salario_entry.get()}, Cargo: {self.cargo_entry.get()}, Lotação: {self.lotacao_entry.get()}\n"
                        arquivo.write(data)  # Escreve os dados no arquivo
                        messagebox.showinfo("Sucesso", "Funcionario salvo com sucesso!")
                        self.clear_fields()
            except FileNotFoundError:
                messagebox.showerror("Erro", "Arquivo não encontrado. Por favor, verifique se o endereço do mesmo está correto.")
        except Exception as e: 
            messagebox.showerror("Erro", f"teste um erro: {str(e)}")    
    
    # Função para limpar os campos de entrada de texto
    def clear_fields(self):
        self.nome_entry.delete(0, ctk.END)  # Limpa o campo de entrada de nome
        self.email_entry.delete(0, ctk.END)  # Limpa o campo de entrada de email
        self.telefone_entry.delete(0, ctk.END)  # Limpa o campo de entrada de telefone
        self.senha_entry.delete(0, ctk.END)
        self.cargo_entry.delete(0, ctk.END)
        self.lotacao_entry.delete(0, ctk.END)
        self.salario_entry.delete(0, ctk.END)
        
    # Função para buscar um cliente no arquivo .txt
    def buscar_cliente(self):
        buscar_nome = self.email_entry.get().lower()  # Pega o nome a ser buscado e converte em minúsculas
        if not buscar_nome:
            messagebox.showwarning("Atenção", "Preencha o campo de busca para encontrar o cliente.")
            return

        file_path = self.get_file_path()  # Obtém o caminho do arquivo

        try:
            # Tenta abrir o arquivo .txt para leitura
            with open(file_path, "r") as arquivo:
                found = False  # Variável para verificar se o cliente foi encontrado
                # Percorre cada linha do arquivo
                for line in arquivo.readlines():
                    # Se o nome buscado estiver no arquivo, mostra a linha inteira
                    if buscar_nome in line.lower():
                        messagebox.showinfo("Cliente encontrado!", f"Dados: {line.strip()}")
                        found = True
                        break
                if not found:
                    messagebox.showinfo("Cliente não encontrado", "O cliente não foi encontrado no arquivo.")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado. Por favor, verifique se o endereço do mesmo está correto.")

    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def screen(self):
        window.geometry("700x600")  # largura x altura
        window.title("Sistema de Agendamento")
        window.resizable(False, False)

    def criar_frame_secundario(self):
        self.frame_secundario = ctk.CTkFrame(master=window, width=260, height=600)
        self.frame_secundario.place(x=0, y=0)
        self.frame_secundario.configure(fg_color="#4F4F4F")

    def cadastro_screen(self):
        #informações de cadastro:  nome, telefone, salario, cargo, lotação, email, senha
        self.tt_label = ctk.CTkLabel(master=window, text="Sistema de Cadastro de Funcionarios", font=("Roboto", 20)).place(x=310, y=20)

        self.stt_label = ctk.CTkLabel(master=window, text="Faça login para entrar no sistema", font=("Roboto", 15)).place(x=285, y=60)

        self.nome_entry = ctk.CTkEntry(master=window, placeholder_text="Insira o nome do funcionario", width=390, font=("Roboto", 14))
        self.nome_entry.place(x=285, y=90)

        self.nome_label = ctk.CTkLabel(master=window, text="*O campo nome é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=120)

        self.senha_entry = ctk.CTkEntry(master=window, placeholder_text="Insira a senha de login desse usuario", width=390, font=("Roboto", 14))
        self.senha_entry.place(x=285, y=151)

        self.senha_label = ctk.CTkLabel(master=window, text="*O campo senha é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=180)

        self.email_entry = ctk.CTkEntry(master=window, placeholder_text="Insira o email do funcionario", width=390, font=("Roboto", 14))
        self.email_entry.place(x=285, y=211)

        self.email_label = ctk.CTkLabel(master=window, text="*O campo e-mail é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=241)

        self.telefone_entry = ctk.CTkEntry(master=window, placeholder_text="Insira o telefone do funcionario", width=390, font=("Roboto", 14))
        self.telefone_entry.place(x=285, y=272)

        self.telefone_label = ctk.CTkLabel(master=window, text="*O campo telefone é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=301)

        self.salario_entry = ctk.CTkEntry(master=window, placeholder_text="Insira o salario do funcionario", width=390, font=("Roboto", 14))
        self.salario_entry.place(x=285, y=332)

        self.salario_label = ctk.CTkLabel(master=window, text="*O campo salario é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=362)

        self.cargo_entry = ctk.CTkEntry(master=window, placeholder_text="Insira o cargo do funcionario", width=390, font=("Roboto", 14))
        self.cargo_entry.place(x=285, y=393)

        self.cargo_label = ctk.CTkLabel(master=window, text="*O campo cargo é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=422)

        self.lotacao_entry = ctk.CTkEntry(master=window, placeholder_text="Insira a lotação do funcionario", width=390, font=("Roboto", 14))
        self.lotacao_entry.place(x=285, y=453)

        self.lotacao_label = ctk.CTkLabel(master=window, text="*O campo lotação é obrigatorio", text_color="green", font=("Roboto", 10)).place(x=285, y=483)

        login_button = ctk.CTkButton(master=window, text="Cadastrar Funcionario", width=284, command=self.salvar_cliente).place(x=338, y=524)

Cadastro()