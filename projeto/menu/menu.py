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

        opcoes = ["Jogo Rápido[1]", "Jogador vs Jogador[2]", "Sem Fim[3]", "Ajuda[4]", "Sair[5]"]

        for i in range(len(opcoes) - 2):
            escrever(opcoes[i], atraso=0.025, centralizar=True, cor="\033[33m")
        escrever(opcoes[3], atraso=0.025, centralizar=True, cor="\033[96m")
        escrever(opcoes[4], atraso=0.025, centralizar=True, cor="\033[31m")

        print("\n" * 2)

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
                ajuda()
            elif escolha == 5:
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

def ajuda():
    limpar_tela()
    print("\n" * 11)
    escrever("  AJUDA - COMO JOGAR", atraso=0.0, centralizar=True, cor="\033[95m")
    print()

    linhas_ajuda = [
        "Objetivo: adivinhar a palavra secreta.",
        "",
        "Controles:",
        "        - \033[96mDigite a letra que deseja tentar e pressione ENTER.\033[0m",
        "        - \033[96mPara chutar a palavra inteira, pressione ENTER sem digitar uma letra e então digite o seu chute.\033[0m",
        "        - \033[96mSe repetir a instrução acima, voltará ao modo de digitar apenas uma letra.\033[0m",
        "        - \033[96mDurante a tentativa de letra, digite 'sair' e pressione ENTER para voltar ao menu.\033[0m",
        "",
        "Modos:",
        "        - \033[35mJogo Rápido: escolha um tema e jogue uma partida única.\033[0m",
        "        - \033[35mJogador vs Jogador: players se alternam entre escolher a palavra e adivinhar.\033[0m",
        "        - \033[35mSem Fim: acumule pontos adivinhando o máximo de palavras até errar.\033[0m",
        "",
        "Dicas:",
        "        - \033[33mUse tela cheia (F11) para uma melhor experiência (caso contrário, o jogo ficará assimétrico).\033[0m",
        "        - \033[33mEvite acentos (ex: use 'maca' em vez de 'maçã').\033[0m",
        "        - \033[33mLetras já tentadas aparecem na tela para ajudar.\033[0m",
        "        - \033[33mDivirta-se!\033[0m"
    ]

    for linha in linhas_ajuda:
        escrever(linha, atraso=0.0, centralizar=True, reset_por_letra=False)
        time.sleep(0.03)

    print("\n" * 3)
    escrever("Pressione ENTER para voltar ao menu...", atraso=0.0, centralizar=True, cor="\033[1;37m")
    input() 
