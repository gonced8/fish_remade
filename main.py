import pygame
import graphics
import color
import math
import numpy as np
from world import *
from fish import *
import random
import neural_network
import movement
import interaction
import load


def main():

    x = 500
    y = 400

    gameDisplay, clock = graphics.initialize_display(x, y)

    fps = 30
    speed = 50

    aging = 1.

    running = True

    nload = 0

    world = World(x, y)

    population=[]
    max_fish = 3
    for i in range(max_fish):
        name = str(i)
        age = 0
        pos = [random.randint(0, x-1), random.randint(0, y-1)]
        angle = random.randint(0, 359)
        size = 5 #random.randint(5, 10)
        health = 1
        hunger = 1
        amplitude = 90
        distance = 30
        input = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 1, 0]).T
        output = np.array([0, 0]).T

        if not nload:
            layers, brain = neural_network.initialize((input.size, 3, output.size))

        else:
            brain = Brain()
            brain.weights = load.synapses(nload)
            layers = [input.size, output.size]

        population.append( Fish(name, age, pos, angle, size, health, hunger, amplitude, distance, input, output, layers, brain))

    foods=[]
    max_food=200
    for i in range(max_food):

        pos = [random.randint(0, x-1), random.randint(0, y-1)]
        while not world.free_pos(pos):
            pos = [random.randint(0, x-1), random.randint(0, y-1)]

        world.insert(pos, 1)
        foods.append(pos)


    while running:

        # Analizes all users inputs/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draws the background in white
        gameDisplay.fill(color.white)


        # Generate more food if necessary
        while len(foods) < max_food:

            pos = [random.randint(0, x-1), random.randint(0, y-1)]
            while not world.free_pos(pos):
                pos = [random.randint(0, x-1), random.randint(0, y-1)]

            world.insert(pos, 1)
            foods.append(pos)


        flag=False
        fittest=[[0 , 0], [0 , 0]]
        j=0
        for i in range(len(population)):

            if population[j].health>0:

                f=neural_network.fitness(population[j])
                if f>fittest[0][1]:
                    if f<fittest[1][1]:
                        fittest[0]=[population[j], f]
                    elif fittest[0][1]>fittest[1][1]:
                        fittest[1]=[population[j], f]
                    else:
                        fittest[0] = [population[j], f]

                elif f>fittest[1][1]:
                    fittest[1] = [population[j], f]

                j=j+1

            else:
                population.pop(j)

                flag=True


        if flag:
            flag2=0

            if fittest[0]==[0, 0]:
                flag2=1
            else:
                #print (fittest[0][0].name)
                #print (fittest[0][0].brain)
                #print ('\n')
                pass

            if fittest[1]==[0, 0]:
                if not flag:
                    flag2=2
                else:
                    flag2=3
            else:
                #print (fittest[1][0].name)
                #print (fittest[1][0].brain)
                #print ('\n')
                #print ('\n')
                pass


        while len(population) < max_fish:
            if len(population)==0:
                name = "1"
            else:
                name = str( int(population[-1].name) + 1 )
            age = 0
            pos = [random.randint(0, x - 1), random.randint(0, y - 1)]
            angle = random.randint(0, 359)
            size = 5 #random.randint(5, 10)
            health = 1
            hunger = 1
            amplitude = 90
            distance = 30
            input = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 1, 0]).T
            output = np.array([0, 0]).T

            layers = [input.size, output.size]

            if flag2==0:
                brain = neural_network.crossover(fittest[0][0].brain, fittest[1][0].brain)
            elif flag2==1:
                brain = neural_network.crossover(fittest[1][0].brain, neural_network.initialize((input.size, 3, output.size))[1])
            elif flag2==2:
                brain = neural_network.crossover(fittest[0][0].brain, neural_network.initialize((input.size, 3, output.size))[1])
            elif flag2==3:
                brain = neural_network.crossover(neural_network.initialize((input.size, 3, output.size))[1], neural_network.initialize((input.size, 3, output.size))[1])

            #synapses = load.synapses(1)
            neural_network.mutation(brain, 0.80)

            population.append( Fish(name, age, pos, angle, size, health, hunger, amplitude, distance, input, output, layers, brain))


        for food in foods:
            graphics.draw_food(gameDisplay, food, 1)

        for fish in population:
            graphics.draw_fish(gameDisplay, fish.pos, fish.size)

            fish.output = neural_network.calculate(fish.input, fish.brain)

            movement.next_pos(world, fish, 1.0/fps)

            interaction.vision2(world, fish)

            graphics.draw_line(gameDisplay, fish.pos, [fish.pos[0]+fish.distance*math.cos(math.radians(fish.angle-fish.amplitude/2.0)), fish.pos[1]+fish.distance*math.sin((math.radians(fish.angle-fish.amplitude/2.0)))])

            graphics.draw_line(gameDisplay, fish.pos, [fish.pos[0]+fish.distance*math.cos(math.radians(fish.angle+fish.amplitude/2.0)), fish.pos[1]+fish.distance*math.sin((math.radians(fish.angle+fish.amplitude/2.0)))])

            interaction.eat(world, fish, foods)

            fish.aging(aging/fps)


        # Updates display
        graphics.update(fps*speed, clock)

        #raw_input()


    # Terminates Pygame
    graphics.close_display()
    # Terminates Python
    quit()



main()
