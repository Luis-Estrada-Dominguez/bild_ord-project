import pygame, sys
pygame.init()
font= pygame.font.Font(None, 32)
rect_text= pygame.Rect(540,350,140,32)
color_active= pygame.Color("lightskyblue3")
color_pasive=pygame.Color("gray15")
color= color_pasive

def main():

    screen = pygame.display.set_mode([1000, 600])
    image_mouth = pygame.image.load(r"C:/Users/Luis/Pictures/boca.png")
    user_text = ""
    active = False
    running = True
    show_image = False
    show_text= False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                if user_text.lower() == "mun":
                    running = False

        screen.fill((255, 255, 255))
        if show_image:
            screen.blit(image_mouth, (500, 140))

        if show_text:
            text_surface = font.render(user_text, True, (0, 0, 0))
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


if __name__ == "__main__":
    main()
