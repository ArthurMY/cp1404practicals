def celsius_to_fahreheit():
    celsius = get_temperature_in_fahreheit()
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def fahreheit_to_celsius():
    fahreheits = get_temperature_in_celsius()
    celsius = 5 / 9 * (fahreheits - 32)
    print(f"Result: {celsius:.2f} C")


def get_temperature_in_celsius():
    return float(input("temperature in fahreheit: "))


def get_temperature_in_fahreheit():
    return float(input("temperature in celsius: "))


celsius_to_fahreheit()
fahreheit_to_celsius()
