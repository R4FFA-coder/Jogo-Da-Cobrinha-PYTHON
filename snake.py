from random import randint
import pygame
from sys import exit
from pygame.locals import *

pygame.init()
fps = 15

altura = 600
largura = 800

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)
x_maca = randint(10,750)
y_maca = randint(5, 590)
score = 0
velocidade = 8
x_controle = velocidade
y_controle = 0

bgm = pygame.mixer_music.load('../PraticapyGame/asset/Samba.wav')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.5)
coin = pygame.mixer.Sound('../PraticapyGame/asset/Score.wav')

fonte = pygame.sysfont.SysFont("arial", 30, True,True)  # Primeiro para criar texto, precisamos configurar uma fonte, depois criar uma mensagem em str, renderizar o texto e janela.blit para adicionar na janela
janela = pygame.display.set_mode(size=(largura, altura))
pygame.display.set_caption("Jogo 0.1")
relogio = pygame.time.Clock()
lista_corpo = []
comprimento_inicial= 2


def cresce_cobra(lista_corpo):
    for XeY in lista_corpo:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(janela, (0,255,0), (XeY[0], XeY[1], 23, 30))

while True:
    relogio.tick(fps)
    if 24 < score < 56:
        velocidade = 15
        fps = 30
    janela.fill((0, 0, 0))
    mensagem = f'Pontuação = {score}'
    textoFormatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                x_controle = -velocidade
                y_controle = 0
            if event.key == K_d and x_controle != -velocidade:
                x_controle = velocidade
                y_controle = 0
            if event.key == K_w and y_controle != velocidade:
                x_controle = 0
                y_controle = -velocidade
            if event.key == K_s and y_controle != -velocidade:
                x_controle = 0
                y_controle = velocidade


    cobra = pygame.draw.rect(janela, (0, 255, 0), (x_cobra, y_cobra, 23, 30))
    maca = pygame.draw.rect(janela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    x_cobra += x_controle
    y_cobra += y_controle

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_corpo.append(lista_cabeca)

    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]


    cresce_cobra(lista_corpo)

    if cobra.colliderect(maca):
        velocidade += 0.4
        comprimento_inicial +=1
        score += 1
        coin.play()
        x_maca = randint(5, 540)
        y_maca = randint(5, 540)

    # if cobra.collidelist(lista_corpo):
    #     pass

    janela.blit(textoFormatado, (550, 20))  # Adiciona o texto na janela com os parametros para a posicao x e y
    pygame.display.update()
