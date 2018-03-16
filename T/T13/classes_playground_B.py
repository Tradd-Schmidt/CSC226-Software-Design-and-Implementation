class Animal:
    """
    A class representing an animal
    """
    def __init__(self, fur, love, color, speed, legs, height, weight, name, toys = []):
        """
        The initializer method, which sets attributes of the animal when its created
        :param fur: the type of fur the animal has
        :param love: the lovability of the animal
        :param color: the color of the animal
        :param speed: the speed of the animal
        :param legs: how many legs the animal has
        :param height: the height of the animal
        :param weight: the weight of the animal
        :param name: the name of the animal
        :param toys: a list of what toys the animal has
        """

        self.fur = fur
        self.lovability = love
        self.color = color
        self.speed = speed
        self.num_legs = legs
        self.height = height
        self.weight = weight
        self.toys = toys
        self.name = name
        print("New animal!")

    def run(self):
        """
        A method to make the animal run
        :return: None
        """
        print("Run away!")

    def eat(self):
        """
        A method to make the animal eat
        :return: None
        """
        print("Eat something")

    def reproduce(self, animal):
        """
        A method for allowing the animal to reproduce with another animal
        :param animal: an animal object for this animal to mate with
        :return: None
        """
        print("{1} mated with {0}".format(animal.name, self.name))


def main():
    dog = Animal("Fluffy", 0, "Purple", 7, 4, 18, 60, "Jack", ["bone", "ball", "rope"])

    print(dog.num_legs)
    print(dog.fur)
    dog.run()

    kingkong = Animal("matted", 10, "black", 9, 2, 150*12, 50*2000, "King Kong")
    print(kingkong.height)
    print(kingkong.weight)

    kingkong.reproduce(dog)         # poor Jack!


main()
