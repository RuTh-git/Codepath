class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        #new_catchphrase = new_catchphrase.replace(" ", "")
        if new_catchphrase.replace(" ", "").isalpha():
            if len(new_catchphrase) < 20:
                self.catchphrase = new_catchphrase 
                print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")


alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
