from prac_09.unreliable_car import UnrealiableCar


def main():
    great_car = UnrealiableCar("Great", 100, 90)
    broke_car = UnrealiableCar("Broke", 100, 9)

    for i in range(1, 12):
        print(f"Attemping to drive {i}km:")
        print(f"{great_car.name:12} drove {great_car.drive(i):2}km")
        print(f"{broke_car.name:12} drove {broke_car.drive(i):2}km")

    print(great_car)
    print(broke_car)


main()
