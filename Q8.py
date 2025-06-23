import pygame
import sys

def mostrar_q8(screen):
    import menu
    largura = 800
    altura = 600
    PRETO = (0, 0, 0)
    CINZA = (200, 200, 200)
    MARROM = (139, 69, 19)
    MARROM_ESCURO = (100, 40, 10)
    alt_font = pygame.font.SysFont("Comic Sans MS", 32, bold=True)
    roxo_claro = (180, 140, 255)
    roxo_escuro = (80, 0, 120)
    clock = pygame.time.Clock()

    # Carrega a imagem da questão
    try:
        imagem = pygame.image.load("questao.png")
        imagem = pygame.transform.smoothscale(imagem, (137, 203))
    except Exception as e:
        imagem = None

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

    alt_textos = ["12", "14", "10", "16", "1"]
    botoes = []
    btn_w, btn_h = 300, 60  # Deixa igual aos outros arquivos
    espaco_x = 40
    x1 = largura // 2 - btn_w - espaco_x // 2
    x2 = largura // 2 + espaco_x // 2
    y_cima = 240
    y_baixo = 240 + 90
    botoes.append(Button(x1, y_cima, btn_w, btn_h, alt_textos[0], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    botoes.append(Button(x2, y_cima, btn_w, btn_h, alt_textos[1], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    botoes.append(Button(x1, y_baixo, btn_w, btn_h, alt_textos[2], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    botoes.append(Button(x2, y_baixo, btn_w, btn_h, alt_textos[3], alt_font, MARROM, PRETO, MARROM_ESCURO, 4))
    indice_correto = 0  # Altere para o índice da alternativa correta

    # Botão transparente com número 1, fonte Arial maior, sem negrito
    botoes.append(Button(324, 12, 50, 50, alt_textos[4], pygame.font.SysFont("Arial", 43, bold=False), (0,0,0), PRETO, None, 0,))

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
                if botoes[indice_correto].rect.collidepoint(event.pos):
                    menu.mostrar_menu()  # Troque para avançar para a próxima questão se desejar
                    return
                elif any(b.rect.collidepoint(event.pos) for i, b in enumerate(botoes) if i != indice_correto):
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
        questoes(8, screen, largura, roxo_claro, roxo_escuro)
        # Exibe a imagem centralizada
        if imagem:
            img_rect = imagem.get_rect(center=(largura // 2, 120))  # Posição mais para cima
            screen.blit(imagem, img_rect)
        else:
            erro_font = pygame.font.SysFont("Comic Sans MS", 24, bold=True)
            erro_text = erro_font.render("questao.png não encontrada", True, (200,0,0))
            screen.blit(erro_text, (largura//2 - 120, 80))
        for btn in botoes:
            # Só desenha fundo se não for o botão transparente
            if btn.text == "1":
                btn.text_surf = btn.font.render(btn.text, True, PRETO)
                btn.text_rect = btn.text_surf.get_rect(center=btn.rect.center)
                screen.blit(btn.text_surf, btn.text_rect)
            else:
                btn.draw(screen)
        direitos_font = pygame.font.SysFont("Comic Sans MS", 20, bold=True)
        direitos_text = direitos_font.render("nenhum direito reservado © Murilo CZR 2025", True, (0,0,0))
        screen.blit(direitos_text, (10, altura - 30))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quiz - Questão 8")
    mostrar_q8(screen)
