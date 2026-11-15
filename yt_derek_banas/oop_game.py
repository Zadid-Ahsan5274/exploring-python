import random
import math

class Warrior:
    def __init__(self,name="Warrior",health=0,attackMax=0,blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        attack_amount = self.attackMax * (random.random() + 0.5)
        return attack_amount

    def block(self):
        block_amount = self.blockMax * (random.random() + 0.5)
        return block_amount

class Battle:
    def start_fight(self,warrior1,warrior2):
        while True:
            if self.getAttackResult(warrior1,warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2,warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA,warriorB):
        warriorAAttackAmount = warriorA.attack()
        warriorBBlockAmount = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttackAmount - warriorBBlockAmount)
        warriorB.health = warriorB.health - damage2WarriorB
        print("{} attacks {} and deals {} damage".format(warriorA.name,warriorB.name,damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name,warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name,warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    maximus = Warrior("Maximus",50,20,10)
    galaxon = Warrior("Galaxon", 50, 20, 10)
    battle = Battle()
    battle.start_fight(maximus,galaxon)
main()
