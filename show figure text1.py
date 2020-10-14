import pygame, sys
pygame.init()
pygame.image.load("boca.png")
pygame.image.load("dientes.png")
pygame.image.load("labios.png")
pygame.image.load("lengua.png")
pygame.image.load("pie.png")
pygame.image.load("pierna.png")
img_list = [None, pygame.image.load("boca.png"), pygame.image.load("dientes.png"), pygame.image.load("labios.png"), pygame.image.load("lengua.png"), pygame.image.load("pie.png"), pygame.image.load("pierna.png")]

screen = pygame.display.set_mode([1000, 600])
font= pygame.font.Font(None, 32)
rect_text= pygame.Rect(540,350,140,32)
color_active= pygame.Color("lightskyblue3")
color_pasive=pygame.Color("gray15")
color= color_pasive

def main():

    user_text = ""
    active = False
    running = True
    show_text= False
    current_img = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_text.collidepoint(event.pos):
                    active = True
                else:
                    active= False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[0:-1]
                    else:
                        user_text += event.unicode
                if user_text.lower() == "mun":
                    running = False

            if pygame.mouse.get_pos()[0] >= 800 and pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] >= 280 and pygame.mouse.get_pos()[1] <= 320 and event.type == pygame.MOUSEBUTTONDOWN:
                current_img += 1
                show_text = True
                if current_img >= len(img_list):
                    current_img = 1


        screen.fill((255, 255, 255))

        if img_list[current_img] is not None:
            screen.blit(img_list[current_img], (500, 140))

        if not active:
            color=color_pasive
        else:
            color=color_active

        if show_text:
            text_surface = font.render(user_text, True, (0, 0, 0))
            screen.blit(text_surface, (rect_text.x + 5, rect_text.y + 5))
            pygame.draw.rect(screen, color, rect_text, 2)
            rect_text.w = max(100, text_surface.get_width() + 10)

        rect_button = pygame.draw.rect(screen, (255, 153, 204), (800, 280, 80, 40))
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()