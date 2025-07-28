"""
File met objecten verantwoordelijk voor de CRUD operaties m.b.t. de output.
CRUD = Create, Replace, Update, Delete
"""
import os

import pandas as pd

from pandas import DataFrame

from source_code.utils.file_readers_writers import dataset_reader
from source_code.utils.string_utils import file_extention_from_path

from dotenv import load_dotenv
load_dotenv()


OUTPUT_FOLDER_PATH: str = os.getenv("OUTPUT_FOLDER_PATH")



class OutputManager:

    output_folder: str = os.path.join(OUTPUT_FOLDER_PATH, 'rapportage_dataset.csv')

    def __init__(self) -> None:
        self.dataset: DataFrame = dataset_reader(path=self.output_folder, file_extention=file_extention_from_path(self.output_folder))

    def add(self, new_data: DataFrame) -> None:
        self.dataset = pd.concat([self.dataset, new_data], ignore_index=True)

    def store_dataset(self, mode: str = 'overwrite') -> None:
        match mode:
            case 'overwrite':
                self.dataset.to_csv(self.output_folder, index=False, encoding='utf-8')

    def load_stored_dataset(path: str) -> DataFrame:
        pass