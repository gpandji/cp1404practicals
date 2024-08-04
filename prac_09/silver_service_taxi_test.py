from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    fancy_taxi = SilverServiceTaxi("Limo", 100, 2)
    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print("Fare: ${:.2f}".format(fare))
    print(fancy_taxi)


main()
