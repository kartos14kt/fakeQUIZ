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

class Button:
    def __init__(self, x, y, w, h, text, font, cor_fundo, cor_texto, cor_borda=None, borda=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.cor_borda = cor_borda
        self.borda = borda
        self.text_surf = self.font.render(self.text, True, self.cor_texto)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.cor_fundo, self.rect)
        if self.cor_borda and self.borda > 0:
            pygame.draw.rect(surface, self.cor_borda, self.rect, self.borda)
        surface.blit(self.text_surf, self.text_rect)

botao_font = pygame.font.SysFont("Comic Sans MS", 36, bold=True)
botao_comecar = Button(largura // 2 - 100, 200, 200, 75, "COMEÇAR", botao_font, MARROM, PRETO, (100, 40, 10), 4)

def questoes(numero, screen, largura, roxo_claro, roxo_escuro):
    pygame.draw.circle(screen, roxo_claro, (50, 50), 30)
    pygame.draw.circle(screen, roxo_escuro, (50, 50), 30, 4)
    font = pygame.font.SysFont("Comic Sans MS", 36, bold=True)
    texto = font.render(str(numero), True, (0, 0, 0))
    texto_rect = texto.get_rect(center=(50, 50))
    screen.blit(texto, texto_rect)

def mostrar_menu():
    while True:
        mouse_sobre_botao = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_comecar.rect.collidepoint(event.pos):
                    import Q1
                    Q1.mostrar_q1(screen)
                    return
        mouse_pos = pygame.mouse.get_pos()
        if botao_comecar.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.fill((CINZA))
        text_rect = text.get_rect(center=centro)
        text_rect.y = 80
        screen.blit(text, text_rect)
        botao_comecar.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    mostrar_menu()