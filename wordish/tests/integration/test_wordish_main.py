import sys
import pytest

from unittest.mock import patch

from wordish.main import main


def test_main(file_path):
    with patch.object(sys, "argv", ["main", "--file_path", file_path]):
            main()



def test_main_exception(bad_file_path):
    with patch.object(sys, "argv", ["main", "--file_path", bad_file_path]):
        with pytest.raises(TypeError):
            main()
