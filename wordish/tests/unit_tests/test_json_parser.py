
from unittest.mock import patch, mock_open

import pytest

from wordish.text_parser import TextParser


def test_load_file_simple():
    with patch("builtins.open",
               mock_open(read_data='{"services": [{"title": "ECU Reset", "id": "11"}]}')):
        text_parser = TextParser()
        text_parser.load_file("path/to/json/file")
        assert text_parser.data == {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_load_file_wrong_type():
    with patch("builtins.open", mock_open(read_data="This is wrong data!")):
        with pytest.raises(ValueError):
            json_parser = TextParser()
            json_parser.load_file("path/to/json/file")
