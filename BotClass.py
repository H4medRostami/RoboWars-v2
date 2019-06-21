import random
# used to damage calculate
import sys
# exit in game end.


class WarRobot:

    def __init__(self, name, en, attack, defense, speed, location):
        self.attack = attack
        self.name = name
        self.defense = defense
        self.speed = speed
        self._energy = 100
        self.location = location
        self.enemy = en
        self.is_great = True
        if self.enemy:
            if self.enemy.location > self.location:
                self.is_great = False
    # energy attribute getter
    @property
    def energy(self):
        return self._energy
    # energy attribute setter , also check robot Die.
    @energy.setter
    def energy(self, value):
        if not isinstance(value, int):
            raise TypeError('get only integer!')
        if value <= 0:
            print(self.name, ": *****************Game Over!***************** ")
            sys.exit()
        else:
            self._energy = value

    # get type of action 'move or shot' and calculate energy usage
    def _energy_calc(self, arg):
        distance = abs(self.location - self.enemy.location)
        if arg == 'move':
            result = (distance/self.speed)*5
            self.energy -= result

        elif arg == 'shot':
            result = (random.randint(1, 10) * self.attack / distance) - (self.enemy.defense * (distance / 10))
            if result < 0:
                result = 0
            self.enemy.energy -= result

    # Check if robots doesn't belong in same location and pass eachother then call energy_calc to calculate energy
    def move(self):
        temp = self.location
     
        if self.is_great:
            temp -= self.speed
        else:
            temp += self.speed
            
        if temp == self.enemy.location:
            return 'error same location'
        elif self.is_great and self.enemy.location > temp:
            return 'error invalid location'
        elif self.enemy.is_great and self.enemy.location < temp:
            return 'error invalid location'
        else:
            self.location = temp
            self._energy_calc('move')
            return ''

    # shot missile then calculate competitor energy
    def shot(self):
        self._energy_calc('shot')         


