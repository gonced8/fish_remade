class World (object):

    # This function initializes an empty world M by N
    def __init__(self, m, n):
        self.world = []
        for line in range(m):
            self.world.append([])
            for column in range(n):
                self.world[line].append([])

    # Prints a more beautiful version of world
    def show(self):
        for row in self.world:
            print(row)

    # Returns [M,N] in which M is the number of rows in world and N is the number of columns
    def size(self):
        return [len(self.world), len(self.world[0])]

    # Inserts an object in a chosen position [i,j].
    def insert(self, pos, obj):
        self.world[pos[0]][pos[1]].append(obj)

    # Removes any object from given position [i,j].
    def remove(self, pos):
        self.world[pos[0]][pos[1]] = []

    # Returns True if given position [i,j] in world is free and returns False if not.
    def free_pos(self, pos):

        if pos[0]<0 or pos[0]>=len(self.world) or pos[1]<0 or pos[1]>=len(self.world[0]):
            return True

        return self.world[pos[0]][pos[1]] == []

    # Returns the name of what's in the position [pos].
    def what_in(self, pos):
        return self.world[pos[0]][pos[1]]

    # Show world the way it's implemented
    def show2(self):
        return self.world
