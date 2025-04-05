'''def total_treasures(treasure_map):
    return (sum(treasure_map.values()))
    

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) '''
'''
def can_trust_message(message):
    dict = {}

    for i in message:
        if i.isalpha() == False:
            continue
        elif i in dict:
            dict[i] += 1 
        else:
            dict[i] = 1 
    return len(dict) == 26

    

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))'''

def find_duplicate_chests(chests):
    dict = {}
    for i in chests:
        dict[i] = dict.get(i, 0) + 1 # puts the default count
    
    res = []
    for k, v in dict.items():
        if v > 1:
            res.append(k)
    return res


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))