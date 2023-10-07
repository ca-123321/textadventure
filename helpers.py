from constants import *

def setmap(room):
    pass

def print_text(text, font, area, line):
    line = line * 20
    area.blit(font.render(text, True, BLACK), (0,line))