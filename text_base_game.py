import random

# Constants
WEAPONS = ["sword", "axe", "bow", "dagger"]
MONSTERS = ["goblin", "troll", "dragon", "orc"]
LOCATIONS = ["forest", "cave", "castle", "village"]

# Helper functions
def get_random_element(lst):
    return random.choice(lst)

def generate_stat():
    return random.randint(1, 20)

# Class definitions
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.take_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {enemy.name} but it's not effective.")
    
    def __str__(self):
        return f"{self.name}: Health={self.health}, Attack={self.attack}, Defense={self.defense}"

class Player(Character):
    def __init__(self, name):
        super().__init__(name, generate_stat() + 20, generate_stat(), generate_stat())
        self.inventory = [get_random_element(WEAPONS)]
    
    def find_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} found a {item}!")

class Monster(Character):
    def __init__(self, name):
        super().__init__(name, generate_stat(), generate_stat(), generate_stat())

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.monsters = [Monster(get_random_element(MONSTERS)) for _ in range(5)]
        self.current_location = get_random_element(LOCATIONS)
    
    def start(self):
        print(f"Welcome, {self.player.name}, to the adventure game!")
        print(f"You are currently in the {self.current_location}.")
        while self.player.is_alive() and self.monsters:
            action = input("What do you want to do? (explore/fight/run): ")
            if action == "explore":
                self.explore()
            elif action == "fight":
                self.fight()
            elif action == "run":
                self.run()
            else:
                print("Invalid action. Please choose again.")
        if self.player.is_alive():
            print("Congratulations, you have defeated all the monsters!")
        else:
            print("Game over. You have been defeated.")

    def explore(self):
        print(f"{self.player.name} is exploring the {self.current_location}.")
        event = random.choice(["item", "monster", "nothing"])
        if event == "item":
            item = get_random_element(WEAPONS)
            self.player.find_item(item)
        elif event == "monster":
            if self.monsters:
                monster = self.monsters.pop()
                print(f"A wild {monster.name} appears!")
                self.fight_monster(monster)
            else:
                print("No more monsters to fight!")
        elif event == "nothing":
            print("You found nothing.")

    def fight(self):
        if self.monsters:
            monster = self.monsters.pop()
            print(f"A wild {monster.name} appears!")
            self.fight_monster(monster)
        else:
            print("No more monsters to fight!")

    def fight_monster(self, monster):
        while self.player.is_alive() and monster.is_alive():
            self.player.attack_enemy(monster)
            if monster.is_alive():
                monster.attack_enemy(self.player)
        if self.player.is_alive():
            print(f"{self.player.name} has defeated the {monster.name}!")
        else:
            print(f"{self.player.name} has been defeated by the {monster.name}!")

    def run(self):
        print(f"{self.player.name} is trying to run away...")
        success = random.choice([True, False])
        if success:
            print("You successfully ran away!")
        else:
            print("You failed to run away! Prepare to fight!")
            self.fight()

# Main function to start the game
def main():
    player_name = input("Enter your character's name: ")
    game = Game(player_name)
    game.start()

# Start the game
if __name__ == "__main__":
    main()
