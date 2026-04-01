import random 
def gerar_numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)
def obter_palpite_do_jogador(inicio, fim):
    return int(input(f"Digite seu palpite: (entre {inicio} e {fim}): "))