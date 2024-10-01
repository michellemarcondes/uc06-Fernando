import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def abrir():
    #Abre arquivo
    caminho = askopenfilename(
        filetypes=[("teste", "*.txt"), ("Salvar como...", "*.*")]
    )
    if not caminho:
        return
    txt_edit.delete("1.0", tk.END)
    with open(caminho, mode="r", encoding="utf-8") as entrada:
        text = entrada.read()
        txt_edit.insert(tk.END, text)
    window.title(f'----Editor de texto----{caminho}')

def salvar():
    #Salvar arquivo atual
    caminho = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[('Arquivo de texto', '*.txt'), ('Salvar', '*.*')],
    )
    if not caminho:
        return
    with open (caminho, mode='w', encoding='utf-8') as saida:
        text = txt_edit.get('1.0', tk.END)
        saida.write(text)
    window.title(f'-----Editor de Texto---- {caminho}')

window = tk.Tk()
window.title('-----Eitor de texto------')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text='Abrir', command=abrir)
btn_save = tk.Button(frm_buttons, text='Salvar', command=salvar)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()