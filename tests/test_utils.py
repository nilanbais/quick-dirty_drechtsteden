"""
File met tests voor de utility functies.
"""
import os

from source_code.utils.string_utils import file_extention_from_path


def test_file_extention_from_path():
    path: str = "tests\test_data_manager.py"
    file_extention: str = file_extention_from_path(path)
    assert file_extention == 'py'