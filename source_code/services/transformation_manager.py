"""
File met objecten verantwoordelijk voor de transformatie gerelateerde operaties.
"""
import os
from datetime import datetime, timedelta

import pandas as pd

from pandas import DataFrame, Series

from source_code.models.interfaces import (
    TransformationInputInterface, 
    ReportDatasetInterface
)
from source_code.utils.aggregation_utils import (
    get_avg_time,
    get_max_time
)
from source_code.utils.preperation_utils import strftimedelta

from dotenv import load_dotenv
load_dotenv()


class TransformationManager:

    def __init__(self):
        pass

    def aggregate_data(self, dataset: DataFrame) -> DataFrame:
        """
        Hoofdfunctie voor het uitvoeren van de verschillende aggregaties.
        """
        dataset['Datum'] = pd.to_datetime(dataset['Start']).dt.date
        aggregated_dataset: DataFrame = dataset.groupby('Datum').apply(self.aggregate_daily_metrics).reset_index(drop=True)
        # result_dataset: DataFrame = self.agg_result_cleanup(aggregated_dataset)
        result_dataset: DataFrame = aggregated_dataset
        return result_dataset

    def aggregate_daily_metrics(self, dataset_day: DataFrame) -> Series:
        """
        Input: df met alle data m.b.t. 1 dag
        Output: pd.Series (record) met de geaggregeerde metrics van de input dag.
        """
        pre_filtered_dataset: DataFrame = dataset_day

        # presentatie van de datapunten wordt gedaan in de methods voor het extraheren/berekenen van de data
        return Series({
            "Datum Call": self.get_date_value(pre_filtered_dataset['Datum']),
            "Aangeboden": self.calls_offered(pre_filtered_dataset),
            "ACD-Oproepen": self.acd_calls(pre_filtered_dataset),
            "Geannuleerde Oproepen": self.calls_canceled(pre_filtered_dataset),
            "Gemiddelde Antwoord Snelheid (sec)": self.avg_answer_time(pre_filtered_dataset),
            "Gemiddelde Annuleer-tijd (sec)": self.avg_cancel_time(pre_filtered_dataset),
            "Gemiddelde ACD-tijd (sec)": self.avg_acd_time(pre_filtered_dataset),
            "Gemiddelde ACW-tijd (sec)": self.avg_acw_time(pre_filtered_dataset),
            "Maximale Vertraging (sec)": self.max_call_delay(pre_filtered_dataset),
            "Maximale In-wachtrij": '[berekening toevoegen]',
            "Extensie Uit-gesprek": '[berekening toevoegen]',
            "Gemiddelde Extensie Uit-gesprek": '[berekening toevoegen]',
            "ACD-Tijd (%)": self.acd_time_percentage(pre_filtered_dataset),
            "Beantwoorde Oproepen (%)": self.answered_calls_percentage(pre_filtered_dataset),
            "Binnen Service-Level (%)": self.within_service_percentage(pre_filtered_dataset),
            "Omgeleid Geen Antwoord": '[berekening toevoegen]'
        })
    
    @staticmethod
    def agg_result_cleanup(dataset: DataFrame) -> DataFrame:
        # dataset.reset_index(drop=True, inplace=True)

        dataset['Datum'] = dataset['Datum Call']
        clean_dataset = dataset.drop('Datum Call', axis=1)

        return clean_dataset

    @staticmethod
    def get_date_value(dataset_column: Series) -> datetime:
        return dataset_column.iloc[0]
    
    @staticmethod
    def calls_offered(dataset: DataFrame) -> DataFrame:
        return len(dataset)

    @staticmethod
    def acd_calls(dataset: DataFrame) -> int:
        acd_calls_df: DataFrame = dataset[dataset['Call Disposition'] == 'Answered']
        return len(acd_calls_df)
    
    @staticmethod
    def calls_canceled(dataset: DataFrame) -> int:
        canceled_calls_df: DataFrame = dataset[dataset['Call Disposition'] == 'Abandoned']
        return len(canceled_calls_df)
    
    @staticmethod
    def avg_answer_time(dataset: DataFrame) -> str:
        avg_time: timedelta = get_avg_time(dataset, columns=['System', 'Queue', 'Ring'])
        return avg_time.total_seconds()
    
    @staticmethod
    def avg_cancel_time(dataset: DataFrame) -> str:
        avg_time: timedelta = get_avg_time(dataset[dataset['Call Disposition'] == 'Abandoned'], columns='Duration')
        if not isinstance(avg_time, timedelta):
            return 0
        return avg_time.total_seconds()

    @staticmethod
    def avg_acd_time(dataset: DataFrame) -> str:
        avg_time: timedelta = get_avg_time(dataset[dataset['Call Disposition'] == 'Answered'], columns=['Duration'])
        return avg_time.total_seconds()
    
    @staticmethod
    def avg_acw_time(dataset: DataFrame) -> str:
        avg_time: timedelta = get_avg_time(dataset, columns=['ACW'])
        return avg_time.total_seconds()
    
    @staticmethod
    def max_call_delay(dataset: DataFrame) -> str:
        max_time: timedelta = get_max_time(dataset, columns=['System', 'Queue', 'Ring'])
        return max_time.total_seconds()
    
    @staticmethod
    def acd_time_percentage(dataset: DataFrame) -> float:
        total_acd_time: timedelta = dataset['Duration'][dataset['Call Disposition'] == 'Answered'].sum()
        finished_calls_count: int = len(dataset[dataset['Call Disposition'] == 'Answered'])
        acd_percentage: float = total_acd_time.total_seconds() / finished_calls_count
        return acd_percentage
    
    @staticmethod
    def answered_calls_percentage(dataset: DataFrame) -> float:
        answered_calls_count: int = len(dataset[dataset['Call Disposition'] == 'Answered'])
        total_calls_count: int = len(dataset)
        answered_percentage: float = answered_calls_count / total_calls_count
        return answered_percentage
    
    @staticmethod
    def within_service_percentage(dataset: DataFrame) -> float:
        binnen_service_drempelwaarde: timedelta = timedelta(seconds=20)
        temp_df: DataFrame = dataset[dataset['Call Disposition'] == 'Answered'][['System', 'Queue', 'Ring']]
        temp_df['row_sum'] = temp_df.sum(axis=1)
        opgenomen_binnen_drempelwaarde_df: DataFrame = temp_df[temp_df['row_sum'] < binnen_service_drempelwaarde]
        opgenomen_binnen_drempelwaarde_count: int = len(opgenomen_binnen_drempelwaarde_df)
        total_calls_count: int = len(dataset)
        return opgenomen_binnen_drempelwaarde_count / total_calls_count