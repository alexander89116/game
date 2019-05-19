from data_for_server import *


class Building:
    def __init__(self, name, data):
        self.lvl = 1
        self.name = name
        self.data = data

    def update(self, city):
        if self.lvl >= len(self.data):
            return '{} max level'.format(self.name)

        if not city.check_resources(self.data[self.lvl]):
            return 'Not enough resources'

        if not city.check_population(self.data[self.lvl]['pop']):
            return 'Not enough population'

        city.update(self.data[self.lvl])
        self.lvl += 1
        return 'OK'

    def watch(self):
        return '\nBuilding: {}\nLevel: {}\nOutput per hour: {}\nUpdate: wood - {} stone - {} silver - {} population - {} new_output - {}\n'.format(
            self.name, self.lvl, self.data[self.lvl - 1]['output'] * GAME_SPEED, self.data[self.lvl]['wood'],
            self.data[self.lvl]['stone'], self.data[self.lvl]['silver'], self.data[self.lvl]['pop'],
                                 self.data[self.lvl]['output'] * GAME_SPEED)


class Farm(Building):
    def __init__(self):
        super().__init__('Farm', FARM_LVL)

    def update(self, city):
        res = super().update(city)
        if res == 'OK':
            city.population += self.data[self.lvl - 1]['delta']
        return res

    def watch(self):
        return '\nBuilding: {}\nLevel: {}\nMax_population: {}\nUpdate: wood - {} stone - {} silver - {} new_max_population - {}\n'.format(
            self.name, self.lvl, self.data[self.lvl - 1]['max_population'], self.data[self.lvl]['wood'],
            self.data[self.lvl]['stone'], self.data[self.lvl]['silver'],
            self.data[self.lvl]['max_population'])


class Sawmill(Building):
    def __init__(self):
        super().__init__('Sawmill', SAWMILL_LVL)


class Quarry(Building):
    def __init__(self):
        super().__init__('Quarry', QUARRY_LVL)


class Mine(Building):
    def __init__(self):
        super().__init__('Mine', MINE_LVL)


class Warehouse(Building):
    def __init__(self):
        super().__init__('Warehouse', WAREHOUSE_LVL)

    def watch(self):
        return '\nBuilding: {}\nLevel: {}\nStorage: {}\nStash: {}\nUpdate: wood - {} stone - {} silver - {} population - {} new_storage - {} new_stash - {}\n'.format(
            self.name, self.lvl, int(self.data[self.lvl - 1]['storage'] / 3), self.data[self.lvl - 1]['stash'],
            self.data[self.lvl]['wood'],
            self.data[self.lvl]['stone'], self.data[self.lvl]['silver'], self.data[self.lvl]['pop'],
            int(self.data[self.lvl]['storage'] / 3),
            self.data[self.lvl]['stash'])


class Wall(Building):
    def __init__(self):
        super().__init__('Wall', WALL_LVL)

    def watch(self):
        return '\nBuilding: {}\nLevel: {}\nDefence bonus: {}%\nUpdate: wood - {} stone - {} silver - {} population - {} new_bonus - {}\n'.format(
            self.name, self.lvl, self.data[self.lvl - 1]['bonus'] / 100, self.data[self.lvl]['wood'],
            self.data[self.lvl]['stone'], self.data[self.lvl]['silver'], self.data[self.lvl]['pop'],
            self.data[self.lvl]['bonus'])


BUILDINGS_CLASS = [Farm, Warehouse, Sawmill, Quarry, Mine, Wall]

BUILDINGS_NAME = ['Farm', 'Warehouse', 'Sawmill', 'Quarry', 'Mine', 'Wall']
