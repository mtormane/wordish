import os
import pytest


from wordish.text_parser import TextParser


@pytest.fixture
def json_parser_instance():
    text_parser = TextParser()
    text_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    return text_parser


@pytest.fixture
def file_path():
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_dir, "integration", "fixtures", "test_basic.json")


@pytest.fixture
def bad_file_path():
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_dir, "integration", "fixtures", "fake_db.json")
