from gestione_dello_zoo_park import *
# Example Test:
animal1: Animal = Animal("Harambe", "Western Gorilla", 17, 2.1, 0.5, "Tropical")
animal2: Animal = Animal("Fiona", "Common Hippopotamus", 20, 1.6, 1.2, "Savannah")
animal3: Animal = Animal("Diego", "Aldabra giant tortoise", 90, 0.8, 1.2, "Tropical")
animal4: Animal = Animal("Winter", "Hourglass Dolphin", 28, 0.2, 1.9, "Antarctic")
animal5: Animal = Animal("Pingu", "Emperor penguin", 8, 0.5, 0.18, "Antarctic")

animal_list = [animal1, animal2, animal3]

fence1: Fence = Fence(10000, 24, "Tropical", animal_list)
fence2: Fence = Fence(50000, -10, "Antarctic")

fence_list = [fence1,fence2]

zookeeper1: ZooKeeper = ZooKeeper("Giacomo","Belli","120D58A")
zookeeper2: ZooKeeper = ZooKeeper("Liliana","Fortuna","3982BL4")
zookeeper3: ZooKeeper = ZooKeeper("Priscilla","Perlana","032AA27")

zookeeper_list = [zookeeper1,zookeeper2,zookeeper3]

zoo1: Zoo = Zoo(fence_list, zookeeper_list)

zoo1.describe_zoo()

zookeeper1.add_animal(animal4, fence2)
zookeeper1.add_animal(animal2, fence2)
zookeeper1.remove_animal(animal1, fence1)
zookeeper1.remove_animal(animal5, fence2)
zookeeper1.add_animal(animal5, fence2)

zoo1.describe_zoo()

zookeeper2.feed(animal5)
for _ in range(10):
    zookeeper2.feed(animal3)

print(f"{zookeeper3.clean(fence2)}")
print(f"{zookeeper3.clean(fence1)}")