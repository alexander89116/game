import random


class Unit:
    def __init__(self, name, wood, stone, silver, population, offence, defence, loot, speed, cnt=0):
        self.name = name
        self.offence = offence
        self.defence = defence
        self.data = {'wood': wood, 'stone': stone, 'silver': silver, 'pop': population}
        self.loot = loot
        self.speed = speed
        self.count = cnt

    def increase(self, city, delta=1):
        if not city.check_resources({name: count * delta for name, count in self.data.items()}):
            return 'Not enough resources'
        if not city.check_population(delta * self.data['pop']):
            return 'Not enough population'
        city.update({name: count * delta for name, count in self.data.items()})
        self.count += delta
        return 'OK'

    def decrease(self, delta=1):
        self.count -= delta
        if self.count < 0:
            self.count = 0


class Swordman(Unit):
    def __init__(self, count=0):
        super().__init__('Swordman', 95, 0, 85, 1, 5, 52, 16, 8, count)


class Slinger(Unit):
    def __init__(self, count=0):
        super().__init__('Slinger', 55, 100, 40, 1, 23, 17, 8, 14, count)


class Archer(Unit):
    def __init__(self, count=0):
        super().__init__('Archer', 120, 0, 75, 1, 8, 45, 24, 12, count)


class Horseman(Unit):
    def __init__(self, count=0):
        super().__init__('Hoseman', 240, 12, 360, 3, 60, 43, 72, 22, count)


class Chariot(Unit):
    def __init__(self, count=0):
        super().__init__('Chariot', 200, 440, 32, 4, 56, 148, 64, 18, count)


class Catapult(Unit):
    def __init__(self, count=0):
        super().__init__('Catapult', 700, 700, 700, 15, 100, 90, 400, 2, count)


UNITS_CLASS = [Swordman, Slinger, Archer, Horseman, Chariot, Catapult]

UNITS_NAME = ['Swordman', 'Slinger', 'Archer', 'Horseman', 'Chariot', 'Catapult']


class Army:
    def __init__(self, count=[0 for i in range(len(UNITS_CLASS))], isGrab=False, owner='God'):
        self.units = {UNITS_NAME[i]: UNITS_CLASS[i](int(count[i])) for i in range(len(UNITS_CLASS))}
        self.wood = 0
        self.stone = 0
        self.silver = 0
        self.pop = 0
        self.owner = owner

    def getOff(self):
        res = 0
        for unit in self.units.values():
            res += unit.offence * unit.count
        return res

    def getDef(self):
        res = 0
        for unit in self.units.values():
            res += unit.defence * unit.count
        return res

    def getCount(self):
        res = 0
        for unit in self.units.values():
            res += unit.count
        return res

    def getLoot(self):
        res = 0
        for unit in self.units.values():
            res += unit.count * unit.loot
        return res

    def getSpeed(self):
        res = 100
        cnt = self.getCount()
        for unit in self.units.values():
            if unit.count != 0:
                res = min(res, unit.speed)
        if cnt == 0:
            return 0
        return res

    def join(self, otherArmy):
        for name in UNITS_NAME:
            self.units[name].count += otherArmy.units[name].count
        self.wood += otherArmy.wood
        self.stone += otherArmy.stone
        self.silver += otherArmy.silver

    def divide(self, otherArmy):
        for name in UNITS_NAME:
            self.units[name].count -= otherArmy.units[name].count

    def check(self, otherArmy):
        for name in UNITS_NAME:
            if self.units[name].count < otherArmy.units[name].count:
                return 'You don\'t have so many units'
        return 'OK'

    def kill(self, count):
        killed = {UNITS_NAME[i]: 0 for i in range(len(UNITS_CLASS))}
        for i in range(count):
            name = random.choice(UNITS_NAME)
            while self.units[name].count == 0:
                name = random.choice(UNITS_NAME)
            killed[name] += 1
            self.units[name].decrease()
        self.pop += count
        return 'Your army lost:\n{}\n'.format(killed)

    def watch(self):
        return '\nYour army:\n' + ''.join('{}: {} '.format(name, unit.count) for name, unit in self.units.items())
