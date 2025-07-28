"""
File met objecten verantwoordelijk voor de CRUD operaties m.b.t. de output.
CRUD = Create, Replace, Update, Delete
"""
import os

import pandas as pd

from pandas import DataFrame

from source_code.utils.file_readers_writers import dataset_reader
from source_code.utils.string_utils import file_extention_from_path
from source_code.models.interfaces import ReportDatasetInterface

from dotenv import load_dotenv
load_dotenv()


OUTPUT_FOLDER_PATH: str = os.getenv("OUTPUT_FOLDER_PATH")



class OutputManager:

    stored_dataset_path: str = os.path.join(OUTPUT_FOLDER_PATH, 'rapportage_dataset.csv')

    def __init__(self) -> None:
        self.dataset: DataFrame = self.load_stored_dataset()

    def add(self, new_data: DataFrame) -> None:
        self.dataset = pd.concat([self.dataset, new_data], ignore_index=True)

    def store_dataset(self, mode: str = 'overwrite') -> None:
        match mode:
            case 'overwrite':
                self.dataset.to_csv(self.stored_dataset_path, index=False, encoding='utf-8')

    def load_stored_dataset(self) -> DataFrame:
        if os.path.exists(self.stored_dataset_path):
            stored_dataset: DataFrame = dataset_reader(path=self.stored_dataset_path, file_extention=file_extention_from_path(self.stored_dataset_path))
        else:
            stored_dataset = DataFrame(columns=ReportDatasetInterface.columns)
        return stored_dataset