import matplotlib.pyplot as plt
from numpy import arange

new_list_with_counted_words = []


def count_word_length(the_list):
    for the_words in the_list:
        length = len(the_words)
        new_list_with_counted_words.append(length)

    return new_list_with_counted_words


def longest_word(the_list_2):
    longest_word_in_list = 0
    for the_words_2 in the_list_2:
        length = len(the_words_2)
        if length > longest_word_in_list:
            longest_word_in_list = length
    return longest_word_in_list


def draw_histogram(values, word_length, word_amount):
    x_value = values

    plt.hist(x_value, word_length, ec="red")

    plt.xticks(arange(1, word_length + 1, 1))
    plt.xlabel("Word Length")
    plt.ylabel("Count")
    plt.title(f"Word length Distribution of {word_amount} words")

    plt.show()
