"""
File met objecten verantwoordelijk voor het managen van welke data opgehaald/ingelezen moet worden.

De objecten controleren een referentie document voor de namen van reeds afgehandelde/geaggregeerde
input datasets. Een dataset wordt in eerste instantie enkel verwerkt wanneer deze niet in de
referentie lijst staat.

Data collectors zijn verantwoordelijk voor de volgende zaken:
- controleren welke bestanden ingelezen moeten worden.
- inlezen van de data.
- schoonmaken van de dataset (toewijzen juiste datatypes, etc.)
"""
from abc import ABC, abstractmethod

from pandas import DataFrame

from dotenv import load_dotenv

load_dotenv()


class AbstractCollectionStrategy(ABC):
        
        @abstractmethod
        def collect_data(self, data_path: str) -> DataFrame:
            pass


class AbstractPreperationStrategy(ABC):
        
        @abstractmethod
        def prepare_dataset(self, dataset: DataFrame) -> DataFrame:
            pass



class DataManagerContext:

    def __init__(
              self, 
              collection_strategy: AbstractCollectionStrategy,
              preperation_strategy: AbstractPreperationStrategy
              ) -> None:
        self._data_collect_strategy = collection_strategy
        self._dataset_preperation_strategy = preperation_strategy

    @property
    def collection_strategy(self) -> AbstractCollectionStrategy:
        return self._data_collect_strategy
    
    @collection_strategy.setter
    def collection_strategy(self, new_strategy: AbstractCollectionStrategy) -> None:
        self._data_collect_strategy = new_strategy

    @property
    def preperation_strategy(self) -> AbstractPreperationStrategy:
        return self._data_collect_strategy
    
    @preperation_strategy.setter
    def preperation_strategy(self, new_strategy: AbstractPreperationStrategy) -> None:
        self._data_collect_strategy = new_strategy

    def get_data(self) -> DataFrame:
         input_data: DataFrame = self.collection_strategy.collect_data()






