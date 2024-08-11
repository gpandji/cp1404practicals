from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class."""
    unreliable_car = UnreliableCar("Old Car", 100, 50)
    for i in range(10):
        print("Attempting to drive 10km:")
        print("Drove {}km".format(unreliable_car.drive(10)))
        print(unreliable_car)


main()
