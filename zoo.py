class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
    
    
class Zookeeper:
    def __init__(self, name):
        self.name = name
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)

    
    
class Zoo:
    def __init__(self):
        self.animals = []
        self.zookeepers = []
        
        
    def add_animal(self, animal):
        self.animals.append(animal)    
    
    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)
        
    
        
zoo = Zoo()



zelda_zebra = Animal("Zebra", "Zelda")
skrutt_kamel = Animal("Kamel", "Skrutt")
kakan_pingvin = Animal("Pingvin", "Kakan")
zelda_pingvin = Animal("Pingvin", "Zelda")
rex_lejon = Animal("Lejon", "Rex")


sebastian = Zookeeper("Sebastian")
stefan = Zookeeper("Stefan")
isabell = Zookeeper("Isabell")

zoo.add_animal(zelda_zebra)
zoo.add_animal(skrutt_kamel)
zoo.add_animal(kakan_pingvin)
zoo.add_animal(zelda_pingvin)
zoo.add_animal(rex_lejon)

zoo.add_zookeeper(sebastian)
zoo.add_zookeeper(stefan)
zoo.add_zookeeper(isabell)


sebastian.add_animal(zelda_zebra)
sebastian.add_animal(skrutt_kamel)
sebastian.add_animal(rex_lejon)

stefan.add_animal(kakan_pingvin)
stefan.add_animal(zelda_pingvin)
stefan.add_animal(rex_lejon)

isabell.add_animal(skrutt_kamel)
isabell.add_animal(kakan_pingvin)


print("Animals:\n")
for animal in zoo.animals:
    print(f"{animal.name} som är en {animal.species}")

print("\nZookeepers:\n")
for zookeeper in zoo.zookeepers:
    animal_list = ", ".join(
        [f"{animal.species}{'et' if animal.species == 'Lejon' else'en' if animal.species[-1] not in 'aeiou' else 'n'} {animal.name}" for animal in zookeeper.animals]
    )
    print(f"{zookeeper.name} som tar hand om [{animal_list}]")
