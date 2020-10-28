import pygame
pygame.init()
pygame.image.load("boca.png")
pygame.image.load("dientes.png")
pygame.image.load("labios.png")
pygame.image.load("lengua.png")
pygame.image.load("pie.png")
pygame.image.load("pierna.png")
img_list = [None, pygame.image.load("boca.png"), pygame.image.load("dientes.png"),
            pygame.image.load("labios.png"), pygame.image.load("lengua.png"),
            pygame.image.load("pie.png"), pygame.image.load("pierna.png")]
list_esp = [None, "boca", "dientes", "labios", "lengua", "pie", "pierna"]
list_svensk = [None, "mun", "tänder", "läppar", "tunga", "fot", "ben"]
list_choice = list_svensk
screen = pygame.display.set_mode([500, 400])
font = pygame.font.Font(None, 32)
rect_text = pygame.Rect(95, 250, 140, 32)
color_active = pygame.Color("lightskyblue3")
color_pasive = pygame.Color("gray15")
color = color_pasive

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


class Allbuttons:
    def __init__(self, surface, x, y, width, height, colour):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def display_buttons(self):
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.width, self.height))


button_hint = Allbuttons(screen, 250, 130, 80, 40, RED)
button_start = Allbuttons(screen, 250, 180, 80, 40, YELLOW)
button_language = Allbuttons(screen, 250, 80, 80, 40, BLUE)


def main():
    user_text = ""
    active = False
    running = True
    show_text = False
    correct_text = True
    current_img = 0
    current_txt = 0
    count_hint = 0
    change_language = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_text.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if 250 <= pygame.mouse.get_pos()[0] <= 330 and \
                80 <= pygame.mouse.get_pos()[
                 1] <= 120 and event.type == pygame.MOUSEBUTTONDOWN:
                change_language *= -1

            if correct_text and 250 <= pygame.mouse.get_pos()[0] <= 330 and \
                    180 <= pygame.mouse.get_pos()[1] <= 220 and event.type == pygame.MOUSEBUTTONDOWN:
                user_text = ""
                correct_text = False
                current_img += 1
                current_txt += 1
                show_text = True
                count_hint = 0
                if current_img >= len(img_list):
                    current_img = 1
                if current_txt >= len(list_choice):
                    current_txt = 1

            if 250 <= pygame.mouse.get_pos()[0] <= 330 and \
                    130 <= pygame.mouse.get_pos()[1] <= 170 and event.type == pygame.MOUSEBUTTONDOWN:
                count_hint += 1
                user_text = ""
                lista_txt_list = list(list_choice[current_txt])
                if count_hint > len(list_choice[current_txt]):
                    count_hint = 1
                for i in range(0, count_hint):
                    user_text += lista_txt_list[i]

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[0:-1]
                    else:
                        user_text += event.unicode

        screen.fill((255, 255, 255))

        if img_list[current_img] is not None:
            screen.blit(img_list[current_img], (50, 50))

        if not active:
            color = color_pasive
        else:
            color = color_active

        if show_text:
            text_surface = font.render(user_text, True, (0, 0, 0))
            screen.blit(text_surface, (rect_text.x + 5, rect_text.y + 5))
            pygame.draw.rect(screen, color, rect_text, 2)
            rect_text.w = max(100, text_surface.get_width() + 10)

        if change_language == 1:
            list_choice = list_esp
        else:
            list_choice = list_svensk

        if not correct_text:
            if user_text.lower() == list_choice[current_txt] and list_choice[current_txt] is not None:
                correct_text = True
            else:
                correct_text = False

        button_hint.display_buttons()
        button_start.display_buttons()
        button_language.display_buttons()
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
