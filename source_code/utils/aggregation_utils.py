"""
File met objecten die abstracte functionaliteit implementeren m.b.t. het aggregeren van data.
"""
from typing import List, Union
from datetime import timedelta

from pandas import DataFrame, Series


def get_avg_time(dataset: Union[Series, DataFrame], columns: List[str]) -> timedelta:
    """
    
    """
    # one column dataframes (Series) need a shorter calculation
    if isinstance(dataset[columns], Series):
        return dataset[columns].mean()
    
    subset: DataFrame = dataset[columns].copy()
    subset['row_sum'] = subset.sum(axis=1)
    average: timedelta = subset['row_sum'].mean()
    return average


def get_max_time(dataset: Union[Series, DataFrame], columns: List[str]) -> timedelta:
    """
    
    """
    if isinstance(dataset[columns], Series):
        return dataset[columns].max()
    
    subset: DataFrame = dataset[columns].copy()
    subset['row_sum'] = subset.sum(axis=1)
    max_time: timedelta = subset['row_sum'].max()
    return max_time