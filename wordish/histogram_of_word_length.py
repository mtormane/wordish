import matplotlib.pyplot as plt

from word_counting import calculate_list_length

ny_lista = []


def count_word_length(lista):
    for orden in lista:
        length = len(orden)
        ny_lista.append(length)

    return ny_lista


def draw_histogram(values):
    x_value = values

    plt.hist(x_value, 20, ec="red")

    plt.xlabel("Word Length")
    plt.ylabel("Count")
    plt.title("Word length Distribution")

    plt.show()
