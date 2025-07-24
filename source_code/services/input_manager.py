"""
File met objecten verantwoordelijk voor het bijhouden welke bestanden zijn 
behandeld (al zijn opgenomen in de dashboard dataset).
"""
import os
from typing import List

from source_code.utils.file_readers_writers import read_json

import pandas as pd
from pandas import DataFrame

from dotenv import load_dotenv
load_dotenv()


INPUT_FOLDER_PATH: str = os.getenv("INPUT_FOLDER_PATH")
REFERENCE_FOLDER_PATH: str = os.getenv("REFERENCE_FOLDER_PATH")
HANDLED_INPUT_FILENAME: str = os.getenv("HANDLED_INPUT_FILENAME")


class InputManager:

    def __init__(self, input_folder_path: str = INPUT_FOLDER_PATH) -> None:
        self.input_folder_path = input_folder_path
        self._prev_handled_files: List[str] = []

    def get_new_input_data(self) -> DataFrame:
        pass

    def prev_handled_input_from_json(self) -> List[str]:
        json_data: dict = read_json(file_path=os.path.join(REFERENCE_FOLDER_PATH, HANDLED_INPUT_FILENAME))
        return json_data['handled_input_files']