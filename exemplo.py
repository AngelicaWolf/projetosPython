def check_victory(board, player):  
    for i in range(3):   
        if board[i].count(player) == 2 and board[i].count('-') == 1:
            return i, board[i].index('-')   
        column = [board[0][i], board[1][i], board[2][i]]
        if column.count(player) == 2 and column.count('-') == 1:
            return column.index('-'), i
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    if diagonal1.count(player) == 2 and diagonal1.count('-') == 1:
        return diagonal1.index('-'), diagonal1.index('-')
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if diagonal2.count(player) == 2 and diagonal2.count('-') == 1:
        return diagonal2.index('-'), 2 - diagonal2.index('-')
    return None
def best_move(board):

    winning_move = vcheck_victory(board, 'X')
    if winning_move:
        return winning_move
    block_play = check_victory(board, 'O')
    if block_play:
        return block_play
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return i, j
    return None
board = []
print("Digite o tabuleiro de jogo da velha (X, O, -):")
for i in range(3):
    line = input(f"Digite a linha {i + 1} (exemplo: X O -): ").split()
    board.append(line)
play = best_move(board)
if play:
    print(f"A melhor jogada é na posição: linha {play[0] + 1}, coluna {play[1] + 1}")
else:
    print("Não há jogadas possíveis ou o jogo terminou empatado.")
