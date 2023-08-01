from tkinter import *
import random

window = Tk()

global lista_locais
global lista_produto_posicao

lista_locais = []
lista_produto_posicao = [2, 2, 2, 2, 2, 2, 2, 2, 2]
vez = True



img_ctrl_play = PhotoImage(file=r"C:\Users\Note\Desktop\download.png")


# ------ Grupo da Linha 1
a1 = Button(window, text="   ", command= lambda : setar(a1), height=2, width=4)
a1.grid(row=1, column=0)

a2 = Button(window, text="   ", command= lambda : setar(a2), height=2, width=4)
a2.grid(row=1, column=1)

a3 = Button(window, text="   ", command= lambda : setar(a3), height=2, width=4)
a3.grid(row=1, column=2)

# ------ Grupo da Linha 2
b1 = Button(window, text="   ", command= lambda : setar(b1), height=2, width=4)
b1.grid(row=2, column=0)

b2 = Button(window, text="   ", command= lambda : setar(b2), height=2, width=4)
b2.grid(row=2, column=1)

b3 = Button(window, text="   ", command= lambda : setar(b3), height=2, width=4)
b3.grid(row=2, column=2)

# ------ Grupo da Linha 3
c1 = Button(window, text="   ", command= lambda : setar(c1), height=2, width=4)
c1.grid(row=3, column=0)

c2 = Button(window, text="   ", command= lambda : setar(c2), height=2, width=4)
c2.grid(row=3, column=1)

c3 = Button(window, text="   ", command= lambda : setar(c3), height=2, width=4)
c3.grid(row=3, column=2)

lbl_img = Label(window, image=img_ctrl_play)
lbl_img.grid(row=0, rowspan=1, columnspan=3)

lista_botoes = [a1, a2, a3, b1, b2, b3, c1, c2, c3]



### Funcoes ###

def setar(botao):
    botao.configure(text="X", state=DISABLED)
    lista_locais.append(botao)
    print(len(lista_locais))
    print(lista_locais)
    print(lista_produto_posicao)

    primeira_rodada(botao)


def primeira_rodada(botao):
    if len(lista_locais) == 1: #Primeira jogada
        if len(lista_locais) == 1 and lista_locais.count(b2) == 1: #Jogador selecionou o Centro
            posicao_aleatoria = random.choice([a1, a3, c1, c3])
            posicao_aleatoria.configure(text="O", state=DISABLED)
            lista_locais.append(botao)
        elif  len(lista_locais) == 1 and lista_locais.count(b2) == 0:
            botao = b2
            botao.configure(text="O", state=DISABLED)
            lista_locais.append(botao)
    else:
        analise_jogo()


def analise_jogo():
    for i in range(len(lista_botoes)):
        if lista_botoes[i].cget("text") == "X":
            lista_produto_posicao[i] = 3
        elif lista_botoes[i].cget("text") == "O":
            lista_produto_posicao[i] = 4
        else:
            lista_produto_posicao[i] = 2

    cabe_vitoria = vitoria()
    cabe_derrota = derrota()

    jogada_i_a(cabe_vitoria, cabe_derrota, lista_produto_posicao)


def vitoria():
    vitoria_caso = "sem_vitoria"
    if lista_produto_posicao[0] * lista_produto_posicao[1] * lista_produto_posicao[2] == 50:
        vitoria_caso = "caso1"
        return vitoria_caso
    elif lista_produto_posicao[3] * lista_produto_posicao[4] * lista_produto_posicao[5] == 50:
        vitoria_caso = "caso2"
        return vitoria_caso
    elif lista_produto_posicao[6] * lista_produto_posicao[7] * lista_produto_posicao[8] == 50:
        vitoria_caso = "caso3"
        return vitoria_caso
    elif lista_produto_posicao[0] * lista_produto_posicao[3] * lista_produto_posicao[6] == 50:
        vitoria_caso = "caso4"
        return vitoria_caso
    elif lista_produto_posicao[1] * lista_produto_posicao[4] * lista_produto_posicao[7] == 50:
        vitoria_caso = "caso5"
        return vitoria_caso
    elif lista_produto_posicao[2] * lista_produto_posicao[5] * lista_produto_posicao[8] == 50:
        vitoria_caso = "caso6"
        return vitoria_caso
    elif lista_produto_posicao[0] * lista_produto_posicao[4] * lista_produto_posicao[8] == 50:
        vitoria_caso = "caso7"
        return vitoria_caso
    elif lista_produto_posicao[2] * lista_produto_posicao[4] * lista_produto_posicao[6] == 50:
        vitoria_caso = "caso8"
        return vitoria_caso
    else:
        vitoria_caso = "sem_vitoria"
        return vitoria_caso

