"""
File met objecten verantwoordelijk voor het bijhouden welke bestanden zijn 
behandeld (al zijn opgenomen in de dashboard dataset).
"""
import os
from typing import List

from source_code.utils.file_readers_writers import read_json, write_to_json
from source_code.services.input_readers import dataset_reader

import pandas as pd
from pandas import DataFrame

from dotenv import load_dotenv
load_dotenv()


INPUT_FOLDER_PATH: str = os.getenv("INPUT_FOLDER_PATH")
REFERENCE_FOLDER_PATH: str = os.getenv("REFERENCE_FOLDER_PATH")
HANDLED_INPUT_FILENAME: str = os.getenv("HANDLED_INPUT_FILENAME")


class InputManager:

    def __init__(self) -> None:
        self.prev_handled_files: List[str] = self.get_prev_handled_input_from_ref()
        self.input_queue: list = [file for file in os.listdir(INPUT_FOLDER_PATH) if file not in self.prev_handled_files]

    def get_input_data(self) -> DataFrame:
        read_result = DataFrame()
        handled_input: list = []
        for file in self.input_queue:
            dataset: DataFrame = dataset_reader(path=os.path.join(INPUT_FOLDER_PATH, file))
            read_result = read_result.add(dataset)
            handled_input.append(file)
        self.update_reference_handled_input(handled_input)

    def get_prev_handled_input_from_ref(self) -> List[str]:
        json_data: dict = read_json(file_path=os.path.join(REFERENCE_FOLDER_PATH, HANDLED_INPUT_FILENAME))
        return json_data['handled_input_files']
    
    def update_reference_handled_input(self, new_data: List[str]) -> None:
        json_object: dict = {"handled_input_files": self.prev_handled_files.append(new_data)}
        write_to_json(json_object, file_path=os.path.join(REFERENCE_FOLDER_PATH, HANDLED_INPUT_FILENAME))