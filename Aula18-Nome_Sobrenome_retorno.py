#Retorna Campos: nome e sobrenome e mostra no terminal
import tkinter as tk

class Retorno(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.pack()

        self.nome_label = tk.Label(self, text='Nome: ')
        self.nome_label.grid(row=0, column=0)

        self.nome_entrada = tk.Entry(self)
        self.nome_entrada.grid(row=0, column=1)

        self.sobrenome_label = tk.Label(self, text='Sobrenome: ')
        self.sobrenome_label.grid(row=1, column=0)

        self.sobrenome_entrada = tk.Entry(self)
        self.sobrenome_entrada.grid(row=1, column=1)

        self.mostrar_button = tk.Button(self, text='Mostrar', command=self.mostrar_campos)
        self.mostrar_button.grid(row=2, column=0, columnspan=2)

    def mostrar_campos(self):
        nome = self.nome_entrada.get()
        sobrenome = self.sobrenome_entrada.get()
        print(f'Nome: {nome}, Sobrenome: {sobrenome}')

window = tk.Tk()
janela = Retorno(window)
janela.mainloop()