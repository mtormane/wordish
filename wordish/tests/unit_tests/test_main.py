from unittest.mock import patch, PropertyMock

import pytest


from wordish.main import load_data, TextParser
from wordish.main import parse_arguments, ArgumentParser
from wordish.main import main, init


class MockArgs:
    file_path = "path/to/file.ext"


class MockStr:
    text_str = "hej"


def test_main():
    with patch("wordish.main.parse_arguments", return_value=MockArgs) \
            as mock_parse_arguments:
        with patch("wordish.main.load_data", return_value="hej") \
                as mock_load_data:
            with patch("wordish.main.create_word_list", return_value=["hej"]) \
                    as mock_create_word_list:
                with patch("wordish.main.calculate_list_length", return_value=1) \
                        as mock_calculate_list_length:
                    main()
                    mock_parse_arguments.assert_called_once()
                    mock_load_data.assert_called_with("path/to/file.ext")
                    mock_create_word_list.assert_called_with("hej")
                    mock_calculate_list_length.assert_called_with(["hej"])


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


def test_load_data_success():
    with patch.object(TextParser, "load_file") as mock_load_file:
        load_data("file_path.json")
        mock_load_file.assert_called_with("file_path.json")


def test_load_data_exception():
    with patch.object(TextParser, "load_file",
                      side_effect=Exception('MockedError')) as mock_load_file:
        with pytest.raises(Exception) as excinfo:
            load_data("something")
            mock_load_file.assert_called_with("something")
            assert excinfo.value.message == 'MockedError'


@patch("wordish.main.main")
def test_init(mock_main):
    with patch("wordish.main.__name__", "__main__"):
        init()
        mock_main.assert_called_once()
