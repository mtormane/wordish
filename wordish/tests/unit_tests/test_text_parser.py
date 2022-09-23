
from unittest.mock import patch, mock_open

import pytest

from wordish.text_parser import TextParser


def test_load_file_simple():
    with patch("builtins.open",
               mock_open(read_data="Vad som helst".encode('utf-8'))):
        text_parser = TextParser()
        text_parser.load_file("path/to/text/file")
        assert text_parser.data == "Vad som helst".encode('utf-8')


def test_load_file_wrong_encoding():
    with patch("builtins.open",
               mock_open(read_data='Nu testar vi'.encode('utf-16'))):
        with pytest.raises(ValueError):
            text_parser = TextParser()
            text_parser.load_file("path/to/text/file")
