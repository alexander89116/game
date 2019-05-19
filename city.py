from building import *
from unit import *
import time


class Greek_civilization:
    def __init__(self):
        self.data = {}
        self.cities = {}
        self.active = {}
        self.messages = {}

    def check_new_login(self, login):
        if login in self.data.keys():
            return 'This login is already taken'
        else:
            return 'True'

    def new_user(self, login, password):
        check = self.check_new_login(login)
        if self.check_new_login(login) == 'True':
            self.data[login] = password
            self.active[login] = City(owner=login)
            self.cities[login] = {'New York': self.active[login]}
            self.messages[login] = []
            return 'OK'
        else:
            return check

    def try_login(self, login, password):
        if login not in self.data.keys():
            return 'Wrong login'
        elif self.data[login] == password:
            return 'OK'
        else:
            return 'Wrong password'

    def watch_info(self, login):
        ans = []
        for name in self.cities[login].keys():
            ans.append(name)
        return 'You have some cities:\n{}'.format(ans)

    def watch_cities(self, login):
        if login not in self.data.keys():
            return 'Player {} does not exist'.format(login)
        ans = []
        for name in self.cities[login].keys():
            ans.append(name)
        return 'Player {} has some cities:\n{}'.format(login, ans)

    def watch_players(self):
        ans = []
        for name in self.data.keys():
            ans.append(name)
        return 'Players in game:\n{}'.format(ans)

    def view_messages(self, login):
        res = ''.join('\nMessage {}: {}'.format(num + 1, message) for num, message in enumerate(self.messages[login]))
        if len(res) == 0:
            return 'You have no unread messages'
        else:
            self.messages[login].clear()
            return res

    def send_message(self, login, text):
        self.messages[login].append(text)
        return 'OK'

    def rename_city(self, login, new_name):
        if new_name in self.cities[login].keys():
            return 'You already have a city with that name'
        self.active[login].name = new_name
        return 'OK'

    def create_city(self, login, name):
        if name in self.cities[login].keys():
            return 'You already have a city with that name'
        elif not self.active[login].check_resources({name: PRICE_NEW_CITY for name in RESOURCE_NAME}):
            return 'Not enough resources, you need {} of each type'.format(PRICE_NEW_CITY)
        elif not self.active[login].check_population(POPULATION_NEW_CITY):
            return 'Not enough population, you need {}'.format(POPULATION_NEW_CITY)
        else:
            self.cities[login][name] = City(name)
            self.active[login] = self.cities[login][name]
            return 'You create {}'.format(name)

    def change_city(self, login, name):
        if name not in self.cities[login].keys():
            return 'You haven\'t a city with that name'
        else:
            self.active[login] = self.cities[login][name]
            return 'Your active city is {}'.format(name)

    def send_army(self, login, other_login, name, army):
        cnt = army.split('_')
        if len(cnt) != len(UNITS_NAME):
            return 'Uncorrect format army'
        if other_login not in self.data.keys():
            return 'Player {} does not exist'.format(other_login)
        if name not in self.cities[other_login]:
            return 'Player {} has no city {}'.format(other_login, name)
        army = Army(count=cnt, owner=login)
        ans = self.active[login].send_army(army, self.cities[other_login][name])
        if ans[0] != 'OK':
            return ans[0]
        elif ans[1] == 'Win':
            res = 'Your army lost the atack from {}:{}'.format(login, self.active[login].name) + ans[
                3] + 'Your city lost:\nWood: {} Stone: {} Silver: {}'.format(int(army.wood), int(army.stone),
                                                                             int(army.silver))
            ans = 'Your army win the atack to {}:{}\n{}\nWood: {} Stone: {} Silver: {}'.format(other_login, name,
                                                                                               ans[2], int(army.wood),
                                                                                               int(army.stone),
                                                                                               int(army.silver))
            self.active[login].back_army(army)
            self.messages[other_login].append(res)
            return ans

        else:
            self.messages[other_login].append(
                '\nYou survived the attack from {}:{}\n'.format(login, self.active[login].name) + ans[3])
            return 'Your army lost the to {}:{}\n{}'.format(other_login, name, ans[2])


