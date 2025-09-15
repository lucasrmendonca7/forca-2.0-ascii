from utils.utilidades import *
from jogo.jogo import *
from titulo.titulo import titulo_ascii
import time
import sys

def menu():
    while True:
        limpar_tela()
        print("\n" * 5)
        mostrar_ascii_dinamico(titulo_ascii(), atraso_linha=0.0)

        opcoes = ["Jogo Rápido[1]", "Jogador vs Jogador[2]", "Sem Fim[3]", "Sair[4]"]

        for i in range(len(opcoes) - 1):
            escrever(opcoes[i], atraso=0.025, centralizar=True, cor="\033[33m")
        escrever(opcoes[3], atraso=0.025, centralizar=True, cor="\033[31m")

        escolha = input("Digite o número da opção: ")
        try:
            escolha = int(escolha)
            if escolha == 1:
                jogo_rapido()
            elif escolha == 2:
                modo_jxj()
            elif escolha == 3:
                modo_sem_fim()
            elif escolha == 4:
                print("\033[31mSaindo...\033[0m")
                time.sleep(1.3)
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("\nEntrada inválida! Digite um número de 1 a 4.")
            input("Pressione ENTER para tentar novamente...")
            for _ in range(5):
                apaga_linha()
