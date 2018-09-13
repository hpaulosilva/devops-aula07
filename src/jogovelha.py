TAB = []
def inicializar() :
    TAB.append(['.','.','.'])
    TAB.append(['.','.','.'])
    TAB.append(['.','.','.'])
def jogar(jogador, linha, coluna):
    if jogador !='X' and jogador != 'O':
        verificaPosicao()
        raise RuntimeError('Jogador inválido!')
        valores = list(range(0,3))
    if linha not in valores:
        verificaPosicao()
        raise RuntimeError('Linha inválida!')
    if coluna not in valores:
        verificaPosicao()
        raise RuntimeError('Coluna inválida!')
        TAB[linha][coluna] = jogador
def tabuleiro():
    return TAB
def verificaPosicao():
    #codigo de verificar posicao
def main():
    inicializar()
    jogar('X', 1, 1)
    print(tabuleiro())
if __name__ == "__main__":
    main()
