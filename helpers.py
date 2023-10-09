import textwrap
from constants import *

def setmap(room):
    pass

def print_text(text, font, area, line):
    line = line * 20
    area.blit(font.render(text, True, BLACK), (0,line))

# Input: text and width
# Output: a list of lines
def break_up_line(input_text, max_length):
    wrapper = textwrap.TextWrapper(width=max_length)
    return wrapper.wrap(text=input_text)
