WIDTH = 800
HEIGHT = 700
INPUT_H = 70         # Input area height
SIDE_BOXES_WH = 210  # minimap/"look", images should be 200x200 giving a small border
CUSHION_LEFT = 80    # left of screen, to the right
CUSHION_SMALL = 30   # Small cushions: Top, right, bottom, TODO: perhaps between sideboxes
CUSHION_MID_W = 50   # horizontal b/t output and right-areas (next to output on the right)
CUSHION_MID_H = 20   # vertical b/t right-areas (currently minimap and "look")
CUSHION_BT_IO = 50   # between input and output areas
OUTPUT_W = WIDTH - (CUSHION_LEFT + CUSHION_MID_W + SIDE_BOXES_WH + CUSHION_SMALL)
OUTPUT_H = HEIGHT - (CUSHION_SMALL + INPUT_H + CUSHION_SMALL + CUSHION_BT_IO)
INPUT_W = OUTPUT_W   # Set input area to be the same width as output area
OUTPUT_MIN = 300
INPUT_W_MIN = 300

# Basic checks

# assert HEIGHT >= CUSHION_TOP + OUTPUT_MIN + CUSHION_BT_IO + INPUT_H + CUSHION_BOTTOM
# assert WIDTH >= CUSHION_LEFT + OUTPUT_MIN + CUSHION_MID_W + SIDE_BOXES_WH + CUSHION_RIGHT
assert HEIGHT >= 600
assert WIDTH >= 600

# Colors
INPUT_BG = '#505050'
SCREEN_BG = '#cdc8b1'
OUTPUT_BG = '#008b8b'
BOTTOMRIGHT_BG = '#cd9b1d'
BLACK = '#000000'
MINIMAP_BG = '#698b69'
PICFRAME_BG = '#ee2c2c'

ROOM = 0
DAY = 1
VERBS = ['go', 'take', 'give', 'look', 'quit', 'change', 'wait']