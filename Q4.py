import pygame
import sys

def mostrar_q4(screen):
    import menu
    largura = 800
    altura = 600
    centro = (largura // 2, altura // 2)
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    CINZA = (200, 200, 200)
    MARROM = (139, 69, 19)
    MARROM_ESCURO = (100, 40, 10)
    font = pygame.font.SysFont("Comic Sans MS", 48)
    pergunta_font = pygame.font.SysFont("Comic Sans MS", 36)
    alt_font = pygame.font.SysFont("Comic Sans MS", 32, bold=True)
    roxo_claro = (180, 140, 255)
    roxo_escuro = (80, 0, 120)
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

    def questoes(numero, screen, largura, roxo_claro, roxo_escuro):
        pygame.draw.circle(screen, roxo_claro, (50, 50), 30)
        pygame.draw.circle(screen, roxo_escuro, (50, 50), 30, 4)
        font = pygame.font.SysFont("Comic Sans MS", 36, bold=True)
        texto = font.render(str(numero), True, (0, 0, 0))
        texto_rect = texto.get_rect(center=(50, 50))
        screen.blit(texto, texto_rect)

    pergunta = "Ps4."
    alt_textos = ["Dualchok 4", "Dualshok 4", "Dualshock 4", "DUALSHOOK 4"]
    botoes = []
    btn_w, btn_h = 300, 60
    espaco_x = 40
    x1 = largura // 2 - btn_w - espaco_x // 2
    x2 = largura // 2 + espaco_x // 2
    y_cima = 220
    y_baixo = 220 + 90
    botoes.append(Button(x1, y_cima, btn_w, btn_h, alt_textos[0], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    botoes.append(Button(x2, y_cima, btn_w, btn_h, alt_textos[1], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    botoes.append(Button(x1, y_baixo, btn_w, btn_h, alt_textos[2], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    botoes.append(Button(x2, y_baixo, btn_w, btn_h, alt_textos[3], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))

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
                if botoes[2].rect.collidepoint(event.pos):  # Alternativa correta: 'Dualshock 4'
                    import Q5
                    Q5.mostrar_q5(screen)  # Avança para a próxima questão
                    return
                elif any(b.rect.collidepoint(event.pos) for i, b in enumerate(botoes) if i != 2):
                    menu.mostrar_menu()
                    return
        mouse_pos = pygame.mouse.get_pos()
        for btn in botoes:
            if btn.rect.collidepoint(mouse_pos):
                mouse_sobre_botao = True
                break
        if mouse_sobre_botao:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.fill(CINZA)
        questoes(4, screen, largura, roxo_claro, roxo_escuro)
        pergunta_surf = pergunta_font.render(pergunta, True, PRETO)
        pergunta_rect = pergunta_surf.get_rect(center=(largura // 2, 140))
        screen.blit(pergunta_surf, pergunta_rect)
        for btn in botoes:
            btn.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quiz - Questão 4")
    mostrar_q4(screen)
