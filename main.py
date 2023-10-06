import pygame_textinput
import pygame
from constants import *
from parsing import *
from sys import exit
import os.path
import math

# init stuff
pygame.init()
pygame.display.set_caption('Text Adventure Someday')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_general = pygame.font.Font('font/Molengo-Regular.ttf', 40)
pygame.key.set_repeat(200, 25)

output_text_area = pygame.Surface((OUTPUT_W, OUTPUT_H))
output_rect = output_text_area.get_rect(topleft = (CUSHION_LEFT,CUSHION_SMALL))
input_text_area = pygame.Surface((INPUT_W, INPUT_H))
input_text_rect = input_text_area.get_rect(bottomleft = (CUSHION_LEFT, HEIGHT - CUSHION_SMALL))
minimap_area = pygame.Surface((SIDE_BOXES_WH, SIDE_BOXES_WH))
minimap_rect = minimap_area.get_rect(center = (
    WIDTH - CUSHION_SMALL - SIDE_BOXES_WH//2, CUSHION_SMALL + OUTPUT_H//4))
picframe_area = pygame.Surface((SIDE_BOXES_WH, SIDE_BOXES_WH))
picframe_rect = picframe_area.get_rect(center = (
    WIDTH - CUSHION_SMALL - SIDE_BOXES_WH//2, CUSHION_SMALL + OUTPUT_H//4 * 3))
bottomright_area = pygame.Surface((SIDE_BOXES_WH, 100))
bottomright_rect = bottomright_area.get_rect(bottomright = (WIDTH - CUSHION_SMALL, HEIGHT - CUSHION_SMALL))

# trying animation
flower_surface = pygame.image.load(os.path.join('graphics/other/', 'flower_58.png')).convert_alpha()
flower_x_pos = 10
flower_y_pos = 30
flower_speed = 2

# screen.fill('cornsilk3')
input_text_area.fill(INPUT_BG)
output_text_area.fill(OUTPUT_BG)
minimap_area.fill(MINIMAP_BG)
picframe_area.fill(PICFRAME_BG)
bottomright_area.fill(BOTTOMRIGHT_BG)

# input marker
input_marker = font_general.render(">", True, BLACK)

# User input
manager = pygame_textinput.TextInputManager()
textinput = pygame_textinput.TextInputVisualizer(manager=manager)
lastinput = ""

# Images
look_pic = pygame.image.load(os.path.join('graphics/other', 'initial_look.jpg')).convert()
map_pic = pygame.image.load(os.path.join('graphics/maps', 'initial_map.jpg')).convert()
daynight = pygame.image.load(os.path.join('graphics/other/time', 'day_cycle.png')).convert()


# daynight scrolling
daynight_width = daynight.get_width()
tiles = math.ceil((OUTPUT_W / daynight_width)) + 1
scroll = 0
daynight_rect = daynight.get_rect(topleft=(scroll, OUTPUT_H-50))

castle_surf = pygame.image.load(os.path.join('graphics/other', 'castle_sm.png')).convert_alpha()
castle_rect = castle_surf.get_rect(midbottom = (50, OUTPUT_H - 50))

while True:
    events = pygame.event.get()
    textinput.update(events)
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(SCREEN_BG)
    if input_text_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
    elif bottomright_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    # onto background
    screen.blit(output_text_area, output_rect)
    screen.blit(input_text_area, input_text_rect)
    screen.blit(minimap_area, minimap_rect)
    screen.blit(picframe_area, picframe_rect)
    screen.blit(bottomright_area, bottomright_rect)
    screen.blit(flower_surface, (flower_x_pos, flower_y_pos))
    if flower_y_pos > 200 or flower_y_pos < 30:
        flower_speed *= -1
    flower_y_pos += flower_speed
    
    # into specific areas
    picframe_area.blit(look_pic, (5,5))
    # Doesn't work, but expected it to... No picture, just the red picframe bg
    # picframe_area.blit(news_pic, picframe_rect.center)
    minimap_area.blit(map_pic, (5,5))
    input_text_area.fill(INPUT_BG)  # need to refill the input bg here
    input_text_area.blit(input_marker, (5,5))
    input_text_area.blit(textinput.surface, (50, 25))
    
    # Daynight scrolling inside output_text_area
    for i in range(tiles):
        daynight_rect.x = i*daynight_width + scroll
        output_text_area.blit(daynight, daynight_rect)

    output_text_area.blit(castle_surf, castle_rect)

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            output_text_area.fill(OUTPUT_BG)
            lastinput = textinput.value
            successful = validate(lastinput)
            turn = parse(textinput.value)
            if turn[0] == True and turn[1] == 'wait':   # change returning success to try/exception
                scroll -= turn[2]
                if abs(scroll) > daynight_width:
                    scroll = 0
            output_text_area.blit(font_general.render(lastinput, True, BLACK), (0,0))
            textinput.value = ""
        if event.type == pygame.MOUSEBUTTONDOWN and bottomright_rect.collidepoint(mouse_pos):
            textinput.value = "go "
            print(manager.cursor_pos)
            manager.cursor_pos = len(textinput.value)

    pygame.display.update()
    clock.tick(60)