class City:
    def __init__(self, name='New York', owner='God'):
        self.buildings = {BUILDINGS_NAME[i]: BUILDINGS_CLASS[i]() for i in range(len(BUILDINGS_NAME))}
        self.army = Army(owner=owner)
        self.wood = 100
        self.silver = 100
        self.stone = 100
        self.population = FARM_LVL[0]['max_population']
        self.time = time.time()
        self.name = name
        self.owner = owner

    def check_population(self, pop):
        self.collect()
        return (self.population >= pop)

    def check_resources(self, mp):
        self.collect()
        return (self.wood >= mp['wood'] and self.stone >= mp['stone'] and self.silver >= mp[
            'silver'])

    def update(self, mp):
        self.collect()
        self.wood -= mp['wood']
        self.stone -= mp['stone']
        self.silver -= mp['silver']
        self.population -= mp['pop']

    def collect(self):
        tm = time.time()
        mx_storage = WAREHOUSE_LVL[self.buildings['Warehouse'].lvl]['storage'] / 3
        self.wood = min(self.wood + (tm - self.time) * SAWMILL_LVL[self.buildings['Sawmill'].lvl]['output'], mx_storage)
        self.stone = min(self.stone + (tm - self.time) * QUARRY_LVL[self.buildings['Quarry'].lvl]['output'], mx_storage)
        self.silver = min(self.silver + (tm - self.time) * MINE_LVL[self.buildings['Mine'].lvl]['output'], mx_storage)
        self.time = tm

    def update_building(self, type):
        self.collect()
        return self.buildings[type].update(self)

    def create_unit(self, type, count):
        self.collect()
        return self.army.units[type].increase(self, count)

    def watch_all(self):
        self.collect()
        res = []
        res.append(
            '\nYour city: {}\nWood: {} Stone: {} Silver: {}\nFree population: {}\n'.format(self.name, int(self.wood),
                                                                                           int(self.stone),
                                                                                           int(self.silver),
                                                                                           self.population))
        for building in self.buildings.values():
            res.append(building.watch())
        res.append(self.army.watch())
        return ''.join(res)

    def watch_building(self, type):
        self.collect()
        return self.buildings[type].watch()

    def watch_info(self):
        self.collect()
        return '\nYour city: {}\nWood: {} Stone: {} Silver: {}\nFree population: {}\n'.format(self.name, int(self.wood),
                                                                                              int(self.stone),
                                                                                              int(self.silver),
                                                                                              self.population)

    def watch_army(self):
        self.collect()
        return self.army.watch()

    def defence(self, otherArmy: Army):
        self.collect()
        if self.army.getCount() == 0:
            self.rub(otherArmy)
            return ('OK', 'Win', '0', '0')
        dmgOff = (self.army.getDef() ** 1.2) * (otherArmy.getOff() ** -0.2)
        dmgDef = (self.army.getDef() ** -0.2) * (otherArmy.getOff() ** 1.2)
        offCnt = int(dmgOff / otherArmy.getOff() * otherArmy.getCount())
        defCnt = int(dmgDef / self.army.getDef() * self.army.getCount())
        winOff = False
        if self.army.getDef() < otherArmy.getOff():
            winOff = True
        a = otherArmy.kill(offCnt)
        b = self.army.kill(defCnt)
        self.population += defCnt
        if winOff:
            self.rub(otherArmy)
            return ('OK', 'Win', a, b)
        else:
            return ('OK', 'Lose', a, b)

    def rub(self, otherArmy):
        self.collect()
        stash = self.buildings['Warehouse'].data[self.buildings['Warehouse'].lvl - 1]['stash']
        loot = otherArmy.getLoot()
        lootCnt = 0
        for i in [3, 2, 1]:
            if self.wood - stash > 0:
                if self.wood - stash < loot / i:
                    lootCnt += self.wood - stash
                    otherArmy.wood += self.wood - stash
                    self.wood = stash
                else:
                    lootCnt += loot / i
                    otherArmy.wood += loot / i
                    self.wood -= loot / i
            if self.stone - stash > 0:
                if self.stone - stash < loot / i:
                    lootCnt += self.stone - stash
                    otherArmy.stone += self.stone - stash
                    self.stone = stash
                else:
                    lootCnt += loot / i
                    otherArmy.stone += loot / i
                    self.stone -= loot / i
            if self.silver - stash > 0:
                if self.silver - stash < loot / i:
                    lootCnt += self.silver - stash
                    otherArmy.silver += self.silver - stash
                    self.silver = stash
                else:
                    lootCnt += loot / i
                    otherArmy.silver += loot / i
                    self.silver -= loot / i
            loot -= lootCnt
            lootCnt = 0

    def send_army(self, army, city):
        check = self.army.check(army)
        if check != 'OK':
            return (check, 0, 0, 0)
        self.army.divide(army)
        return city.defence(army)

    def back_army(self, army):
        self.army.join(army)
        self.wood += army.wood
        self.stone += army.stone
        self.silver += army.silver
        self.army.wood = 0
        self.army.stone = 0
        self.army.silver = 0
        self.population += army.pop

