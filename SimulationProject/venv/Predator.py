class Predator:
    # parameters that are common to the movement of all the preys: speed, field of view (angle), position(x,y,z?)
    # direction of movement(two angles [if we use 3d], gamma and phi?)
    speed = 10  # TODO
    field = 20  # TODO
    pos_x = 0
    pos_y = 0
    pos_z = 0
    gamma = 0 #angle for x-y plane
    phi = 0 #angle for x-y plane

    def locatePrey(self):
        return self
        # Locate prey, just added it so we have some kind of structure
