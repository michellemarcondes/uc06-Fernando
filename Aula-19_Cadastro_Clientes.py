# Importação dos módulos necessários do Tkinter para criar a interface gráfica
import tkinter as tk  # Usado para a interface gráfica principal
from tkinter import ttk  # Usado para widgets estilizados
from tkinter import messagebox  # Usado para exibir mensagens
import os  # Usado para manipulação de arquivos e diretórios (Não utilizamos nesse exemplo)

# Função para salvar os dados do cliente no arquivo .txt
def salvar_cliente():
    name = entry_name.get()  # Pega o nome digitado no campo de entrada de nome
    email = entry_email.get()  # Pega o email digitado no campo de entrada de email
    telefone = entry_telefone.get()  # Pega o telefone digitado no campo de entrada de telefone

    # Verifica se todos os campos estão preenchidos
    if name and email and telefone:
        # Formata os dados em uma string para serem salvos no arquivo
        data = f"Nome: {name}, Email: {email}, Telefone: {telefone}\n"
        # Abre o arquivo clientes.txt em modo de escrita
        with open("C:/Users/Thiago-not/Documents/clientes.txt", "a") as arquivo:  # Substitua clientes.txt pela localização correta do seu arquivo .txt
            arquivo.write(data)  # Escreve os dados no arquivo
            messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")  # Exibe uma mensagem de sucesso ao salvar os dados
            clear_fields()  # Limpa os campos de entrada após salvar
    else:
        # Exibe uma mensagem de aviso caso algum campo esteja vazio
        messagebox.showwarning("Atenção", "Preencha todos os campos para salvar o cliente!")

# Função para limpar os campos de entrada de texto
def clear_fields():
    entry_name.delete(0, tk.END)  # Limpa o campo de entrada de nome
    entry_email.delete(0, tk.END)  # Limpa o campo de entrada de email
    entry_telefone.delete(0, tk.END)  # Limpa o campo de entrada de telefone

# Função para buscar um cliente no arquivo .txt
def buscar_cliente():
    buscar_nome = entry_busca.get().lower()  # Pega o nome a ser buscado e converte em minúsculas
    if not buscar_nome:
        messagebox.showwarning("Atenção", "Preencha o campo de busca para encontrar o cliente.")
        return
    try:
        # Tenta abrir o arquivo .txt para leitura
        with open("C:/Users/Thiago-not/Documents/clientes.txt", "r") as arquivo:
            found = False  # Variável para verificar se o cliente foi encontrado
            # Percorre cada linha do arquivo
            for line in arquivo.readlines():
                # Se o nome buscado estiver no arquivo, mostra a linha inteira
                if buscar_nome in line.lower():
                    messagebox.showinfo("Cliente encontrado!", f"Dados: {line}")
                    found = True
                    break
            if not found:
                messagebox.showinfo("Cliente não encontrado", "O cliente não foi encontrado no arquivo.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado. Por favor, verifique se o endereço do mesmo está correto.")

# Função para aplicar um visual moderno aos widgets (Botões, entradas de texto, etc.)
def apply_style():
    style = ttk.Style()
    style.theme_use('clam')  # Aplica o tema 'clam' para o estilo

    # Configuração para os botões (TButton), como fonte, cor de fundo e estilo
    style.configure('TButton', font=('Segoe UI', 12), foreground='white', background='#0078D7', relief="flat", padding=6)
    style.map('TButton', foreground=[('active', '#005A9E')])

    # Configuração para os rótulos (TLabel)
    style.configure('TLabel', font=('Segoe UI', 12), padding=5, background='#F3F3F3', foreground='#333')
    # Configurações para os campos de entrada de texto (TEntry)
    style.configure('TEntry', font=('Segoe UI', 12), padding=5, relief="solid", borderwidth=1)

    # Configuração para os fundos dos frames
    style.configure('TFrame', background='#F3F3F3')

# Criação da janela principal da aplicação
janela = tk.Tk()
janela.title("Gerenciador de Clientes")  # Título da janela
janela.geometry('440x460')  # Tamanho da janela (largura x altura)
janela.resizable(False, False)
janela.configure(bg='#F3F3F3')

# Aplica o estilo moderno aos widgets da interface
apply_style()

# Frame principal que centraliza os widgets na janela
frame_principal = tk.Frame(janela)
frame_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Campo de entrada e rótulos para o cadastro do cliente

# Campo de entrada para o nome do cliente
label_nome = tk.Label(frame_principal, text="Nome:")
label_nome.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
entry_name = ttk.Entry(frame_principal, width=30)
entry_name.grid(row=0, column=1, pady=10)

# Campo de entrada para o email do cliente
label_email = tk.Label(frame_principal, text="E-mail:")
label_email.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
entry_email = ttk.Entry(frame_principal, width=30)
entry_email.grid(row=1, column=1, pady=10)

# Campo de entrada para o telefone do cliente
label_telefone = tk.Label(frame_principal, text="Telefone:")
label_telefone.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
entry_telefone = ttk.Entry(frame_principal, width=30)
entry_telefone.grid(row=2, column=1, pady=10)

# Botão para salvar os dados do cliente
save_button = ttk.Button(frame_principal, text='Salvar', command=salvar_cliente)
save_button.grid(row=3, columnspan=2, pady=20, ipadx=10)

# Separador Visual entre a parte do cadastro e a parte da busca
separador = ttk.Separator(frame_principal, orient="horizontal")
separador.grid(row=4, column=0, columnspan=2, sticky="ew", pady=20)

# Campo de busca de cliente

# Rótulo e campo de entrada para buscar o cliente pelo nome
label_search = ttk.Label(frame_principal, text="Buscar cliente: ")
label_search.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)
entry_busca = ttk.Entry(frame_principal, width=30)
entry_busca.grid(row=5, column=1, pady=10)

# Botão para buscar o cliente
buscar_button = ttk.Button(frame_principal, text='Buscar', command=buscar_cliente)
buscar_button.grid(row=6, columnspan=2, pady=10, ipadx=10)

# Inicia a aplicação, mantendo a janela aberta
janela.mainloop()