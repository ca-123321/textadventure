import pygame_textinput
import pygame
from constants import *
from parsing import *
from helpers import *
from sys import exit
import os.path
import math

# Initialization
pygame.init()
pygame.display.set_caption('Text Adventure Someday')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_input = pygame.font.Font('font/Molengo-Regular.ttf', 40)
font_output = pygame.font.Font('font/Molengo-Regular.ttf', 20)
pygame.key.set_repeat(200, 25)

# UI Areas and rects
output_area = pygame.Surface((OUTPUT_W, OUTPUT_H))
output_rect = output_area.get_rect(topleft = (CUSHION_LEFT,CUSHION_SMALL))
input_area = pygame.Surface((INPUT_W, INPUT_H))
input_text_rect = input_area.get_rect(bottomleft = (CUSHION_LEFT, HEIGHT - CUSHION_SMALL))
# middle_list = pygame.Surface(())
sidebox1_area = pygame.Surface((SIDE_BOXES_WH, SIDE_BOXES_WH))
#sidebox1_rect = sidebox1_area.get_rect(topleft = (output_rect.topright[0]+10, output_rect.topright[1]))
sidebox1_rect = sidebox1_area.get_rect(topright = (WIDTH - CUSHION_SMALL, CUSHION_SMALL))
sidebox_mid_area = pygame.Surface((SIDE_BOXES_WH, 40))
sidebox_mid_rect = sidebox_mid_area.get_rect(topleft = sidebox1_rect.bottomleft)
sidebox2_area = pygame.Surface((SIDE_BOXES_WH, SIDE_BOXES_WH))
sidebox2_rect = sidebox2_area.get_rect(topleft = (sidebox_mid_rect.bottomleft[0], sidebox_mid_rect.bottomleft[1]+20))
sidebox_bottom_area = pygame.Surface((SIDE_BOXES_WH, 40))
sidebox_bottom_rect = sidebox_bottom_area.get_rect(topleft = sidebox2_rect.bottomleft)
bottomright_area = pygame.Surface((SIDE_BOXES_WH, 100))
bottomright_rect = bottomright_area.get_rect(bottomright = (WIDTH - CUSHION_SMALL, HEIGHT - CUSHION_SMALL))

# UI Fills -- some are filled in the game loop
input_area.fill(INPUT_BG)
output_area.fill(OUTPUT_BG)
sidebox1_area.fill(SIDEBOX1_BG)
sidebox2_area.fill(SIDEBOX2_BG)
sidebox_mid_area.fill(BLACK)
sidebox_bottom_area.fill(BLACK)
bottomright_area.fill(BOTTOMRIGHT_BG)

# Side animation playing
flower_surface = pygame.image.load(os.path.join('graphics/other/', 'flower_58.png')).convert_alpha()
flower_x_pos = 10
flower_y_pos = 30
flower_speed = 2

# User input
input_marker = font_input.render(">", True, BLACK)
manager = pygame_textinput.TextInputManager()
textinput = pygame_textinput.TextInputVisualizer(manager=manager)
lastinput = ""

# Images
look_pic = pygame.image.load(os.path.join('graphics/other', 'initial_look.jpg')).convert()
map_pic = pygame.image.load(os.path.join('graphics/maps', 'initial_map.jpg')).convert()
daynight = pygame.image.load(os.path.join('graphics/other/time', 'day_cycle.png')).convert()

# Daynight scrolling
daynight_width = daynight.get_width()
tiles = math.ceil((OUTPUT_W / daynight_width)) + 1
scroll = 0
daynight_rect = daynight.get_rect(topleft=(scroll, OUTPUT_H-50))

# Castle image, just for experimenting, maybe will be decoration reflecting the current room/zone/weather
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

    # Background rendering
    screen.blit(output_area, output_rect)
    screen.blit(input_area, input_text_rect)
    screen.blit(sidebox1_area, sidebox1_rect)
    screen.blit(sidebox2_area, sidebox2_rect)
    screen.blit(sidebox_mid_area, sidebox_mid_rect)
    screen.blit(sidebox_bottom_area, sidebox_bottom_rect)
    screen.blit(bottomright_area, bottomright_rect)
    screen.blit(flower_surface, (flower_x_pos, flower_y_pos))
    if flower_y_pos > 200 or flower_y_pos < 30:
        flower_speed *= -1
    flower_y_pos += flower_speed
    
    # Rendering into specific areas
    sidebox2_area.blit(look_pic, (5,5))
    # Doesn't work, but expected it to... No picture, just the red picframe bg
    # picframe_area.blit(news_pic, picframe_rect.center)
    sidebox1_area.blit(map_pic, (5,5))
    input_area.fill(INPUT_BG)  # need to refill the input bg here
    input_area.blit(input_marker, (5,10))
    input_area.blit(textinput.surface, (50, 25))
    
    # Daynight scrolling inside output_text_area
    for i in range(tiles):
        daynight_rect.x = i*daynight_width + scroll
        output_area.blit(daynight, daynight_rect)

    output_area.blit(castle_surf, castle_rect)

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            output_area.fill(OUTPUT_BG)
            lastinput = textinput.value
            #successful = validate(lastinput)
            # while successful: ... 
            turn = parse(textinput.value)
            if turn[0] == True and turn[1] == 'wait':   # change returning success to try/exception
                scroll -= turn[2]
                if abs(scroll) > daynight_width:
                    scroll = 0
            print_text(lastinput, font_output, output_area)
            textinput.value = ""
        if event.type == pygame.MOUSEBUTTONDOWN and bottomright_rect.collidepoint(mouse_pos):
            textinput.value = "go "
            print(manager.cursor_pos)
            manager.cursor_pos = len(textinput.value)

    pygame.display.update()
    clock.tick(60)