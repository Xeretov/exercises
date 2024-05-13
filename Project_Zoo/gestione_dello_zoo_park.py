'''
This module provides some classes and functions that are needed to manage a virtual zoo

Classes:
    Animal: represents an animal with a name, species, age, height, width, preferred_habitat and health
    Fence: represents an enclusure with a list of Animal, area, temperature and habitat
    ZooKeeper: represents a zookeeper with a name, surname and an id
    Zoo: represents a zoo with a list of Fence and a list of ZooKeeper

Functions:
    Fence.is_available: checks if an animal can be put in the fence
    ZooKeeper.add_animal: adds an animal to an enclusure
    ZooKeeper.remove_animal: remove an animal from an enclusure
    ZooKeeper.feed: feed an animal (increases health and size)
    ZooKeeper.clean: returns a float with the time needed to clean a fence
    Zoo.describe_zoo: shows every information inside of the zoo. (Zookeepers, fences and animals)
'''
# Gioele Amendola
# 13/05/2024

# Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

class Animal:

    def __init__(self, name: str, species: str, age: int, measure: tuple[float,float], preferred_habitat: str) -> None:
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = measure[0]
        self.width: float = measure[1]
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)

class Fence:

    def __init__(self, area: float, temperature: float, habitat: str, animals: list[Animal] = []) -> None:
        self.animals: list[Animal] = animals[:]
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat

    def is_available(self, add_animal: Animal, feed: bool = False) -> bool:
        '''
        This method checks if the animal can be contained inside the fence.

        Args:
            add_animal(Animal): the animal to add to the fence.
            feed(bool)(optional): if the animal is being fed. Defaults to False.
        
        Returns:
            bool: if there is availabe area in the fence.
        '''
        available = self.area - sum(animal.width*animal.height for animal in self.animals if self.animals)
        if feed:
            return True if available-(add_animal.width*add_animal.height + (add_animal.width*2/100)*(add_animal.height*2/100)) > 0 else False
        return True if available-add_animal.width*add_animal.height > 0 else False

class ZooKeeper:

    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
    
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        '''
        This method adds an animal to a specified fence.
        
        Args:
            animal(Animal): the animal to add in the fence.
            fence(Fence): the fence that the animal needs to be added to.
        '''
        if fence.habitat == animal.preferred_habitat:
            if fence.is_available(animal):
                fence.animals.append(animal)
            else:
                print("The animal cannot be contained in the specified fence.")
        else:
            print("The animal's preferred habitat is not the same as the fence's.")

    def remove_animal(self, remove_animal: Animal, fence: Fence) -> None:
        '''
        This method removes an animal from a specified fence.

        Args:
            animal(Animal): the animal to remove from the fence.
            fence(Fence): the fence where the animal is in and need to be removed from.
        '''
        animals: list = fence.animals
        animals_names: list = [animal.name for animal in animals]
        if animals:
            if remove_animal.name in animals_names:
                index: int = animals_names.index(remove_animal.name)
                del animals[index]
            else:
                print("There is no animal in the fence that resambles the animal to remove.")
        else:
            print("The fence is empty.")
    
    def feed(self, feed_animal: Animal, fence: Fence) -> None:
        '''
        This method feeds an animal.

        Args:
            feed_animal(Animal): animal to feed.
            fence(Fence): fence of the animal.
        '''
        animals: list = fence.animals
        animals_names: list = [animal.name for animal in animals]
        if animals:
            if feed_animal.name in animals_names:
                if fence.is_available(feed_animal, feed=True):
                    feed_animal.width += feed_animal.width*2/100
                    feed_animal.height += feed_animal.height*2/100
                    feed_animal.health += feed_animal.health/100
                else:
                    print("The animal is too big to be fed.")
            else:
                print("There is no animal in the fence that resables the animal to feed.")
        else:
            print("The fence is empty.")
    
    def clean(self, fence: Fence) -> float:
        '''
        This method returns the time that the zookeper needs to clean the enclusure

        Args:
            fence(Fence): fence to clean.
        '''
        animals: list = fence.animals
        occupied: int = sum(animal.width*animal.height for animal in animals)
        available: int = fence.area - occupied
        time: float = occupied if available == 0 else occupied/available
        return time

class Zoo:

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers

    def describe_zoo(self) -> None:
        '''This method shows every information about the zookeepers, the fences and the animals'''
        print("\nGuardians:")
        for keeper in self.zoo_keepers:
            print(f"\nZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})")
        print("\nFences:")
        for fence in self.fences:
            print(f"\nFence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            print("\nwith animals:\n")
            for animal in fence.animals:
                print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})",end="\n\n")
            print("#"*30)


animal1: Animal = Animal("Harambe", "Western Gorilla", 17, (210.64,50.24), "Tropical")
animal2: Animal = Animal("Fiona", "Common Hippopotamus", 20, (160.25,120.89), "Savannah")
animal3: Animal = Animal("Diego", "Aldabra giant tortoise", 90, (80.3,128.22), "Tropical")
animal4: Animal = Animal("Winter", "Dolphin", 28, (20,190.2), "Lurk warm Sea")
animal5: Animal = Animal("Pingu", "Emperor penguin", 8, (50.24,18.33), "Antartica")