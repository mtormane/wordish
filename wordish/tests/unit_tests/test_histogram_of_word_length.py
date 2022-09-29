import pytest

from wordish.histogram_of_word_length import count_word_length


def test_count_word_length():
    assert count_word_length(["hej", "då", "elak", "snäll", "varför", \
                              "bibliotek", "åsna", "penna"]) == [3, 2, 4, 5, 6, 9, 4, 5]
