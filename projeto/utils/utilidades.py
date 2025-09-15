import sys
import time
import os


def largura_terminal():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80 

def escrever(texto, atraso=0.05, centralizar=False, cor=""):
    reset = "\033[0m"
    largura = largura_terminal()
    if centralizar:
        inicio = (largura - len(texto)) // 2
        sys.stdout.write(" " * max(0, inicio))
    for letra in texto:
        sys.stdout.write(cor + letra + reset)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def mostrar_ascii_dinamico(titulo, atraso_linha=0.1):
    largura = largura_terminal()
    for linha in titulo.splitlines():
        inicio = (largura - len(linha)) // 2
        print(" " * max(0, inicio) + linha)
        time.sleep(atraso_linha)

def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')

def apaga_linha():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")