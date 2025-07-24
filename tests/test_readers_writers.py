"""
File met tests voor de objecten die data lezen/schrijven.
"""
import os
from dotenv import load_dotenv
load_dotenv()

from source_code.utils.file_readers_writers import read_json, write_to_json

REFERENCE_FOLDER_PATH: str = os.getenv("REFERENCE_FOLDER_PATH")
HANDLED_INPUT_FILENAME: str = os.getenv("HANDLED_INPUT_FILENAME")


def test_read_json():
    assert read_json(file_path=os.path.join(REFERENCE_FOLDER_PATH, HANDLED_INPUT_FILENAME)) != None