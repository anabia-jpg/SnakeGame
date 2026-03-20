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
esquerda = (-1, 0)
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
    global cobra, direcao, comida, pontuacao, game_over
    cobra = [(LARGURA_COLUNA // 2, ALTURA_LINHA // 2)]
    direcao = direita
    comida = gerar_comida(cobra)
    pontuacao = 0
    game_over = False

reiniciar_jogo()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if game_over:
                reiniciar_jogo()
            else:
                # Controles
                if evento.key in (pygame.K_UP, pygame.K_w) and direcao != baixo:
                    direcao = cima
                elif evento.key in (pygame.K_DOWN, pygame.K_s) and direcao != cima:
                    direcao = baixo
                elif evento.key in (pygame.K_LEFT, pygame.K_a) and direcao != direita:
                    direcao = esquerda
                elif evento.key in (pygame.K_RIGHT, pygame.K_d) and direcao != esquerda:
                    direcao = direita

    if not game_over:
        cabeca = cobra[0]
        nova_cabeca = (cabeca[0] + direcao[0], cabeca[1] + direcao[1])

        if (nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA_COLUNA or
            nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA_LINHA):
            game_over = True

        elif nova_cabeca in cobra:
            game_over = True
        else:
 
            cobra.insert(0, nova_cabeca)

 
            if nova_cabeca == comida:
                pontuacao += 1
                comida = gerar_comida(cobra)
            else:

                cobra.pop()


        tela.fill(PRETO)

        # Desenha a comida
        desenhar_celula(comida, VERMELHO)

        # Desenha a cobra
        for segmento in cobra:
            desenhar_celula(segmento, VERDE)

        # Mostra pontuação
        fonte = pygame.font.Font(None, 30)
        texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))
    else:
        # Tela de game over
        tela.fill(PRETO)
        mostrar_imagem("GAME OVER", VERMELHO, 60)
        mostrar_imagem(f"Pontuação: {pontuacao}", BRANCO, 30)
        mostrar_imagem("Pressione qualquer tecla para jogar novamente", AZUL, 25)
        # O texto "Pressione qualquer tecla..." fica um pouco mais abaixo
        # Ajuste manual da posição:
        fonte_peq = pygame.font.Font(None, 25)
        texto_reiniciar = fonte_peq.render("Pressione qualquer tecla para jogar novamente", True, AZUL)
        ret_reiniciar = texto_reiniciar.get_rect(center=(LARGURA/2, ALTURA/2 + 50))
        tela.blit(texto_reiniciar, ret_reiniciar)

    # Atualiza a tela
    pygame.display.flip()
    # Controla a velocidade do jogo
    relogio.tick(FPS)