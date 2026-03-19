import pygame 
import random
import sys

pygame.init()

LARGURA, ALTURA = 600, 400
TAMANHO_CELULA = 20
LARGURA_COLUNA = LARGURA // TAMANHO_CELULA
ALTURA_LINHA = ALTURA // TAMANHO_CELULA
FPD = 10 #quadros por segundo

#cores
PRETO = (0,0,0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

#configurações da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da eobrinha")
relogio = pygame.time.Clock()

#direção
cima = (0, -1)
baixo = (0, 1)
esqueda = (-1, 0)
direita = (1, 0)

def desenhar_celula(pos, cor):
    """Desenha um quadro na posição(Coluna, linha) com a cor especificada."""
    x = pos[0] * TAMANHO_CELULA
    y = pos[1] * TAMANHO_CELULA
    pygame.draw.rect(tela, cor, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))

def gerar_comida(cobra):
    """gerar uma nova posição aleatória para comida, que não seja ocupadda pela cobra"""
    while True:
        x = random.randint(0, LARGURA_COLUNA - 1)
        y = random.randint(0, ALTURA_LINHA - 1)
        if (x, y) not in cobra:
            return (x, y)
        
def mostrar_imagem(texto, cor, tamanho=50):
    """Exibe um texto centralizado na tela"""
    fonte = pygame.font.Font(None, tamanho)
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(LARGURA/2, ALTURA/2))
    tela.blit(superficie, retangulo)

def reiniciar_jogo():
    """Reinicia as variáveis do jogo"""
    global cobra, direção, comida, pontuação, game_over
    cobra = [(LARGURA_COLUNA // 2, ALTURA_LINHA // 2)]
    direcao = direita
    comida = gerar_comida(cobra)
    pontuacao = 0
    game_over = False

reiniciar_jogo()

