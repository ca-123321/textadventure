import pygame
from constants import *
import os.path

def parse(text):
    success = False
    time_passed = 0
    action = ""
    print("parsing: ", text)
    words = text.split(' ')
    if words[0] in VERBS:
        match words[0]:
            case 'quit':
                success = True
                pygame.quit()
                exit()
            case 'change':
                # map_pic = pygame.image.load(os.path.join('graphics/maps', '00.jpg'))
                print("Should change the map")
                success = True
            case 'wait' if len(words) == 1:  # Default waiting
                time_passed = 10
                action = 'wait'
                success = True
            # string '12.2' needs to be converted to float then int, maybe better way to do this
            case 'wait' if isinstance(int(float(words[1])), int) and 1 <= int(float(words[1])) <= 100:
                time_passed = int(float(words[1]))
                action = 'wait'
                success = True
            case 'wait' if isinstance(int(float(words[1])), int) and int(float(words[1])) > 100:
                print("Too long to wait")
            case _:
                print("Didn't understand")
    else:
        print("Use a verb from verbs")

    return (success, action, time_passed)