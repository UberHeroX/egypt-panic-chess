import pygame 
import sys
import os


# Inicijalizacija PyGame modula

pygame_instance = pygame.init()

#Dimenzije prozora

WIDTH = 1280
HEIGHT = 720
screen_size= (WIDTH, HEIGHT)

# Inicijalizacija prozora

window = pygame.display.set_mode(screen_size)


# Ime prozora

window_name = "Egypt - Panic Chess"

pygame.display.set_caption(window_name)


# Nova ikonica za prozor. Uzmemo lokaciju trenutnog foldera gde se nalazi igra, i dodamo files images i ime ikone


current_path = os.path.join(os.getcwd(), "files", "images","icon.png")

# Bilo koja slika mora da se louduje preko ove funkcije

icon = pygame.image.load(current_path)

# postavljamo ikonu

pygame.display.set_icon(icon)

# Boje za bar meni

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200, 200 ,200)

# Opcije za meni

menu_options = ["Game", "Edit", "About"]
option_width = 100
option_height = 30

# font

font = pygame.font.Font(None, 30)

def draw_menu():
     y = 0
     for i, option in enumerate(menu_options):
        x = i * option_width
        pygame.draw.rect(window, GRAY, (x, y, option_width, option_height))
        text = font.render(option, True, BLACK)
        window.blit(text, (x + 5, y + 5))


def check_click(position):
    x, y = position
    if y < option_height:
        option_index = x // option_width
        if option_index < len(menu_options):
            print(f"{menu_options[option_index]} was clicked")