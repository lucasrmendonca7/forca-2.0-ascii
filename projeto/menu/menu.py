from utils.utilidades import *
from jogo.jogo import *
import time

def menu():
    opcoes = ["Jogo Rápido[1]", "Jogador vs Jogador[2]", "Sem Fim[3]", "Sair[4]"]

    for _ in range(8):
        apaga_linha()
    for i in range(len(opcoes) - 1):
        escrever(opcoes[i], atraso=0.025, centralizar=True, cor="\033[33m")
    
    escrever(opcoes[3], atraso=0.025, centralizar=True, cor="\033[31m")
    
    while True:
        escolha = input("Digite o número da opção: ")
        try:
            escolha = int(escolha)
            if 1 <= escolha <= 4:
                if escolha == 4:
                    print("\033[31mSaindo...\033[0m")
                    time.sleep(1.3)
                    break
                else:
                    print(f"\nExecutando modo {opcoes[escolha - 1][:-3]}...")
                    time.sleep(1.3)
                    if escolha == 1:
                        #modojr()
                        break
                    elif escolha == 2:
                        modo_jxj()
                    elif escolha == 3:
                        #modosf
                        break

            else:
                raise ValueError 
        except ValueError:
            print("\nEntrada inválida! Digite um número de 1 a 4.")
            input("Pressione ENTER para tentar novamente...")
            for _ in range(5):
                apaga_linha()


