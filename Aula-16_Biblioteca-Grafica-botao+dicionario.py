import tkinter as tk #Esta forma importa todas as opções de biblioteca do tkinter
janela = tk.Tk()
janela.title('SCM - (Sistema de Cotação de Moedas)')

msg0 = tk.Label(text='> Sistema de Busca de cotação de moedas <', fg='white', bg='#5858FA')
msg0.grid(row=1,column=0, columnspan=2,sticky='NSEW')

msg1 = tk.Label(text='Selecione a moeda desejada: ')
msg1.grid(row=1,column=0)

dicionario_cotacoes = {
    'Dolar': 4.99,
    'Euro' : 6.29,
    'Real' : 4.00
}

botao = tk.Button(text='Buscar Cotação')
botao.grid(row=2,column=1)

moeda = tk.Entry()
moeda.grid(row=1, column=1)

janela.mainloop()