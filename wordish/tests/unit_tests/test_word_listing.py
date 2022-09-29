import pytest

from wordish.word_listing import create_word_list


def test_create_word_list_with_list_input():
    assert create_word_list("Does this become a string") \
           == ['Does', 'this', 'become', 'a', 'string']


def test_create_word_list_with_wrong_input():
    with pytest.raises(TypeError):
        create_word_list(123)
