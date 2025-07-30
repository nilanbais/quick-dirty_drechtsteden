"""
File met objecten voor het lezen van bestanden.
"""
import json

import pandas as pd
from pandas import DataFrame


def dataset_reader(path: str, file_extention: str) -> DataFrame:
    match file_extention:
        case 'xlsx':
            dataset: DataFrame = pd.read_excel(path, header=1)
        case 'csv' | '.csv':
            dataset: DataFrame = pd.read_csv(path, header=0, sep=';')
        case _:
            raise ValueError("No suitable file_extention given. Choose 'csv', 'xlsx'.")
    return dataset



def read_json(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f) 
        return json_data
    except FileNotFoundError:
        print("Bestand niet gevonden.")
    except json.JSONDecodeError as e:
        print("JSON is ongeldig:", e)


def write_to_json(json_data: dict, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4)