def derrota():
    derrota_caso = "sem_derrota"
    if lista_produto_posicao[0] * lista_produto_posicao[1] * lista_produto_posicao[2] == 18:
        derrota_caso = "caso1"
        return derrota_caso
    elif lista_produto_posicao[3] * lista_produto_posicao[4] * lista_produto_posicao[5] == 18:
        derrota_caso = "caso2"
        return derrota_caso
    elif lista_produto_posicao[6] * lista_produto_posicao[7] * lista_produto_posicao[8] == 18:
        derrota_caso = "caso3"
        return derrota_caso
    elif lista_produto_posicao[0] * lista_produto_posicao[3] * lista_produto_posicao[6] == 18:
        derrota_caso = "caso4"
        return derrota_caso
    elif lista_produto_posicao[1] * lista_produto_posicao[4] * lista_produto_posicao[7] == 18:
        derrota_caso = "caso5"
        return derrota_caso
    elif lista_produto_posicao[2] * lista_produto_posicao[5] * lista_produto_posicao[8] == 18:
        derrota_caso = "caso6"
        return derrota_caso
    elif lista_produto_posicao[0] * lista_produto_posicao[4] * lista_produto_posicao[8] == 18:
        derrota_caso = "caso7"
        return derrota_caso
    elif lista_produto_posicao[2] * lista_produto_posicao[4] * lista_produto_posicao[6] == 18:
        derrota_caso = "caso8"
        return derrota_caso
    else:
        derrota_caso = "sem_derrota"
        return derrota_caso



def jogada_i_a(win,loss, vet_vazios):
    #Caso nao tenha chance de vitoria ou derrota
    if win == "sem_vitoria" and loss == "sem_derrota":
        vet_escolha = []
        for i in vet_vazios:
            if lista_produto_posicao[i] == 2:
                vet_escolha.append(i)
        if len(vet_escolha) == 0:
            for i in range(len(lista_produto_posicao)):
                if lista_produto_posicao[i] == 2:
                    vet_escolha.append(i)
            escolha = random.choice(vet_escolha)
            lista_botoes[escolha].configure(text="O", state=DISABLED)
        else:
            escolha = random.choice(vet_escolha)
            lista_botoes[escolha].configure(text="O", state=DISABLED)


    #Ganhando
    elif win != "sem_vitoria":
        if win == "caso1":
            vet = [0, 1, 2]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso2":
            vet = [3, 4, 5]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso3":
            vet = [6, 7, 8]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso4":
            if lista_produto_posicao[0] * lista_produto_posicao[3] * lista_produto_posicao[6] == 50:
                vet = [0, 3, 6]
                for i in vet:
                    if lista_produto_posicao[i] == 2:
                        lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso5":
            vet = [1, 4, 7]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso6":
            vet = [2, 5, 8]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso7":
            vet = [0, 4, 8]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso8":
            vet = [2, 4, 6]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)

    #Evitando Derrota
    elif loss != "sem_derrota":
        if loss == "caso1":
            vet = [0, 1, 2]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif loss == "caso2":
            vet = [3, 4, 5]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif loss == "caso3":
            vet = [6, 7, 8]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif loss == "caso4":
            vet = [0, 3, 6]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif loss == "caso5":
            vet = [1, 4, 7]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif loss == "caso6":
            vet = [2, 5, 8]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif win == "caso7":
            vet = [0, 4, 8]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)
        elif loss == "caso8":
            vet = [2, 4, 6]
            for i in vet:
                if lista_produto_posicao[i] == 2:
                    lista_botoes[i].configure(text="O", state=DISABLED)



window.mainloop()




