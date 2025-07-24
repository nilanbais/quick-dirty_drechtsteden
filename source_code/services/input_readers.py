"""
File met objecten voor het inlezen van data uit bestanden.
"""
import pandas as pd
from pandas import DataFrame


def dataset_reader(path: str, file_extention: str) -> DataFrame:
    match file_extention:
        case 'xlsx':
            input_df: DataFrame = pd.read_excel(path, header=1)
        case 'csv':
            input_df: DataFrame = pd.read_csv(path, header=1)
        case _:
            raise ValueError("No suitable file_extention given. Choose 'csv', 'xlsx'.")
    return input_df