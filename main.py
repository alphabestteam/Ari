from monster import Monster
from hero import Hero


def choose_action():
    return input(
        "Enter what you wanna do: 1 - attack , 2 - level up, 3 - heal, 4 - defend\n"
    )


def main():
    hero = Hero("Ari")
    monster = Monster("HEN", hero.level)
    attack = hero

    while hero.hp > 0:
        user_choice = choose_action()
        hero.increase_coins(1)

        if user_choice == "1":
            hero.attack(monster)
            print(f"Attack, monster life - {monster.hp}, your coins - {hero.coins}")
            monster.attack(hero)
            print(f"The monster attack you, your life - {hero.hp}")
            if monster.hp <= 0:
                monster = Monster("HEN", hero.level)
                print(f"A new monster was created with {monster.hp} hp")

        elif user_choice == "2":
            hero.level_up()
            monster.attack(hero)
            print(
                f"The monster {monster.name_of_monster} attack you, your life: {hero.hp} "
            )

        elif user_choice == "3":
            hero.heal()
            print(f"Heal, your life is: {hero.hp} your coins - {hero.coins}")
            monster.attack(hero)
            print(
                f"The monster {monster.name_of_monster} attack you, your life - {hero.hp} "
            )

        elif user_choice == "4":
            print(
                f"Defend, next time the monster will hurt you it will be 80% less, your coins - {hero.coins}"
            )
            hero.defend(monster)
            monster.attack(hero)
            print(
                f"The monster {monster.name_of_monster} attack you, your life: {hero.hp} your coins - {hero.coins}"
            )

        else:
            print("Pleas enter a number between 1 - 4")
    print("You dead, it was pleasure to play with you!")


if __name__ == "__main__":
    main()
