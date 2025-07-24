"""
File met objecten die abstracte functionaliteit implementeren m.b.t. het prepareren van data.
"""
from typing import List
from datetime import datetime, timedelta

from pandas import DataFrame
from pandas.core.indexes.base import Index



def summarize_unused_columns(dataset_column_index: Index) -> List[str]:
   """
   
   """
   unused_column_names: List[str] = [col_name for col_name in dataset_column_index if 'unnamed' in str(col_name).lower()]
   return unused_column_names


def filter_unused_columns(dataset: DataFrame) -> DataFrame:
    """
    
    """
    input_dataset: DataFrame = dataset.copy()
    unused_column_names: List[str] = summarize_unused_columns(dataset.columns)
    clean_df: DataFrame = input_dataset.drop(labels=unused_column_names, axis='columns')
    return clean_df


def set_datetime_dtype_values(dataset: DataFrame, columns: List[str], format_string: str = "%Y-%m-%d %H:%M:%S") -> DataFrame:
    """
    
    """
    for col_name in columns:
        dataset[col_name] = dataset[col_name].map(lambda str_value: datetime.strptime(str_value, format_string))

    return dataset


def timedelta_from_string(timestring: str, format_string: str = "%H:%M:%S") -> timedelta:
    """
    
    """
    time_obj = datetime.strptime(timestring, format_string)
    timedelta_obj: timedelta = timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second)
    return timedelta_obj


def timestring_to_seconds(dataset: DataFrame, columns: List[str]) -> DataFrame:
    """
    
    """
    for col_name in columns:
        dataset[col_name] = dataset[col_name].map(lambda timestring: timedelta_from_string(timestring))

    return dataset