# Arquitetura

O gerenciamento das casas ficara no arquivo jogovelha.py

Cada casa podera ter tres estados sendo:

casa vazia = "."
casa ocupada player1 = "X"
casa ocupada player2 = "O"

existira uma funcao que vai inicializar o jogo criando uma lista 3x3 onde cada casa sera por default vazia.

outra necessidade e a criacao da funcao jogar que recebera por parametros qual o player, a linha e a coluna. Esta funcao ira 
posicionar na casa selecionada o jogador que requisitou essa funcao.
