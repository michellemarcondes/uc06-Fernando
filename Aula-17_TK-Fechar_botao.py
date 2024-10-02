#Aula-17_TK-Fechar
#Programa que cria a opção de FECHAR  

from tkinter import ttk
from tkinter import Tk

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title('---Função Fechar---')
frm.grid()
ttk.Label(frm, text='Ola mundo ').grid(column=1, row=0)
ttk.Button(frm, text=' Fechar ', command=root.destroy).grid(column=1, row=1)
root.mainloop()