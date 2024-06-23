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
        return f"Name: {self.get_name()} \n Life: {self.get_life()} \n Level: {self.get_level()}"
    
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

        message = f"{self.get_name} attacked {target.get_name}, taking {damage} damage points!"
        print(message)

class Hero(Character):
    def __init__(self, name, life, level, power) -> None:
        super().__init__(name, life, level)
        self.__power = power

    def get_power(self):
        return self.__power
    
    def get_details(self):
        return f"{super().get_details()} \nPower: {self.get_power}"
    
    def special_attack(self, target):
        level = self.get_level()
        
        min_damage = level * 5
        max_damage = level * 8

        damage = random.randint(min_damage, max_damage)
        target.get_attacked(damage)

        message = f"{self.get_name} special attacked {target.get_name}, taking {damage} damage points!"
        print(message)


class Enemy(Character):
    def __init__(self, name, life, level, type) -> None:
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def get_details(self):
        return f"{super().get_details()} \nType: {self.get_type}"
    
