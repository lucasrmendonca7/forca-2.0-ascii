from utils.utilidades import *
import os
import time

def mensagem_vitoria(palavra):
    limpar_tela()
    print("\033[32mParabéns, você ganhou! A palavra era:\033[0m", palavra.upper())

def mensagem_derrota(palavra):
    limpar_tela()
    print("\033[31mFim de jogo! A palavra era:\033[0m", palavra.upper())

def verifica_letras(palavra):
    verificador = all(e in "abcdefghijklmnopqrstuvwxyz" for e in palavra)
    return verificador

def modo_jxj():
    cor_ciano = "\033[36m"
    cor_amarela = "\033[33m"
    cor_verde = "\033[32m"
    cor_vermelho = "\033[31m"
    cor_reset = "\033[0m"

    while True:
        limpar_tela()
        palavra = input("Digite a palavra a ser adivinhada: ").lower()
        if len(palavra) <= 1 or not verifica_letras(palavra):
            print(cor_amarela + "Digite uma palavra válida!" + cor_reset)
            time.sleep(1)
            continue
        else:
            break

    tema = input("Digite o tema: ").upper()
    oculto = ["_"] * len(palavra)
    letras_escolhidas = []
    vidas = 6
    primeiro_loop = True
    
    while True:
        limpar_tela()
        if tema != "":
            print("\033[34mTEMA:" + cor_reset)
        print("\033[34m" + tema + cor_reset+ "\n")
        print(" ".join(oculto))
        print(f"Você tem {vidas} vidas")
        print(cor_ciano + "Letras já tentadas: " + ", ".join(sorted(letras_escolhidas)).upper() + cor_reset)
        
        if primeiro_loop:
            print(cor_amarela + "Aperte ENTER para adivinhar a palavra completa" + cor_reset)
            time.sleep(2)
            apaga_linha()
            primeiro_loop = False

        tentativa = input("Digite sua tentativa: ").lower()
        
        if tentativa == "":
            apaga_linha()
            chute = input("Digite seu chute: ").lower()

            if chute == "":
                continue
            if chute == palavra:
                mensagem_vitoria(palavra)
                break
            else:
                mensagem_derrota(palavra)
                break
        
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
            limpar_tela()
            mensagem_vitoria(palavra)
            break

        if vidas == 0:
            limpar_tela()
            mensagem_derrota(palavra)
            break
