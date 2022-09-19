from sys import argv


def read_in_a_file():
    program, filename = argv

    text = open(filename)

    print(text.read())

read_in_a_file()
