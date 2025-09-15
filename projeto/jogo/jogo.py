from utils.utilidades import *
import os
import time
import random

# ----------------------- MENSAGENS -----------------------
def mensagem_vitoria(palavra):
    limpar_tela()
    print("\033[32mParabéns, você ganhou! A palavra era:\033[0m", palavra.upper())
    time.sleep(2.5)

def mensagem_derrota(palavra):
    limpar_tela()
    print("\033[31mFim de jogo! A palavra era:\033[0m", palavra.upper())
    time.sleep(2.5)

# ----------------------- UTILITÁRIOS -----------------------
def verifica_letras(palavra):
    return all(e in "abcdefghijklmnopqrstuvwxyz" for e in palavra)

# ----------------------- JOGO BASE -----------------------
def jogar_forca(palavra, tema=""):
    cor_ciano = "\033[36m"
    cor_amarela = "\033[33m"
    cor_reset = "\033[0m"

    oculto = ["_"] * len(palavra)
    letras_escolhidas = []
    vidas = 6
    primeiro_loop = True

    while True:
        limpar_tela()
        if tema != "":
            print("\033[34mTEMA:\033[0m", tema + "\n")
        print(" ".join(oculto))
        print(f"Você tem {vidas} vidas")
        print(cor_ciano + "Letras já tentadas: " + ", ".join(sorted(letras_escolhidas)).upper() + cor_reset)

        # Aviso inicial do chute 
        if primeiro_loop:
            print(cor_amarela + "Aperte ENTER para adivinhar a palavra completa" + cor_reset)
            time.sleep(2)
            apaga_linha()
            primeiro_loop = False

        tentativa = input("Digite sua tentativa: ").lower()

        # Chute da palavra completa
        if tentativa == "":
            apaga_linha()
            chute = input("Digite seu chute: ").lower()
            if chute == "":
                continue
            if chute == palavra:
                mensagem_vitoria(palavra)
                return True
            else:
                mensagem_derrota(palavra)
                return False

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
            print("\033[1;31mLetra errada!" + cor_reset)

        time.sleep(1.3)

        if "_" not in oculto:
            mensagem_vitoria(palavra)
            return True

        if vidas == 0:
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
    palavras = ["python", "computador", "programacao", "jogo", "terminal"]
    tema = random.choice(["TECNOLOGIA", "PALAVRAS ALEATORIAS"])
    palavra = random.choice(palavras)
    jogar_forca(palavra, tema)

def modo_sem_fim():
    palavras = ["python", "computador", "programacao", "jogo", "terminal"]
    tema = random.choice(["TECNOLOGIA", "PALAVRAS ALEATORIAS"])
    score = 0
    while True:
        palavra = random.choice(palavras)
        venceu = jogar_forca(palavra, tema)
        if venceu:
            score += 1
            print(f"\033[32mPontuação atual: {score}\033[0m")
            time.sleep(1.5)
        else:
            print(f"\033[31mFim do jogo! Sua pontuação final: {score}\033[0m")
            time.sleep(2.5)
            break