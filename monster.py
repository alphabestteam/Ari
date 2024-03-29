import random


class Monster:
    proportion = 0.90

    def __init__(self, name_of_monster, hero_level):
        self._name = name_of_monster
        self._level = random.randint(hero_level - 1, hero_level + 1)
        self._hp = int(self._level * self.proportion + 1)
        self._damage = int(self._level * self.proportion + 1)

    def attack(self, hero):
        hero.reduce_health(self)

    def reduce_health(self, hero):
        self.hp -= hero.damage
        if self.hp - hero.damage < 0:
            self.hp = 0

    @property
    def name_of_monster(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def damage(self):
        return self._damage

    @property
    def level(self):
        return self._level

    @name_of_monster.setter
    def name_of_hero(self, new_name_of_monster: str):
        self._name_of_hero = new_name_of_monster

    @hp.setter
    def hp(self, new_hp: int):
        self._hp = new_hp

    @damage.setter
    def damage(self, new_damage: int):
        self._damage = new_damage

    @level.setter
    def level(self, new_level: int):
        self._level = new_level
