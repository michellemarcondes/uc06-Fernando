import tkinter as tk #Esta forma importa todas as opções de biblioteca do tkinter
janela = tk.Tk()
janela.title('SCM - (Sistema de Cotação de Moedas)')

msg0 = tk.Label(text='> Sistema de Busca de cotação de moedas <', fg='white', bg='#5858FA', width=50,height=10)
msg0.pack()

msg1 = tk.Label(text='selecione a moeda desejada: (D = Dólar, E= Euro, R= Reais)')
msg1.pack()

moeda = tk.Entry()
moeda.pack()

janela.mainloop()