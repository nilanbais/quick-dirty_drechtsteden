"""
File met het object verantwoordelijk voor het 'aan elkaar knopen' van de stappen in de automatisering.

stappen die doorlopen worden:
1. inlezen van de input data vóó de aggregatie.
2. aggregeren van de data over een periode van 1 dag (elke dag is 1 record).
3. toevoegen van de nieuwe records aan de output (dashboard dataset).
"""
from pandas import DataFrame

from source_code.services.input_manager import InputManager
from source_code.services.output_manager import OutputManager


class TransformationEngine:

    def __init__(self):
        pass

    def run_transformations(self) -> None:
        transformation_input: DataFrame = self.get_transformation_input()
        print("transformation input:", transformation_input)
        # Uitvoeren van de transformaties/aggregaties
        self.transformation_result: DataFrame = transformation_input

    @staticmethod
    def get_transformation_input() -> DataFrame:
        input_manager = InputManager()
        transformation_input: DataFrame = input_manager.get_input_data()
        return transformation_input
    
    @staticmethod
    def store_transformation_dataset(dataset: DataFrame) -> None:
        output_manager = OutputManager()
        output_manager.add(dataset)
        output_manager.store_dataset()
        