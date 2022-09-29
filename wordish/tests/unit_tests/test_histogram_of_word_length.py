
from unittest.mock import patch


from wordish.histogram_of_word_length import count_word_length, draw_histogram


def test_count_word_length():
    print("hej")
    tmp = count_word_length(["hej", "då", "elak", "snäll", "varför",
                            "bibliotek", "åsna", "penna"])
    assert tmp == [3, 2, 4, 5, 6, 9, 4, 5]


@patch("matplotlib.pyplot.title")
@patch("matplotlib.pyplot.show")
@patch("matplotlib.pyplot.ylabel")
@patch("matplotlib.pyplot.xlabel")
@patch("matplotlib.pyplot.hist")
def test_draw_histogram(mock_hist, mock_xlabel, mock_ylabel, mock_show, mock_title):
    draw_histogram([3, 2, 4, 5, 6, 9, 4, 5])
    mock_hist.assert_called_once()
    mock_xlabel.assert_called_once()
    mock_ylabel.assert_called_once()
    mock_show.assert_called_once()
    mock_title.assert_called_once()
