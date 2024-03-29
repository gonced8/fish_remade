from random import choice

black = (0, 0, 0)
gray = (128, 128, 128)
silver = (192, 192, 192)
white = (255, 255, 255)
maroon = (128, 0, 0)
red = (255, 0, 0)
olive = (128, 128, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
lime = (0, 255, 0)
teal = (0, 128, 128)
aqua = (0, 255, 255)
navy = (0, 0, 128)
blue = (0, 0, 255)
purple = (128, 0, 128)
pink = (255, 0, 255)

colors = [black, gray, silver, white, maroon, red, olive, yellow, green, lime, teal, aqua, navy, blue, purple, pink]

def random_color ():
    return choice(colors)