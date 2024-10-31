import random

class TreasureKey:
    def __init__(self):
        pass
    
class Pirate:
    def __init__(self, name, key:TreasureKey):
        self.name = name
        self.key = key
        
        
class Treasure:
    def __init__(self, _secret_treasure, _secret_treasure_key:TreasureKey):
        self._secret_treasure = _secret_treasure
        self._secret_treasure_key = _secret_treasure_key
        
    def open_treasure_box(self, pirate):
        if pirate.key == self._secret_treasure_key:
            print(f"{pirate.name} öppnar skattkistan och finner: {self._secret_treasure}")
        else:
            print(f"{pirate.name} försöker öppna.. Klick klick klick..")
        
        
key1 = TreasureKey()
key2 = TreasureKey()
key3 = TreasureKey()
key4 = TreasureKey()

keys = [key1, key2, key3, key4]


random_key = random.choice(keys)

secret_treasure = "En skatt full av guld"
treasure = Treasure(secret_treasure, random_key)



pirate_1 = Pirate("Blackbeard", key1)
pirate_2 = Pirate("Redbeard", key2)
pirate_3 = Pirate("Greenbeard", key3)
pirate_4 = Pirate("Pinkbeard", key4)


pirates = [pirate_1, pirate_2, pirate_3, pirate_4]


for pirate in pirates:
    treasure.open_treasure_box(pirate)