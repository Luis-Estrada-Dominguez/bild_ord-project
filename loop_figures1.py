
import pygame
pygame.init()
pygame.image.load("boca.png")
pygame.image.load("dientes.png")
pygame.image.load("labios.png")
img_list=[pygame.image.load("boca.png"), pygame.image.load("dientes.png"),pygame.image.load("labios.png")]
show_img=[False, False, False]

screen = pygame.display.set_mode([1000, 600])
#def img_display(i,x,y):
    #screen.blit(imgload_list[i],(x,y))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for i in show_img:
                if pygame.mouse.get_pos()[0] >=800 and pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] >= 280 and pygame.mouse.get_pos()[1] <= 320 and event.type == pygame.MOUSEBUTTONDOWN:
                    show_img[i]=True

        screen.fill((255, 255, 255))

        if show_img[i]:
            screen.blit(img_list[i], (300, 300))



        rect_button = pygame.draw.rect(screen, (255, 153, 204), (800, 280, 80, 40))
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
