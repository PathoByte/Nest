# Parent class

class Superhero:
    def __init__(self, name, power):
        self.name = name
        self._power = power 

    def use_power(self):
        return f"{self.name} uses {self._power}!"

# Child class

class Mindhero(Superhero):
    def __init__(self, name, power, mind_control_level):
        self.name = name
        self._power = power
        self.mind_control_level = mind_control_level

    # Polymorphism: changing how use_power works
    def use_power(self):
        return f"{self.name} uses {self._power} with {self.mind_control_level} mind control skills!"
    
# Creating objects

hero1 = Superhero("FlashLight", "super speed")
hero2 = Mindhero("EmmaFrost", "mind control", "master")


# Using methods

print(hero1.use_power())  
print(hero2.use_power())  
