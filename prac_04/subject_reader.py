"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    get_summary()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        list.append(parts)
    input_file.close()
    return list


def get_summary():
    input_file = open(FILENAME)
    for line in input_file:
        lines = line.strip().split(',')
        print(f"{lines[0]} is taught by {lines[1]} and has {lines[-1]} students")
    input_file.close()


main()
