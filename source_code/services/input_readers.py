"""
File met objecten voor het inlezen van data uit bestanden.
"""
import pandas as pd
from pandas import DataFrame


def weekly_dataset_reader(path: str) -> DataFrame:
    input_df: DataFrame = pd.read_excel(path, header=1)
    return input_df