
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:    
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"

import random
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        if isinstance(viking, Viking):
            self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        if isinstance(saxon, Saxon):
            self.saxonArmy.append(saxon)

    def vikingAttack(self): 
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        saxon_damage = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return f"A Saxon has died in combat"
        else:
            return saxon_damage

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        viking_damage = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        else:
            return viking_damage
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."


        
    
