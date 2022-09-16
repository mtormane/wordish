import json
import os

from unittest.mock import patch, mock_open

import pytest

from wordish.json_parser import JsonParser


def test_load_file_simple():
    with patch("builtins.open",
               mock_open(read_data='{"services": [{"title": "ECU Reset", "id": "11"}]}')):
        json_parser = JsonParser()
        json_parser.load_file("path/to/json/file")
        assert json_parser.data == {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_load_file_wrong_type():
    with patch("builtins.open", mock_open(read_data="This is wrong data!")):
        with pytest.raises(ValueError):
            json_parser = JsonParser()
            json_parser.load_file("path/to/json/file")
