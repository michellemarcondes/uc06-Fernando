#Programa que cria a opção de FECHAR

from tkinter import ttk
from tkinter import Tk

window = Tk()
frm = ttk.Frame(window, padding=50)
window.title('Aula 18')
frm.grid()
ttk.Label(frm, text='Olá mundo ->').grid(column=0, row=0)
ttk.Button(frm, text='Fechar', command=window.destroy).grid(column=1, row=0)
window.mainloop()