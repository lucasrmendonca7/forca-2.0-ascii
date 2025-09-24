from utils.utilidades import *


def mostra_titulo():
    subtitulo = "MEU PROJETO - PROGRAMAÇÃO I"
    criador = "Desenvolvido por: Lucas Rodrigues Mendonça"
    instrucoes = ">>> Pressione ENTER para iniciar <<<"
    aviso = "(Fica melhor em tela cheia, aperte F11)"
    
    limpar_tela()
    print("\n" * 5)
    mostrar_ascii_dinamico(titulo_ascii(), atraso_linha=0.1)
    escrever(subtitulo, atraso=0.035, centralizar=True, cor=cor_texto1)
    escrever(criador, atraso=0.035, centralizar=True, cor=cor_texto1)
    escrever(instrucoes, atraso=0.025, centralizar=True, cor=cor_texto2)
    escrever(aviso, atraso=0.02, centralizar=True, cor="\033[38;5;240m")
    input()


def titulo_ascii():
    titulo = r"""                                           







     ███████████                                           ████████        █████   
    ▒▒███▒▒▒▒▒▒█                                          ███▒▒▒▒███     ███▒▒▒███ 
    ▒███   █ ▒   ██████  ████████   ██████   ██████     ▒▒▒    ▒███    ███   ▒▒███
    ▒███████    ███▒▒███▒▒███▒▒███ ███▒▒███ ▒▒▒▒▒███       ███████    ▒███    ▒███
    ▒███▒▒▒█   ▒███ ▒███ ▒███ ▒▒▒ ▒███ ▒▒▒   ███████      ███▒▒▒▒     ▒███    ▒███
    ▒███  ▒    ▒███ ▒███ ▒███     ▒███  ███ ███▒▒███     ███      █   ▒▒███   ███ 
    █████      ▒▒██████  █████    ▒▒██████ ▒▒████████   ▒██████████ ██ ▒▒▒█████▒  
    ▒▒▒▒▒        ▒▒▒▒▒▒  ▒▒▒▒▒      ▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒ ▒▒    ▒▒▒▒▒▒   
                                                                                
                                                                                






    
    """
    return titulo



cor_texto1 = "\033[96m"  # ciano
cor_texto2 = "\033[93m"  # amarelo

#if __name__ == "__main__":
    #mostra_titulo()