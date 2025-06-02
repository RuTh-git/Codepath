'''
Problem 1: New Horizons

Instance of class
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

'''
Problem 2: Greet Player, Problem 3: Update Catchphrase

Method in OOPS
'''

bones = Villager("Bones", "Dog", "yip yip")
bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))

print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 

'''
Problem 4: Set Character, Problem 5: Add Furniture, Problem 6: Print Inventory, Problem 7: Group by Personality, Problem 8: Telephone

Setter methods (instead of updating catchphrase as earlier)
'''
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")
    
    def add_item(self, item_name):
        valid_furniture = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_furniture:
            self.furniture.append(item_name)
    
    def print_inventory(self):
        if not self.furniture:
            print("Inventory empty")
        else:
            count_furniture = {}
            for i in self.furniture:
                if i in count_furniture:
                    count_furniture[i] += 1
                else:
                    count_furniture[i] = 1

            '''res = []
            for k, c in count_furniture.items():
                res.append(f"{k}: {c}")
            output = ", ".join(res)
            print(output)'''

            inventory_output = ", ".join([f"{item}: {count}" for item, count in count_furniture.items()])
            print(inventory_output)

def of_personality_type(townies, personality_type):
    res = []
    for i in townies:
        if i.personality == personality_type:
            res.append(i.name)
    return res

def message_received(start_villager, target_villager):
    current = start_villager
    while current is not None:
        if current == target_villager:
            return True
        current = current.neighbor
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

'''isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
'''
'''alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

'''

'''
Problem 9: Nook's Cranny, Problem 10: Timmy and Tommy, Problem 11: Saharah
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 

timmy = Node("Timmy", tommy)
tom_nook.next = timmy

tom_nook.next = None
saharah = Node("Saharah")
tommy.next = saharah

#print(tom_nook.value) 
#print(tom_nook.next.value) 
print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 

'''
Problem 12: Print List
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(head):
    res = []
    current = head
    while current:
        res.append(current.value)
        current = current.next
    return " -> ".join(res)


isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))