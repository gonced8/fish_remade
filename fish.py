class Fish(object):

    def __init__(self, name, age, pos, angle, size, health, hunger, amplitude, distance, input, output, layers, brain):
        self.name = name
        self.age = age
        self.pos = pos
        self.angle = angle
        self.size = size
        self.health = health
        self.hunger = hunger
        self.amplitude = amplitude
        self.distance = distance
        self.input = input
        self.output = output
        self.layers = layers
        self.brain = brain

    def show(self):
        print("Name: {0} \n Age: {1} \n Position: {2} \n Angle: {3} \n Size: {4} \n Health: {5} \n Hunger: {6} \n Amplitude: {7} \n Distance: {8} \n Input: {9} \n Output: {10} \n Layers: {11} \n brain: {12} \n".format(
            self.name, self. age, self.pos, self.angle, self.size, self.health, self.hunger, self.amplitude, self.distance, self.input, self.output, self.layers, self.brain))


    def aging (fish, dt, t_age=1, t_hunger=0.1, t_health=0.1):

        fish.age += t_age*dt

        if fish.health == 0:
            return False    # Return False to kill the fish

        if fish.hunger == 1:
            fish.health -= t_hunger * dt

            if fish.health < 0:
                fish.health = 0

        else:
            fish.hunger += t_hunger*dt

            if fish.hunger > 1:
                fish.hunger = 1

            if fish.health < 1:
                fish.health += t_health*dt

                if fish.health > 1:
                    fish.health = 1

        fish.input[13] = fish.hunger
        fish.input[14] = fish.health

        return True
