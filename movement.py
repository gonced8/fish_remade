import math

def next_pos(world, fish, dt):

    fish.input[15] = 0   # Assume the fish is stopped

    # Move
    fish.output[1] = fish.output[1]*1.5-0.5

    if fish.output[1]==0:
        return

    world_size = world.size()

    position=fish.pos

    fish_speed=200*fish.output[1]

    # Turn
    fish.output[1] = int(fish.output[0]*180-90)

    fish.angle += int(fish.output[0])

    fish.angle %= 360

    #print(position, fish.angle)

    # Converts the angle to the proper x and y components
    direction = [math.cos(math.radians(fish.angle)), math.sin(math.radians(fish.angle))]

    # Sets the time division accordingly to the fps
    #dt=1.0/fps

    # Calculates the amount to move
    dpos = list(map(int, [fish_speed*direction[0]*dt, fish_speed*direction[1]*dt]))

    # Updates position
    if inside(fish, dpos, world):
        fish.pos =  [fish.pos[0]+dpos[0], fish.pos[1]+dpos[1]]
        fish.input[15] = 1   # The fish is moving



def inside(fish, dpos, world):

    pos = [fish.pos[0]+dpos[0], fish.pos[1]+dpos[1]]
    size = world.size()

    if pos[0]>0 and pos[0]<size[0] and pos[1]>0 and pos[1]<size[1]:
        return True

    else:
        return False
