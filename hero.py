from monster import Monster


class Hero:
    get_heal = 0.10
    get_damage_and_life = 0.20
    to_move_level = 2

    def __init__(self, name_of_hero):
        self._name = name_of_hero
        self._hp = int(10)
        self._damage = int(2)
        self._level = int(1)
        self._coins = int(0)
        self._max_hp = int(10)

    def heal(self):
        self.hp += self.hp * self.get_heal

    def level_up(self):
        if self.level + 1 * self.to_move_level <= self.coins:
            self.level += 1
            self.damage += self.damage * self.get_damage_and_life
            self.hp += self._hp * self.get_damage_and_life
            self.max_hp += self.hp * self.get_damage_and_life
            print(
                f"Level up, you move from level {self.level -1 } to level {self.level}, your life: {self.hp}, hero damage: {self.damage}"
            )
        else:
            print("You can't get level up if you don't have enough money")

    def attack(self, monster: Monster):
        monster.reduce_health(self)
        if monster.hp == 0:
            self.coins += self.level
            print(f"The monster dead so you get money and now your money {self.coins}")

    def defend(self, monster):
        self.hp -= monster.damage * 0.2

    def reduce_health(self, monster: Monster):
        self.hp -= monster.damage
        if self.hp - monster.damage < 0:
            self.hp = 0

    def increase_coins(self, coins):
        self.coins += coins

    @property
    def name_of_hero(self):
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

    @property
    def coins(self):
        return self._coins

    @property
    def max_hp(self):
        return self._max_hp

    # @name_of_hero.setter
    # def name_of_hero(self, new_name_of_hero: str):
    #     self._name_of_hero = new_name_of_hero

    @hp.setter
    def hp(self, new_hp: int):
        self._hp = new_hp

    @damage.setter
    def damage(self, new_damage: int):
        self._damage = new_damage

    @level.setter
    def level(self, new_level: int):
        self._level = new_level

    @coins.setter
    def coins(self, new_coins: int):
        self._coins = new_coins

    @max_hp.setter
    def max_hp(self, new_max_hp: int):
        self._max_hp = new_max_hp
