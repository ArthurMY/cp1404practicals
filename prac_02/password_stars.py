def main():
    password = get_password()
    print(f"{len(password) * '*'}")


def get_password():
    return input("Password: ")


main()
