
from unittest.mock import patch, mock_open

import pytest

from wordish.text_parser import TextParser


def test_load_file_simple():
    with patch("builtins.open",
               mock_open(read_data="Vad som helst")):

        text_parser = TextParser()
        text_parser.load_file("path/to/text/file")
        assert text_parser.data == "Vad som helst"


def test_load_file_with_wrong_encoding():
    file_path = "wordish/wrong_type_text.txt"
    with pytest.raises(UnicodeDecodeError):
        text_parser = TextParser()
        text_parser.load_file(file_path)
