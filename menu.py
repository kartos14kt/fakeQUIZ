import pygame
import sys

pygame.init()

largura = 800
altura = 600
centro = (largura // 2, altura // 2)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
MARROM = (139, 69, 19)
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("FAKE QUIZ")

font = pygame.font.SysFont("Comic Sans MS", 48)
text = font.render("Bem-vindo!", True, PRETO)
clock = pygame.time.Clock()

botao_rect = pygame.Rect((largura // 2 - 100, 200, 200, 75))
botao_font = pygame.font.SysFont("Comic Sans MS", 36, bold=True)
botao_texto = botao_font.render("COMEÇAR", True, BRANCO)
botao_texto_rect = botao_texto.get_rect(center=botao_rect.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((CINZA))
    text_rect = text.get_rect(center=centro)
    text_rect.y = 80
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, MARROM, botao_rect)
    screen.blit(botao_texto, botao_texto_rect)
    pygame.display.flip()
    clock.tick(60)