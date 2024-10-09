# Importando o modulo Tkinter para criar a interface grafica (GUI)
import tkinter as tk

# Função que será chamada quando o usuario clicar em um botao da calculadora
def click(event):
    # Captura o texto do botão que foi clicado
    text = event.widget.cget("text")

    # Verifica se o botão que foi clicado foi o "=" (para calcular o resultado)
    if text == "=":
        try:
            # Avalia a expressão contida na tela (usando eval)
            result = eval(screen.get())
            screen.set(result)
        except:
            # Se houver um erro na avaliação da expressão, exibe "erro" na tela
            screen.set("erro")

    # Se o botão clicado foi "C", limpa a tela da calculadora
    elif text == "C":
        screen.set("")
    # Caso contrário (para qualquer outro botão), adiciona o texto do botão à expressão na tela
    else:
        screen.set(screen.get() + text)

# Configuração da janela principal da calculadora
window = tk.Tk()
window.title("Calculadora - PyCPhone")  # Define o titulo da janela
window.geometry("350x500")  # Define o tamanho da janela
window.config(bg='#F0F0F0')  # Define a cor do fundo da janela (cinza claro, padrão windows)

# Variável para armazenar o texto que será exibido na calculadora
screen = tk.StringVar()

# Caixa de entrada onde as expressões resultados serão exibidos
entry = tk.Entry(window, textvariable=screen, font="Arial 24", bd=10, insertwidth=2, width=14, justify="right")
# Configura a aparencia da caixa de entrada (Fonte, borda, alinhamento à direita)
entry.pack(fill="both", ipadx=8, padx=10, pady=20)  # Posiciona a caixa na interface

# Lista de botões da calculadora, organizados por linha
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ["C", "0", "=", '+']
]

# Função para criar os botões com o estilo especifico
def create_button(frame, text, color="#FFFFFF", bg="#C0C0C0"):
    # CRIA UM BOTÃO COM O TEXTO, COR DO TEXTO, COR DO FUNDO E ESTILO DESEJADO
    button = tk.Button(frame, text=text, font="Arial 20", padx=20, pady=20, bg=bg, fg=color, borderwidth=0)
    # Posiciona o botão no frame (linha) e ajusta o tamanho para preencher o espaço disponivel
    button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    # Associa a função click ao evento de clique no botão
    button.bind("<Button-1>", click)  # Corrected typo: "<Button-l>" -> "<Button-1>"
    return button

# Laço para criar e organizar os botões na interface
for row in buttons:
    # Cria um frame (linha) para organizar os botões da calculadora
    frame = tk.Frame(window, bg="#F0F0F0")  # Cor de fundo similar à calculadora do windows
    frame.pack(expand=True, fill="both")  # Ajusta o frame para preencher o espaço disponivel

    # Para cada botão na linha, cria o botão com as cores e comportamentos apropriados
    for button_text in row:
        if button_text in ['+', '-', '*', '/']:
            # Botões de operações tem cor laranja
            create_button(frame, button_text, color="#FFFFFF", bg="#FFA500")
        elif button_text == "C":
            # Botão de limpar tem cor vermelha
            create_button(frame, button_text, color="#FFFFFF", bg="#FF6347")
        else:
            # Botões de números tem cor padrão, cinza claro
            create_button(frame, button_text)

# Inicia o loop principal da interface grafica
window.mainloop()