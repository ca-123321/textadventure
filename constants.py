WIDTH = 1000
HEIGHT = 700
INPUT_H = 70         # Input area height
SIDE_BOXES_WH = 210  # minimap/"look", images should be 200x200 giving a small border
CUSHION_LEFT = 80    # left of screen, to the right
CUSHION_SMALL = 30   # Small cushions: Top, right, bottom, TODO: perhaps between sideboxes
CUSHION_MID_W = 50   # horizontal b/t output and right-areas (next to output on the right)
CUSHION_MID_H = 20   # vertical b/t right-areas (currently minimap and "look")
CUSHION_BT_IO = 50   # between input and output areas
OUTPUT_W = 470
OUTPUT_H = 370
#OUTPUT_W = WIDTH - (CUSHION_LEFT + CUSHION_MID_W + SIDE_BOXES_WH + CUSHION_SMALL)
#OUTPUT_H = HEIGHT - (CUSHION_SMALL + INPUT_H + CUSHION_SMALL + CUSHION_BT_IO)
INPUT_W = OUTPUT_W   # Set input area to be the same width as output area

# Colors
INPUT_BG = '#505050'
SCREEN_BG = '#cdc8b1'
OUTPUT_BG = '#008b8b'
BOTTOMRIGHT_BG = '#cd9b1d'
BLACK = '#000000'
SIDEBOX1_BG = '#698b69'
SIDEBOX2_BG = '#ee2c2c'

ROOM = 0
DAY = 1
VERBS = ['go', 'take', 'give', 'look', 'quit', 'change', 'wait']