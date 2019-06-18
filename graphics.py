import sys, pygame, color


def initialize_display(x, y):


    display_size = [int(x), int(y)]

    # Initializes everything necessary for Pygame
    pygame.init()

    # Sets window's size
    gameDisplay = pygame.display.set_mode(display_size)

    # Draws the background in white
    gameDisplay.fill(color.white)

    # Sets window's name
    pygame.display.set_caption('Fishbowl')

    # Updates display
    pygame.display.update()

    # Starts the clock
    clock = pygame.time.Clock()

    return gameDisplay, clock



def update(fps, clock):
    # Updates display
    pygame.display.update()
    # Sets the clock according to the fps
    clock.tick(fps)
    return



def close_display():
    # Terminates Pygame
    pygame.quit()



def draw_fish(gameDisplay, pos, size):
    points = ((pos[0]-size, pos[1]+size), (pos[0]+size, pos[1]+size), (pos[0]+size, pos[1]-size), (pos[0]-size, pos[1]-size))
    pygame.draw.polygon(gameDisplay, color.blue, points)


def draw_food(gameDisplay, pos, size):
    points = ((pos[0]-size, pos[1]+size), (pos[0]+size, pos[1]+size), (pos[0]+size, pos[1]-size), (pos[0]-size, pos[1]-size))
    pygame.draw.polygon(gameDisplay, color.green, points)


def draw_line(gameDisplay, a, b, thickness=1):
    pygame.draw.line(gameDisplay, color.black, a, b, thickness)
