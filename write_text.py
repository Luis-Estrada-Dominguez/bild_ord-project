import pygame, sys
pygame.init()
font= pygame.font.Font(None, 32)
rect_text= pygame.Rect(200,200,140,32)
color_active= pygame.Color("lightskyblue3")
color_pasive=pygame.Color("gray15")
color= color_pasive



def main():
    user_text = ""
    clock=pygame.time.Clock()
    screen= pygame.display.set_mode([800, 600])
    active = False
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if rect_text.collidepoint(event.pos):
                    active=True
            if event.type== pygame.KEYDOWN:
                if active == True:
                    if event.key== pygame.K_BACKSPACE:
                        user_text=user_text[0:-1]
                    else:
                        user_text += event.unicode
        if active==False:
            color=color_pasive
        else:
            color=color_active
        screen.fill((0,0,0))
        text_surface=font.render(user_text, True, (255,255,255))
        screen.blit(text_surface,(rect_text.x + 5, rect_text.y + 5))
        pygame.draw.rect(screen,color, rect_text, 2)
        rect_text.w= max(100,text_surface.get_width()+10)

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()
