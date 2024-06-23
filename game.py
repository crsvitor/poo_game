import random

class Character:
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def get_details(self):
        return f"Name: {self.get_name()} \nLife: {self.get_life()} \nLevel: {self.get_level()}"
    
    def get_attacked(self, damage):
        self.__life -= damage

        if damage < 0:
            damage = 0

    def attack(self, target):
        level = self.get_level()
        
        min_damage = level * 2
        max_damage = level * 4

        damage = random.randint(min_damage, max_damage)
        target.get_attacked(damage)

        message = f"{self.get_name()} attacked {target.get_name()}, taking {damage} damage points!"
        print(message)

class Hero(Character):
    def __init__(self, name, life, level, power) -> None:
        super().__init__(name, life, level)
        self.__power = power

    def get_power(self):
        return self.__power
    
    def get_details(self):
        return f"{super().get_details()} \nPower: {self.get_power()}\n"
    
    def special_attack(self, target):
        level = self.get_level()
        
        min_damage = level * 5
        max_damage = level * 8

        damage = random.randint(min_damage, max_damage)
        target.get_attacked(damage)

        message = f"{self.get_name()} special attacked {target.get_name()}, taking {damage} damage points!"
        print(message)


class Enemy(Character):
    def __init__(self, name, life, level, type) -> None:
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def get_details(self):
        return f"{super().get_details()} \nType: {self.get_type()}\n"
    
class Game:
    def __init__(self) -> None:
        self.__hero = Hero(name="Hero", life=100, level=5, power="Super strength")
        self.__enemy = Enemy(name="Bat", life=50, level=5, type="Flying")

    def start_battle(self):
        while self.__hero.get_life() > 0 and self.__enemy.get_life() > 0:
            print("\nCharacters:")
            print(self.__hero.get_details())
            print(self.__enemy.get_details())

            input("Press enter to attack... ")
            choice = int(input("Choose (1 - normal attack, 2 - special attack): "))

            if choice == 1:
                self.__hero.attack(self.__enemy)
            elif choice == 2:
                self.__hero.special_attack(self.__enemy)
            else:
                print("Invalid choice, select again.")

            if self.__hero.get_life() > 0:
                self.__enemy.attack(self.__hero)
            
        if self.__hero.get_life() > 0:
            print("\nCongratulations! You won the battle!")
        else:
            print("\nYou lost the battle!")

game = Game()
game.start_battle()
