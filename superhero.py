# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I have the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with polymorphism
class TechHero(Superhero):
    def __init__(self, name, origin, gadget):
        super().__init__(name, "Technology", origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} hacks into the system using their {self.gadget}!")

class MagicHero(Superhero):
    def __init__(self, name, origin, spell):
        super().__init__(name, "Magic", origin)
        self.spell = spell

    def use_power(self):
        print(f"{self.name} casts a powerful spell: {self.spell} ✨")

class Speedster(Superhero):
    def __init__(self, name, origin, speed):
        super().__init__(name, "Speed", origin)
        self.speed = speed

    def use_power(self):
        print(f"{self.name} uses super speed to to overwhelm bad guys: {self.speed}!")        

class Supernatural(Superhero):
    def __init__(self, name, origin, supernatural):
        super().__init__(name, "Supernatural", origin)
        self.supernatural = supernatural

    def use_power(self):
        print(f"{self.name} has powers from beyond this world seeking to bring justice and is known to riding a motorcycle referred to as Hell cycle: {self.supernatural}!")
       

hero1 = TechHero("ByteMan", "Neo-Tokyo", "Quantum Laptop")
hero2 = MagicHero("Mystica", "Enchanted Forest", "Firestorm")
hero3 = Speedster("Flash", "United States", "superspeed")
hero4 = Supernatural("Ghost rider", "Sarka", "Vigilantee")


hero1.introduce()
hero1.use_power()


hero2.introduce()
hero2.use_power()

hero3.introduce()
hero3.use_power()

hero4.introduce()
hero4.use_power()