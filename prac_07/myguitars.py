from prac_06.guitar import Guitar


def main():
    guitars = []
    infile = open("guitars.csv", 'r')
    data = infile.readlines()
    for line in data[1:]:
        line = line.strip().split(',')
        guitar = Guitar(line[0], line[1], line[2])
        guitars.append(guitar)

    for guitar in guitars:
        guitars.sort()
        print(guitar)


main()
