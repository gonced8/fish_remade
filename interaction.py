import world
import fish
import math

def eat(world, fish, food):

    for x in range (-fish.size, fish.size):
        for y in range (-fish.size, fish.size):

            pos = [int(fish.pos[0])+x, int(fish.pos[1])+y]

            if not world.free_pos(pos):

                fish.hunger -= 0.2

                if fish.hunger < 0:
                    fish.hunger = 0

                fish.input[13]=fish.hunger

                world.remove(pos)

                food.remove(pos)

                return True

    return False



def vision(world, fish):

    d = fish.distance

    position = [int(fish.pos[0]), int(fish.pos[1])]

    for i in range (13):
        fish.input[i] = 0

    for x in range (-d, d):

        for y in range(-d, d):

            pos = [position[0]+x, position[1]+y]

            if world.free_pos(pos):
                continue

            if not in_range(position, pos, d):
                continue

            if not in_field(position, pos, fish.angle, fish.amplitude):
                continue

            sensor = what_sensor(position, pos, fish.angle, fish.amplitude)

            dist=math.sqrt((position[0]-pos[0])**2 + (position[1]-pos[1])**2)

            fish.input[sensor]=dist/d


def in_range(center, pos, radius):

    if ((pos[0]-center[0])**2 + (pos[1]-center[1])**2) <= radius**2:
        return True
    else:
        return False


def in_field(center, pos, angle, amplitude):

    alpha = math.degrees(math.atan2(pos[1] - center[1], pos[0] - center[0]))
    if alpha < 0:
        alpha = alpha + 360

    alpha = alpha - angle

    if alpha < 0:
        alpha = -alpha

    if alpha > 180:
        alpha = 360 - alpha

    if alpha<amplitude/2.0:
        return True

    return False


def what_sensor (center, pos, angle, amplitude):

    dx=pos[0]-center[0]
    dy=pos[1]-center[1]

    alpha = math.degrees( math.atan2(dy,dx) )

    if alpha<0:
        alpha = alpha+360

    #print(center, pos)
    #print(angle,alpha)

    alpha = angle-alpha

    #if alpha>180:
     #   alpha = alpha-360

    #elif alpha<-180:
     #   alpha = alpha+360

    if alpha<-amplitude/2.0:
        alpha+=360

    elif alpha>amplitude/2.0:
        alpha-=360

    alpha = alpha+amplitude/2.0

    alpha = int(round(alpha/10))

    #print(alpha,'\n')

    if alpha > 12:
        print ('Error in vision, field of view, function what_sensor, greater than 12')
        print(alpha)
        input()
        alpha=12

    return alpha



def vision2(world, fish):

    position = [int(fish.pos[0]), int(fish.pos[1])]
    angle = math.radians(fish.angle)
    amplitude = math.radians(fish.amplitude)
    distance = fish .distance

    for i in range (13):
        fish.input[i] = 0

    for j in range (-distance, distance):
        for i in range (-distance, distance):

            pos = [position[0]+i, position[1]+j]

            if world.free_pos(pos):
                continue

            if i**2+j**2<=distance**2:

                alpha=angle+amplitude/2.0

                if math.cos(alpha)*(j) < math.sin(alpha)*(i):

                    alpha=angle-amplitude/2.0

                    if math.cos(alpha)*(j) > math.sin(alpha)*(i):

                        sensor = what_sensor(position, pos, fish.angle, fish.amplitude)

                        dist=math.sqrt((position[0]-pos[0])**2 + (position[1]-pos[1])**2) / distance

                        if dist >= fish.input[sensor]:
                            fish.input[sensor]=dist
