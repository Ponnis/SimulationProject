class Prey:
    # Code for prey goes here
    # parameters that are common to all the preys: speed, field of vision (angle), position(x,y,z?)
    # direction of movement(two angles [if we use 3d], gamma and phi?)
    speed = 10  # TODO
    field = 20  # TODO
    pos_x = 0
    pos_y = 0
    pos_z = 0
    gamma = 0 #angle for x-y plane
    phi = 0 #angle for x-y plane

    def checkForCollision(self):
        return self
# collision checker for the future, don't mind it for now
