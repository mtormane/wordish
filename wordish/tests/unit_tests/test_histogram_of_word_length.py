
from unittest.mock import patch


from wordish.histogram_of_word_length import count_word_length, draw_histogram, longest_word


def test_count_word_length():
    tmp = count_word_length(["hey", "then", "mean", "kinder", "why",
                            "library", "donkey", "pencil"])
    assert tmp == [3, 4, 4, 6, 3, 7, 6, 6]


@patch("matplotlib.pyplot.title")
@patch("matplotlib.pyplot.ylabel")
@patch("matplotlib.pyplot.xlabel")
@patch("matplotlib.pyplot.show")
def test_draw_histogram(mock_ylabel, mock_xlabel, mock_title, mock_show):
    draw_histogram([3, 4, 4, 6, 3, 7, 6, 6], 7, 8)
    mock_xlabel.assert_called_once()
    mock_ylabel.assert_called_once()
    mock_title.assert_called_once()
    mock_show.assert_called_once()


@patch("matplotlib.pyplot.hist")
@patch("matplotlib.pyplot.show")
@patch("matplotlib.pyplot.xticks")
def test_draw_histogram_2(mock_hist, mock_show, mock_xticks):
    draw_histogram([3, 4, 4, 6, 3, 7, 6, 6], 7, 8)
    mock_show.assert_called_once()
    mock_xticks.assert_called_once()
    mock_hist.assert_called_once()


def test_longest_word():
    tmp_2 = longest_word(["hey", "then", "mean", "kinder", "why",
                                                           "library", "donkey", "pencil"])
    assert tmp_2 == 7
