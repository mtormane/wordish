import matplotlib.pyplot as plt
from numpy import arange

ny_lista = []


def count_word_length(lista):
    for orden in lista:
        length = len(orden)
        ny_lista.append(length)

    return ny_lista


def longest_word(lista):
    longura = 0
    for orden in lista:
        length = len(orden)
        if length > longura:
            longura = length
    return longura


def draw_histogram(values, word_length, word_amount):
    x_value = values

    plt.hist(x_value, word_length, ec="red")

    plt.xticks(arange(1, word_length + 1, 1))
    plt.xlabel("Word Length")
    plt.ylabel("Count")
    plt.title(f"Word length Distribution of {word_amount} words")

    plt.show()
