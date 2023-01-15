from prac_09.silver_service_taxi import SliverServiceTaxi


def main():
    taxi = SliverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
