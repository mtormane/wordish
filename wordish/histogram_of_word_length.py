import matplotlib.pyplot as plt

en_lista = ["hej", "då", "elak", "snäll", "varför", "bibliotek", "åsna", "penna"]

ny_lista = []


def count_word_length(lista):
    for orden in lista:
        length = len(orden)
        ny_lista.append(length)
    return ny_lista


def draw_histogram(values):
    x_value = values

    plt.hist(x_value)

    plt.xlabel("age")
    plt.ylabel("count")
    plt.title("Population Age Count")

    plt.show()

