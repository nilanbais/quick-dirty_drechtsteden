"""
File met objecten verantwoordelijk voor het bijhouden welke bestanden zijn 
behandeld (al zijn opgenomen in de dashboard dataset).
"""
import os
from typing import List

from source_code.models.interfaces import TransformationInputInterface
from source_code.utils.preperation_utils import (
    filter_unused_columns, 
    set_datetime_dtype_values,
    timestring_to_seconds
    )
from source_code.utils.file_readers_writers import (
    read_json, 
    write_to_json,
    dataset_reader
    )

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
        self.input_queue: list = [file for file in os.listdir(INPUT_FOLDER_PATH) if file not in self.prev_handled_files and file != '.gitkeep']

    def get_input_data(self) -> DataFrame:
        gathered_input_data = DataFrame(columns=TransformationInputInterface.columns)
        handled_input: list = []
        
        for file in self.input_queue:
            raw_dataset: DataFrame = dataset_reader(path=os.path.join(INPUT_FOLDER_PATH, file), file_extention='xlsx')
            clean_dataset: DataFrame = self.clean_input_dataset(raw_dataset)
            """
            Line underneath has deprecated functionality.
            See: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
            """
            gathered_input_data = pd.concat([gathered_input_data, clean_dataset], ignore_index=True)
            handled_input.append(file)

        self.update_reference_handled_input(handled_input)
        return gathered_input_data

    def get_prev_handled_input_from_ref(self) -> List[str]:
        json_data: dict = read_json(file_path=os.path.join(REFERENCE_FOLDER_PATH, HANDLED_INPUT_FILENAME))
        handled_input_files: list = [] if json_data['handled_input_files'] is None else json_data['handled_input_files']
        return handled_input_files
    
    def update_reference_handled_input(self, new_data: List[str]) -> None:
        json_object: dict = {"handled_input_files": [*new_data, *self.prev_handled_files]}
        write_to_json(json_object, file_path=os.path.join(REFERENCE_FOLDER_PATH, HANDLED_INPUT_FILENAME))

    @staticmethod
    def clean_input_dataset(dataset: DataFrame) -> DataFrame:
        filtered_colums_dataset: DataFrame = filter_unused_columns(dataset)
        dataset_datetime_dtypes: DataFrame = set_datetime_dtype_values(filtered_colums_dataset, columns=['Start','Stop'])
        dataset_timedelta_dtypes: DataFrame = timestring_to_seconds(dataset_datetime_dtypes, columns=['System', 'Queue', 'Ring', 'Talk', 'Hold', 'ACW', 'Consult', 'Disposition', 'Duration'])
        return dataset_timedelta_dtypes