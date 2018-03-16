class Car():
    """
    A class that represents a car
    """

    def __init__(self, make, model, color, year, location, engine, rims = 18, tran = "automatic"):
        """
        Initializer method. Sets initial attributes based on user input
        :param make: car make
        :param model: car model
        :param color: car color
        :param year: car year
        :param location: car's location in the world
        :param engine: car's engine size
        :param rims: car's tire size
        :param tran: car's transmission type
        """
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.location = location
        self.rims = rims
        self.engine_size = engine
        self.transmission_type = tran

    def forward(self, speed):
        """
        A method for "moving forward"
        :param speed: the car's speed
        :return: None
        """
        print("Move forward {0}".format(speed))

    def fly(self):
        """
        Apparently, our car can fly!

        :return: None
        """
        print("Fly, birdie, fly!")

    def reverse(self, speed):
        """
        A method for "moving backwards"
        :param speed: the car's speed
        :return: None
        """
        print("Move backward {0}".format(speed))

    def start(self):
        """
        Starts the car
        :return: None
        """
        print("Start your engine")


def main():
    """
    The main function, which builds new cars, and demonstrates some of their methods.

    :return: None
    """

    scotts_car = Car("Toyota", "Sienna", "Blue", 2015, "Nicholasville, KY", engine = "v6")
    print(scotts_car.make)
    scotts_car.start()
    scotts_car.forward(90)

    jessies_car = Car("Chrystler" , "LeBaron", "Black", 1991, "Virginia", "V6", 17)
    print(jessies_car.color)
    jessies_car.start()
    jessies_car.start()
    jessies_car.forward(20)

main()
