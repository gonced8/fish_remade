import math


def vision1():

    position=[0, 0]
    angle=45
    amplitude=90
    distance=20

    for j in range (-distance, distance):
        for i in range (-distance, distance):
            pos = [position[0]+i, position[1]+j]

            if math.cos(math.radians(angle+amplitude/2.0))*(j) <= math.sin(math.radians(angle+amplitude/2.0))*(i):

                if math.cos(math.radians(angle-amplitude/2.0))*(j) >= math.sin(math.radians(angle-amplitude/2.0))*(i):

                    if i**2+j**2<distance**2:

                        print("# ", end='', flush=True)
                        continue

            print("- ", end='', flush=True)

        print("\n", end='', flush=True)

                    

    return


def vision2():

    position=[0, 0]
    angle=360
    amplitude=90
    distance=20

    matrix=[["-" for y in range(1*distance)] for x in range(1*distance)]

    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print (matrix[i][j]+' ', end='', flush=True)
        print("\n", end='', flush=True)

    

vision1()
print()
vision2()
