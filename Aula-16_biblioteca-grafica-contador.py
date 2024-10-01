import tkinter as tk #Esta forma importa todas as opções de biblioteca do tkinter
janela = tk.Tk()

def diminuir():
    valor = int(lbl_valor["text"])
    lbl_valor["text"] = f"{valor-1}"

def aumentar():
    valor = int(lbl_valor["text"])
    lbl_valor["text"] = f"{valor+1}"

janela.title('Contador')
janela.rowconfigure(0, minsize=50, weight=1)
janela.columnconfigure([0, 1, 2], minsize=50, weight=1)
#btn == Button
btn_diminuir = tk.Button(master=janela, text="-", command=diminuir)
btn_diminuir.grid(row=0, column=0, sticky="nsew")
#lbl = Label
lbl_valor = tk.Label(master=janela, text="0")
lbl_valor.grid(row=0,column=1)

btn_aumentar = tk.Button(master=janela, text="+", command=aumentar)
btn_aumentar.grid(row=0, column=2, sticky="nsew")

janela.mainloop()