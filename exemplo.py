def verificar_vitoria(tabuleiro, jogador):  
    for i in range(3):   
        if tabuleiro[i].count(jogador) == 2 and tabuleiro[i].count('-') == 1:
            return i, tabuleiro[i].index('-')   
        coluna = [tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i]]
        if coluna.count(jogador) == 2 and coluna.count('-') == 1:
            return coluna.index('-'), i
    diagonal1 = [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]]
    if diagonal1.count(jogador) == 2 and diagonal1.count('-') == 1:
        return diagonal1.index('-'), diagonal1.index('-')
    diagonal2 = [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]]
    if diagonal2.count(jogador) == 2 and diagonal2.count('-') == 1:
        return diagonal2.index('-'), 2 - diagonal2.index('-')
    return None
def melhor_jogada(tabuleiro):
    # Primeiro, verifica se o jogador 'X' pode vencer
    jogada_vitoria = verificar_vitoria(tabuleiro, 'X')
    if jogada_vitoria:
        return jogada_vitoria
    jogada_bloqueio = verificar_vitoria(tabuleiro, 'O')
    if jogada_bloqueio:
        return jogada_bloqueio
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '-':
                return i, j
    return None
tabuleiro = []
print("Digite o tabuleiro de jogo da velha (X, O, -):")
for i in range(3):
    linha = input(f"Digite a linha {i + 1} (exemplo: X O -): ").split()
    tabuleiro.append(linha)
jogada = melhor_jogada(tabuleiro)
if jogada:
    print(f"A melhor jogada é na posição: linha {jogada[0] + 1}, coluna {jogada[1] + 1}")
else:
    print("Não há jogadas possíveis ou o jogo terminou empatado.")
