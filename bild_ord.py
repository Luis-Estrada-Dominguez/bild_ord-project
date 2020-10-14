
import pygame
#image_mouth = pygame.image.load("C:/Users/Luis/Pictures/boca.png")

#screen = pygame.display.set_mode([1000, 600])



def main():
    pygame.init()
    screen = pygame.display.set_mode([1000, 600])
    image_mouth = pygame.image.load(r"C:/Users/Luis/Pictures/boca.png")
    #image_tooth= pygame.image.load(r"C:/Users/Luis/Pictures/dientes.png")
    running = True
    show_image= False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pos()[0] >=800 and pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] >= 280 and pygame.mouse.get_pos()[1] <= 320 and event.type == pygame.MOUSEBUTTONDOWN:
                #screen.blit(image_mouth, (300, 300))
                show_image=True

        screen.fill((255, 255, 255))
        if show_image:
            screen.blit(image_mouth, (300, 300))

        #pygame.display.update()

        rect_button = pygame.draw.rect(screen, (255, 153, 204), (800, 280, 80, 40))
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
