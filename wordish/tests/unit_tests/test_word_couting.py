
import pytest
from wordish.word_counting import calculate_list_length


def test_word_counting_can_count_list():
    assert calculate_list_length(["one", "list", "with", "words", "and", "numbers"]) == 6


def test_word_counting_with_dictionary():
    with pytest.raises(TypeError):
        calculate_list_length({})
