# APP DE CADASTRO
from tkinter import *

# ---------------- CONSTANTES ---------------- #
FONTE_CABECALHO = ('Fixedsys', 28, 'normal')
FONTE_TEXTO = ('Fixedsys', 16, 'normal')

AZUL = "#21174A"
AMARELO = "#FAFF00"


# ---------------- FUNÇÕES ---------------- #
def confirmar_pressionado():
    ler_dados_inseridos()
    resetar_campos()

import json
def ler_dados_inseridos():
    _nome      = campo_nome.get()
    _sobrenome = campo_sobrenome.get()
    nome_completo = f"{_nome} {_sobrenome}"

    email = campo_email.get()
    linguagens_lidas = campo_linguagens.get()
    linguagens  = linguagens_lidas.split(',')
    experiencia = campo_exp.get()

    modelo = {
        "nome"  : nome_completo,
        "email" : email,
        "linguagens"  : linguagens,
        "experiencia" : experiencia
    }
    print(json.dumps(modelo, indent=4))

def resetar_campos():
    global check_s, check_j, check_p, check_full, check_front, check_back

    campo_nome.delete(0, END)
    campo_sobrenome.delete(0, END)
    campo_email.delete(0, END)
    campo_linguagens.delete(0, END)
    campo_exp.delete(0, END)

    check_j = 0
    check_p = 0
    check_s = 0

    check_front = 0
    check_back = 0
    check_full = 0


def cancelar_pressionado():
    global root
    root.destroy()


# --------------------------- UI SETUP --------------------------- #

root = Tk()
root.minsize(450, 500)
root.config(bg=AZUL, padx=50, pady=10)
root.resizable(False, False)
root.title("CADASTRO DE DEVS")

# ---------------- LABELS ---------------- #

titulo = Label(text="CADASTRO DE DEVs", font=FONTE_CABECALHO, bg=AZUL, fg=AMARELO)
titulo.grid(row=0, column=0, columnspan=4, pady=20)

nome = Label(text="NOME:", font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
nome.grid(row=1, column=0, pady=10, padx=10)

sobrenome = Label(text="SOBRENOME:", font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
sobrenome.grid(row=1, column=2, pady=10, padx=10)

email = Label(text="EMAIL:", font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
email.grid(row=2, column=0, pady=10, padx=10)

# ---------------- ENTRADAS ---------------- #

campo_nome = Entry(bg=AMARELO, font=FONTE_TEXTO, fg=AZUL)
campo_nome.grid(row=1, column=1, pady=10, padx=10)

campo_sobrenome = Entry(bg=AMARELO, font=FONTE_TEXTO, fg=AZUL)
campo_sobrenome.grid(row=1, column=3, pady=10, padx=10)

campo_email = Entry(bg=AMARELO, font=FONTE_TEXTO, fg=AZUL)
campo_email.grid(row=2, column=1, columnspan=3, pady=10, padx=10, sticky=N+S+W+E)

# ----------------  ESPECIALIDADE ---------------- #

especialidade = Label(text="ESPECIALIDADE:", font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
especialidade.grid(row=3, column=0, pady=10, padx=10)

check_front = IntVar()
check_back = IntVar()
check_full = IntVar()

botao_frontend = Checkbutton(
    text="FRONT-END",
    font=FONTE_TEXTO,
    fg=AZUL,
    bg=AMARELO,
    variable=check_front,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
)
botao_frontend.grid(row=3, column=1, pady=10, padx=10)

botao_backend = Checkbutton(
    text="BACK-END",
    font=FONTE_TEXTO,
    fg=AZUL,
    bg=AMARELO,
    variable=check_back,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
)
botao_backend.grid(row=3, column=2, pady=10, padx=10)

botao_full = Checkbutton(
    text="FULLSTACK",
    font=FONTE_TEXTO,
    fg=AZUL,
    bg=AMARELO,
    variable=check_full,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
)
botao_full.grid(row=3, column=3, pady=10, padx=10)


# ---------------- CHECKBUTTONS SENIORIDADE ---------------- #
senioridade = Label(text="SENIORIDADE:", font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
senioridade.grid(row=4, column=0, pady=10, padx=10)

check_j = IntVar()
check_p = IntVar()
check_s = IntVar()

junior_check = Checkbutton(
    text="JÚNIOR",
    font=FONTE_TEXTO,
    fg=AZUL,
    bg=AMARELO,
    variable=check_j,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
)
junior_check.grid(row=4, column=1, pady=10, padx=10)

pleno_check = Checkbutton(
    text="PLENO",
    font=FONTE_TEXTO,
    fg=AZUL,
    bg=AMARELO,
    variable=check_p,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
)
pleno_check.grid(row=4, column=2, pady=10, padx=10)

senior_check = Checkbutton(
    text="SÊNIOR",
    font=FONTE_TEXTO,
    fg=AZUL,
    bg=AMARELO,
    variable=check_s,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
)
senior_check.grid(row=4, column=3, pady=10, padx=10)

# ---------------- LINGUAGENS ---------------- #
linguagens_texto = Label(text='LINGUAGENS QUE DOMINA:', font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
linguagens_texto.grid(row=5, column=0, pady=10, padx=10)

campo_linguagens = Entry(font=FONTE_TEXTO, bg=AMARELO, fg=AZUL)
campo_linguagens.grid(row=5, column=1, pady=10, padx=10, columnspan=3, sticky=N+S+W+E)

# ---------------- EXPERIÊNCIAS ---------------- #
exp_texto = Label(text='EXPERIÊNCIAS EXTRAS:', font=FONTE_TEXTO, bg=AZUL, fg=AMARELO)
exp_texto.grid(row=6, column=0, pady=10, padx=10)

campo_exp = Entry(font=FONTE_TEXTO, bg=AMARELO, fg=AZUL)
campo_exp.grid(row=6, column=1, pady=10, padx=10, columnspan=3, sticky=N+S+W+E)

# ---------------- BOTÃO DE CONFIRMAR ---------------- #
confirmar = Button(text='CONFIRMAR', font=FONTE_TEXTO, bg=AMARELO, fg=AZUL, command=confirmar_pressionado)
confirmar.grid(row=7, column=1, pady=10, padx=10)

cancelar = Button(text='CANCELAR', font=FONTE_TEXTO, bg=AMARELO, fg=AZUL, command=cancelar_pressionado)
cancelar.grid(row=7, column=2, pady=10, padx=10)

root.mainloop()
