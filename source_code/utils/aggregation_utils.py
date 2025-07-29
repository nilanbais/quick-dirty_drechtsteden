"""
File met objecten die abstracte functionaliteit implementeren m.b.t. het aggregeren van data.
"""
from typing import List
from datetime import timedelta

from pandas import DataFrame


def get_avg_time(dataset: DataFrame, columns: List[str]) -> timedelta:
    """
    
    """
    subset: DataFrame = dataset[columns].copy()
    subset['row_sum'] = subset.sum(axis='columns')
    average: timedelta = subset['row_sum'].mean()
    return average


def get_max_time(dataset: DataFrame, columns: List[str]) -> timedelta:
    """
    
    """
    subset: DataFrame = dataset[columns].copy()
    subset['row_sum'] = subset.sum(axis='columns')
    max_time: timedelta = subset['row_sum'].max()
    return max_time