"""
File met objecten verantwoordelijk voor de transformatie gerelateerde operaties.
"""
import os
from datetime import timedelta

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

from dotenv import load_dotenv
load_dotenv()


class TransformationManager:

    def __init__(self):
        pass

    def aggregate_data(self, dataset: DataFrame) -> DataFrame:
        """
        Hoofdfunctie voor het uitvoeren van de verschillende aggregaties.
        """
        dataset['datum'] = pd.to_datetime(dataset['Start']).dt.date
        aggregated_dataset: DataFrame = dataset.groupby('Datum').apply(self.aggregate_daily_metrics)
        aggregated_dataset.reset_index()
        return aggregated_dataset

    def aggregate_daily_metrics(dataset_day: DataFrame) -> Series:
        """
        Input: df met alle data m.b.t. 1 dag
        Output: pd.Series (record) met de geaggregeerde metrics van de input dag.
        """
        pre_filtered_dataset: DataFrame = dataset_day

        # Berekende waarden voor overzicht apart
        binnen_service_drempelwaarde: timedelta = timedelta(seconds=20)
        temp_df: DataFrame = pre_filtered_dataset['System', 'Queue', 'Ring'].copy()
        temp_df['row_sum'] = temp_df.sum(axis='columns')
        opgenomen_binnen_drempelwaarde: DataFrame = temp_df[temp_df['row_sum'] < binnen_service_drempelwaarde]


        return Series({
            "Aangeboden": len(pre_filtered_dataset),
            "ACD-Oproepen": len(pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Answered']),
            "Geannuleerde Oproepen": len(pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Abandoned']),
            "Gemiddelde Antwoord Snelheid": get_avg_time(pre_filtered_dataset, columns=['System', 'Queue', 'Ring']),
            "Gemiddelde Annuleer-tijd": get_avg_time(pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Abandoned'], columns='Duration'),
            "Gemiddelde ACD-tijd": get_avg_time(pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Answered'], columns=['Duration']),
            "Gemiddelde ACW-tijd": get_avg_time(pre_filtered_dataset, columns=['ACW']),
            "Maximale Vertraging": get_max_time(pre_filtered_dataset, columns=['System', 'Queue', 'Ring']),
            "Maximale In-wachtrij": '[berekening toevoegen]',
            "Extensie Uit-gesprek": '[berekening toevoegen]',
            "Gemiddelde Extensie Uit-gesprek": '[berekening toevoegen]',
            "ACD-Tijd (%)": (pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Answered'].filter('Duration', axis=1).sum())/len(pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Answered']),
            "Beantwoorde Oproepen (%)": (len(pre_filtered_dataset[pre_filtered_dataset['Call Disposition'] == 'Answered'])/len(pre_filtered_dataset))*100,
            "Binnen Service-Level (%)": (opgenomen_binnen_drempelwaarde / len(pre_filtered_dataset)) * 100,
            "Omgeleid Geen Antwoord": '[berekening toevoegen]'
        })