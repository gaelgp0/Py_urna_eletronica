from tkinter import *
from tkinter import ttk
import pymysql.cursors
from tkinter import messagebox

conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="urna_eletronica",
    cursorclass=pymysql.cursors.DictCursor
)
def CandidatosSelecionados(event):
    if (txt_numero.get() != '13') and (txt_numero.get() != '22') and (txt_numero.get() != '18') and (txt_numero.get() != '15' and (txt_numero.get() !='00')):
        x.set("Voto Nulo")
        label_nome = Label(framebranca, textvariable=x, font="Tohama 10",bg=cor3)
        label_nome.place(x=0, y=98)
    if txt_numero.get() == '13':
        x.set("Nome: Lula")
        label_nome = Label(framebranca, textvariable=x, font="Tohama 10",bg=cor3)
        label_nome.place(x=0, y=98)
    if txt_numero.get() == '22':
        x.set("Nome: Bolsonaro")
        label_nome = Label(framebranca, textvariable=x,font="Tohama 10", bg=cor3)
        label_nome.place(x=0, y=98)
    if txt_numero.get() == '18':
        x.set("Nome: Dilma")
        label_nome = Label(framebranca, textvariable=x,font="Tohama 10" ,bg=cor3)
        label_nome.place(x=0, y=98)
    if txt_numero.get() == '15':
        x.set("Nome: Temer")
        label_nome = Label(framebranca, textvariable=x,font="Tohama 10" ,bg=cor3)
        label_nome.place(x=0, y=98)
    
    if txt_numero.get() == '00':
        janela.destroy()
        teste = Tk()
        teste.geometry("402x230")
        teste.title("Resultado da eleição")
        label_candidato = Label(teste,text="N° do candidato")
        label_candidato.place(x=50,y=0)
        label_votos = Label(teste, text="Quantidade de votos")
        label_votos.place(x=220, y=0)

        sql_lula = 'SELECT COUNT(*) FROM lula'
        cursor_lula = conexao.cursor()
        cursor_lula.execute(sql_lula)
        lula = cursor_lula.fetchall()
        numero_votoslula = lula[0]['COUNT(*)']
        numero_lula = Label(teste, text="13")
        numero_lula.place(x=80,y=20)
        votos_lula = Label(teste,text=numero_votoslula)
        votos_lula.place(x=270,y=20)

        sql_bolsonaro = 'SELECT COUNT(*) FROM bolsonaro'
        cursor_bolsonaro = conexao.cursor()
        cursor_bolsonaro.execute(sql_bolsonaro)
        bolsonaro = cursor_bolsonaro.fetchall()
        numero_votosbolsonaro = bolsonaro[0]['COUNT(*)']
        numero_bolsonaro = Label(teste, text="22")
        numero_bolsonaro.place(x=80, y=40)
        votos_bolsonaro = Label(teste, text=numero_votosbolsonaro)
        votos_bolsonaro.place(x=270, y=40)

        sql_dilma = 'SELECT COUNT(*) FROM dilma'
        cursor_dilma = conexao.cursor()
        cursor_dilma.execute(sql_dilma)
        dilma = cursor_dilma.fetchall()
        numero_votosdilma = dilma[0]['COUNT(*)']
        numero_dilma = Label(teste, text="18")
        numero_dilma.place(x=80, y=60)
        votos_dilma = Label(teste, text=numero_votosdilma)
        votos_dilma.place(x=270, y=60)

        sql_temer = 'SELECT COUNT(*) FROM temer'
        cursor_temer = conexao.cursor()
        cursor_temer.execute(sql_temer)
        temer = cursor_temer.fetchall()
        numero_votostemer = temer[0]['COUNT(*)']
        numero_temer = Label(teste, text="15")
        numero_temer.place(x=80, y=80)
        votos_temer = Label(teste, text=numero_votostemer)
        votos_temer.place(x=270, y=80)

        sql_voto_branco = 'SELECT COUNT(*) FROM voto_branco'
        cursor_voto_branco = conexao.cursor()
        cursor_voto_branco.execute(sql_voto_branco)
        voto_branco = cursor_voto_branco.fetchall()
        numero_votos_brancos = voto_branco[0]['COUNT(*)']
        numero_voto_branco = Label(teste, text="Voto Branco")
        numero_voto_branco.place(x=60, y=100)
        votos_voto_branco = Label(teste, text=numero_votos_brancos)
        votos_voto_branco.place(x=270, y=100)

        sql_nulo = 'SELECT COUNT(*) FROM nulo'
        cursor_nulo = conexao.cursor()
        cursor_nulo.execute(sql_nulo)
        voto_nulo = cursor_nulo.fetchall()
        numero_votosnulo = voto_nulo[0]['COUNT(*)']
        numero_nulo = Label(teste, text="Voto Nulo")
        numero_nulo.place(x=64, y=120)
        votos_nulo = Label(teste, text=numero_votosnulo)
        votos_nulo.place(x=270, y=120)

        teste.mainloop()


def entrar_valores(numero):
    txt_numero.config(state=NORMAL)
    entrarvalor = txt_numero.get()
    txt_numero.delete(0, END)
    txt_numero.insert(0, str(entrarvalor) + str(numero))
    txt_numero.config(state=DISABLED)

def corrigir():
    txt_numero.config(state=NORMAL)
    txt_numero.delete(0,END)
    txt_numero.config(state=DISABLED)
    return

