from titulo.titulo import titulo_ascii
from utils.utilidades import *
from utils.bancodepalavras import banco_palavras
import os
import time
import random
import curses


# ----------------------- MENSAGENS -----------------------
def mensagem_vitoria(palavra):
    limpar_tela()
    mostrar_ascii_dinamico(tela_youwin(), atraso_linha=0.1)
    time.sleep(2)
    print("\n" * 2)
    escrever(f"Parabéns, você ganhou! A palavra era: {palavra.upper()}", atraso=0.025, centralizar=True, cor="\033[32m")
    time.sleep(3)


def mensagem_derrota(palavra):
    limpar_tela()
    mostrar_ascii_dinamico(tela_gameover(), atraso_linha=0.1)
    time.sleep(2)
    print("\n" * 2)
    for linha in frames_forca(-1).split("\n"):
        escrever(linha, centralizar=True, atraso=0.020, cor="\033[31m")
    print()
    escrever(f"Fim de jogo! A palavra era: {palavra.upper()}", atraso=0.025, centralizar=True, cor="\033[31m")
    time.sleep(4)


# ----------------------- UTILITÁRIOS -----------------------

def verifica_letras(palavra):
    return all(e in "abcdefghijklmnopqrstuvwxyz" for e in palavra)

# ----------------------- JOGO BASE -----------------------
def jogar_forca(palavra, tema="", score=None):
    cor_ciano = "\033[36m"
    cor_amarela = "\033[33m"
    cor_reset = "\033[0m"

    oculto = ["_"] * len(palavra)
    letras_escolhidas = []
    vidas = 6
    cont_frame = 0
    primeiro_loop = True

    while True:
        limpar_tela()
        print("\n" * 8)
        
        if score is not None:
            escrever(f"Pontuação: {score}", atraso=0.0, centralizar=True, cor=cor_amarela)
            print()
        if tema != "":
            escrever(f"TEMA: {tema}", atraso=0.0, centralizar=True, cor="\033[34m")
            print()
        
        for linha in frames_forca(cont_frame).split("\n"):
            escrever(linha, centralizar=True, atraso=0.0)

        print("\n" * 4)
        
        escrever(" ".join(oculto), atraso=0.0, centralizar=True)
        print("\n" * 2)
        escrever(f"Você tem {vidas} vidas", atraso=0.0, centralizar=True)
        escrever(f"Letras já tentadas: {', '.join(sorted(letras_escolhidas)).upper()}", atraso=0.0, centralizar=True, cor=cor_ciano)

        if primeiro_loop:
            escrever("Aperte ENTER para adivinhar a palavra completa",
                     atraso=0.0, centralizar=True, cor=cor_amarela)
            time.sleep(2)
            apaga_linha()
            primeiro_loop = False
        
        print("\n" * 4)

        tentativa = input("Digite sua tentativa: ").lower()

        if tentativa == "":
            apaga_linha()
            chute = input("Digite seu chute: ").lower()
            if chute == "":
                continue
            if chute == palavra:
                mensagem_vitoria(palavra)
                return True
            else:
                limpar_tela()
                time.sleep(1.5)
                mensagem_derrota(palavra)
                return False

        if tentativa == "sair":
            return

        if len(tentativa) != 1 or not verifica_letras(tentativa):
            print(cor_amarela + "Digite apenas UMA letra válida!" + cor_reset)
            time.sleep(1.3)
            continue

        if tentativa in letras_escolhidas:
            print(cor_amarela + "Você já tentou essa letra" + cor_reset)
            time.sleep(1.3)
            continue

        letras_escolhidas.append(tentativa)

        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    oculto[i] = letra.upper()
            print("\033[1;32mLetra correta!" + cor_reset)
        else:
            vidas -= 1
            cont_frame += 1
            print("\033[1;31mLetra errada!" + cor_reset)

        time.sleep(1.3)

        if "_" not in oculto:
            time.sleep(2)
            limpar_tela()
            mensagem_vitoria(palavra)
            return True

        if vidas == 0:
            time.sleep(2)
            limpar_tela()
            mensagem_derrota(palavra)
            return False

        


# ----------------------- MODOS -----------------------
def modo_jxj():
    while True:
        limpar_tela()
        palavra = input("Digite a palavra a ser adivinhada: ").lower()
        if len(palavra) <= 1 or not verifica_letras(palavra):
            print("\033[33mDigite uma palavra válida!\033[0m")
            time.sleep(1)
            continue
        else:
            break

    tema = input("Digite o tema: ").upper()
    jogar_forca(palavra, tema)

def jogo_rapido():
    while True:
        limpar_tela()
        print("\n" * 5)
        mostrar_ascii_dinamico(titulo_ascii(), atraso_linha=0.0)

        escrever("Escolha um tema", atraso=0.025, centralizar=True, cor="\033[35m")

        opcoes = ["Geral      [1]", "Animais    [2]", "Frutas     [3]", "Países     [4]", "Objetos    [5]", "Profissões [6]", "Voltar     [7]"]

        for i in range(len(opcoes) - 1):
            escrever(opcoes[i], atraso=0.025, centralizar=True, cor="\033[34m")
        escrever(opcoes[6], atraso=0.025, centralizar=True, cor="\033[31m")

        escolha = input("Digite o número da opção: ")
        try:
            escolha = int(escolha)
            if escolha == 1:
                tema = "geral"
            elif escolha == 2:
                tema = "animais"
            elif escolha == 3:
                tema = "frutas"
            elif escolha == 4:
                tema = "paises"
            elif escolha == 5:
                tema = "objetos"
            elif escolha == 6:
                tema = "profissoes"
            elif escolha == 7:
                return
            else:
                raise ValueError
            break
        except ValueError:
            print("\nEntrada inválida! Digite um número de 1 a 6.")
            input("Pressione ENTER para tentar novamente...")
            for _ in range(5):
                apaga_linha()
            
    palavra = random.choice(banco_palavras[tema])
    jogar_forca(palavra, tema.upper())

def modo_sem_fim():
    score = 0
    while True:
        tema = random.choice(list(banco_palavras.keys()))
        palavras = random.choice(banco_palavras[tema])
        venceu = jogar_forca(palavras, tema.upper(), score)
        if venceu:
            score += 1
            escrever(f"Pontuação atual: {score}", atraso=0.025, centralizar=True, cor="\033[32m")
            time.sleep(1.5)
        else:
            escrever(f"Pontuação final: {score}", atraso=0.025, centralizar=True, cor="\033[31m")
            time.sleep(3)
            break