from unittest.mock import patch

import pytest

from wordish.json_parser import JsonParser
from wordish.main import load_data
from wordish.main import parse_arguments, ArgumentParser
from wordish.main import main, init


class MockArgs:
    file_path = "path/to/file.ext"


def test_main():
    with patch("wordish.main.parse_arguments", return_value=MockArgs) as mock_parse_arguments:
        with patch("wordish.main.load_data") as mock_load_data:
            main()
            mock_parse_arguments.assert_called_once()
            mock_load_data.assert_called_with("path/to/file.ext")


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


def test_load_data_success():
    with patch.object(JsonParser, "load_file") as mock_load_file:
        load_data("file_path.json")
        mock_load_file.assert_called_with("file_path.json")


def test_load_data_exception():
    with patch.object(JsonParser, "load_file", side_effect=Exception('MockedError')) as mock_load_file:
        with pytest.raises(Exception) as excinfo:
            load_data("something")
            mock_load_file.assert_called_with("something")
            assert excinfo.value.message == 'MockedError'


@patch("wordish.main.main")
def test_init(mock_main):
    with patch("wordish.main.__name__", "__main__"):
        init()
        mock_main.assert_called_once()
