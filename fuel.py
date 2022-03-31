from engine import *
class Fuel:
    def __init__(self,engine):
        self.engine=engine
        self.maxLevel = 1000
        self.level = self.maxLevel

    def update(self):
        self.level = self.level - abs(self.engine.get_speed()) * 0.01
        if self.level<0:
            self.level = 0

    def get_porcentage_level(self):
        return self.level*100/1000

    def reload(self):
        self.level = self.maxLevel

    def __str__(self):        
        return str(self.level)+ " L"

