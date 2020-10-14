import pygame, sys
pygame.init()
font= pygame.font.Font(None, 32)
rect_text= pygame.Rect(540,350,140,32)
color_active= pygame.Color("lightskyblue3")
color_pasive=pygame.Color("gray15")
color= color_pasive
fig_text={r"C:/Users/Luis/Pictures/boca.png" : "mun", r"C:/Users/Luis/Pictures/dientes.png": "tänd", r"C:/Users/Luis/Pictures/labios.png": "läpp",
          r"C:/Users/Luis/Pictures/lengua.png": "tunga", r"C:/Users/Luis/Pictures/pie.png": "fot", r"C:/Users/Luis/Pictures/pierna.png": "ben"}
def main():

    screen = pygame.display.set_mode([1000, 600])
    image_mouth = pygame.image.load(r"C:/Users/Luis/Pictures/boca.png")
    user_text = ""
    active = False
    running = True
    show_image = False
    show_text= False
    next= False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for k, v in fig_text:
                if pygame.mouse.get_pos()[0] >= 800 and pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[
                    1] >= 280 and pygame.mouse.get_pos()[1] <= 320 and event.type == pygame.MOUSEBUTTONDOWN:
                        show_image = True
                        show_text=True

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
                for v in fig_text:
                    if user_text.lower() == v:
                        next = True
                    else:
                        next=False

        screen.fill((255, 255, 255))
        if next:
            for k in fig_text:
                if show_image:
                    screen.blit(k, (500, 140))

        if next:
            for v in fig_text:
                if show_text:
                    text_surface = font.render(v, True, (0, 0, 0))
                    screen.blit(text_surface, (rect_text.x + 5, rect_text.y + 5))
                    pygame.draw.rect(screen, color, rect_text, 2)
                    rect_text.w = max(100, text_surface.get_width() + 10)

        if active==False:
            color=color_pasive
        else:
            color=color_active


        rect_button = pygame.draw.rect(screen, (255, 153, 204), (800, 280, 80, 40))
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()
