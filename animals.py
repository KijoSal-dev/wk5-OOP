class Animal:
    """
    Base class for animals.  Defines a default 'move' method.
    """
    def __init__(self, name):
        self.name = name

    def move(self):
        """
        Prints a default message about moving.  This will be overridden by subclasses.
        """
        print(f"{self.name} moves in a generic way.")


class Dog(Animal):
    """
    Represents a dog.
    """
    def move(self):
        """
        Prints a message indicating the dog is running.  Overrides the base class's move method.
        """
        print(f"{self.name} is running.")


class Fish(Animal):
    """
    Represents a fish.
    """
    def move(self):
        """
        Prints a message indicating the fish is swimming.  Overrides the base class's move method.
        """
        print(f"{self.name} is swimming.")


class Bird(Animal):
    """
    Represents a bird.
    """
    def move(self):
        """
        Prints a message indicating the bird is flying.  Overrides the base class's move method.
        """
        print(f"{self.name} is flying.")


# Create a list of animals
animals = [Dog("Scooby Doo"), Fish("Flounder"), Bird("Woody Woodpecker"), Animal("Generic Animal")]

# Iterate through the list and call the move() method on each animal
for animal in animals:
    animal.move()  # Polymorphism in action! The correct move() method is called based on the object type.