def BotaoBranco():
    txt_numero.config(state=NORMAL)
    txt_numero.delete(0, END)
    txt_numero.config(state=DISABLED)
    voto = "."
    sql = "INSERT INTO voto_branco (voto)" \
           "VALUES (%s)"
    cursor = conexao.cursor()
    cursor.execute(sql, (voto))
    conexao.commit()
    messagebox.showinfo("Botão Branco", "Voto Branco Realizado com Sucesso")

def Confirmar():
    if (txt_numero.get() != '13') and (txt_numero.get() != '22') and (txt_numero.get() != '18') and (txt_numero.get() != '15') and (txt_numero.get() !='00'):
        voto = "."
        sql = "INSERT INTO nulo (voto)" \
              "values (%s)"
        cursor = conexao.cursor()
        cursor.execute(sql, (voto))
        conexao.commit()
        messagebox.showinfo("Voto Nulo", "Voto Nulo inserido com sucesso")

    if txt_numero.get() == '13':
        voto = "."
        sql = "INSERT INTO lula (voto)" \
              "values (%s)"
        cursor = conexao.cursor()
        cursor.execute(sql, (voto))
        conexao.commit()
        messagebox.showinfo("Voto Lula", "Voto no Candidato Lula inserido com sucesso")

    if txt_numero.get() == '22':
        voto = "."
        sql = "INSERT INTO bolsonaro (voto)" \
              "values (%s)"
        cursor = conexao.cursor()
        cursor.execute(sql, (voto))
        conexao.commit()
        messagebox.showinfo("Voto Bolsonaro", "Voto no Candidato Bolsonaro inserido com sucesso")

    if txt_numero.get() == '15':
        voto = "."
        sql = "INSERT INTO temer (voto)" \
              "values (%s)"
        cursor = conexao.cursor()
        cursor.execute(sql, (voto))
        conexao.commit()
        messagebox.showinfo("Voto Temer", "Voto no Candidato Temer inserido com sucesso")

    if txt_numero.get() == '18':
        voto = "."
        sql = "INSERT INTO dilma (voto)" \
              "values (%s)"
        cursor = conexao.cursor()
        cursor.execute(sql, (voto))
        conexao.commit()
        messagebox.showinfo("Voto Dilma", "Voto na Candidata Dilma inserido com sucesso")

cor1 = "#242424"
cor3 = 'white'
cor2 = "#000000"
corcinza = "#808080"

janela = Tk()
janela.title("Urna Eletrônica")
janela.config(background=corcinza)
janela.geometry("690x450")

x = StringVar()

# Frame 1
framepreto = Frame(janela, bg="black", width=450, height=150)
framepreto.pack()

# Frame 2
framebranca = Frame(framepreto, bg=cor3, width=400, height=150)
framebranca.pack(pady=20, padx=20)

label_titulo = Label(framebranca, text="Seu voto para: ", bg=cor3)
label_titulo.place(x=0, y=0)

label_presidente = Label(framebranca, text="Presidente", bg=cor3, font="12")
label_presidente.place(x=140, y=20)

label_numero = Label(framebranca, text="Número", bg=cor3)
label_numero.place(x=0, y=70)

vars = StringVar()
vars.trace('w', lambda name, index, mode, var=vars: CandidatosSelecionados(var))
txt_numero = Entry(framebranca,textvariable=vars, font="10",state=DISABLED,bg='white')
txt_numero.place(x=50, y=70)

# Botão 1
botao1 = Button(janela, text='1', command=lambda: entrar_valores(1), width=11, height=2, bg=cor1, foreground='white')
botao1.place(x=150, y=210)

# Botão 2
botao2 = Button(janela, text='2', command=lambda: entrar_valores(2), width=11, height=2, bg=cor1, foreground='white')
botao2.place(x=250, y=210)

# Botão 3
botao3 = Button(janela, text='3', command=lambda: entrar_valores(3), width=11, height=2, bg=cor1, foreground='white')
botao3.place(x=350, y=210)

# Botão 4
botao4 = Button(janela, text='4', command=lambda: entrar_valores(4), width=11, height=2, bg=cor1, foreground='white')
botao4.place(x=150, y=262)

# Botão 5
botao5 = Button(janela, text='5', command=lambda: entrar_valores(5), width=11, height=2, bg=cor1, foreground='white')
botao5.place(x=250, y=262)

# Botão 6
botao6 = Button(janela, text='6', command=lambda: entrar_valores(6), width=11, height=2, bg=cor1, foreground='white')
botao6.place(x=350, y=262)

# Botão 7
botao7 = Button(janela, text='7', command=lambda: entrar_valores(7), width=11, height=2, bg=cor1, foreground='white')
botao7.place(x=150, y=314)

# Botão 8
botao8 = Button(janela, text='8', command=lambda: entrar_valores(8), width=11, height=2, bg=cor1, foreground='white')
botao8.place(x=250, y=314)

# Botão 9
botao9 = Button(janela, text='9', command=lambda: entrar_valores(9), width=11, height=2, bg=cor1, foreground='white')
botao9.place(x=350, y=314)

# Botão 0
botao0 = Button(janela, text='0', command=lambda: entrar_valores(0), width=11, height=2, bg=cor1, foreground='white')
botao0.place(x=250, y=366)

# Botão branco
botaobranco = Button(janela, text='BRANCO', width=11, height=2, bg="white", foreground='black',command=BotaoBranco)
botaobranco.place(x=450, y=210)

botaovermelho = Button(janela, text='CORRIGE', width=11, height=2, bg="RED", foreground='black',command=corrigir)
botaovermelho.place(x=450, y=262)

botaoverde = Button(janela, text='CONFIRMA', width=11, height=2, bg="green", foreground='black',command=Confirmar)
botaoverde.place(x=450, y=314)

janela.mainloop()
