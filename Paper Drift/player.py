import math
class Player:
    def __init__(self, startX, startY, dir, Xvel, Yvel):
        self.Xvel = Xvel
        self.Yvel = Yvel
        self.x = startX
        self.y = startY
        self.dir = dir
    
    def move(self, amount):
        rad = math.radians(self.dir)
        dx = amount * math.cos(rad)
        dy = amount * math.sin(rad)

        self.Xvel += dx
        self.Yvel += dy
    
    def turn(self, mouseX, mouseY):
        dx = mouseX - self.x
        dy = mouseY - self.y

        angle_rad = math.atan2(dy, dx)
        angle_degrees = math.degrees(angle_rad)
        self.dir = angle_degrees
        return self.dir
