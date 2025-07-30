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
from source_code.services.transformation_manager import TransformationManager


class AutomationEngine:

    def __init__(self):
        pass

    def run_transformations(self) -> None:
        transformation_input: DataFrame = self.get_transformation_input(update_handled_files_flag=True)
        print("transformation input:", transformation_input)
        # Uitvoeren van de transformaties/aggregaties
        transformed_data: DataFrame = self.execute_transformations(transformation_input)
        self.transformation_result: DataFrame = transformed_data

    def testrun_transformations(self) -> None:
        transformation_input: DataFrame = self.get_transformation_input(update_handled_files_flag=False)
        print("transformation input:", transformation_input)
        # Uitvoeren van de transformaties/aggregaties
        transformed_data: DataFrame = self.execute_transformations(transformation_input)
        self.transformation_result: DataFrame = transformed_data

    @staticmethod
    def get_transformation_input(update_handled_files_flag: bool) -> DataFrame:
        input_manager = InputManager()
        transformation_input: DataFrame = input_manager.get_input_data(update_handled_files_flag)
        return transformation_input
    
    @staticmethod
    def execute_transformations(dataset: DataFrame) -> DataFrame:
        transformation_manager = TransformationManager()
        transformed_dataset: DataFrame = transformation_manager.aggregate_data(dataset)
        return transformed_dataset

    @staticmethod
    def store_transformation_dataset(dataset: DataFrame) -> None:
        output_manager = OutputManager()
        output_manager.add(dataset)
        output_manager.store_dataset()
        