"""
File met het object verantwoordelijk voor het 'aan elkaar knopen' van de stappen in de automatisering.

stappen die doorlopen worden:
1. inlezen van de input data vóó de aggregatie.
2. aggregeren van de data over een periode van 1 dag (elke dag is 1 record).
3. toevoegen van de nieuwe records aan de output (dashboard dataset).
"""
from pandas import DataFrame

from source_code.services.input_manager import InputManager


class TransformationEngine:

    def __init__(self):
        pass

    def run_transformations(self) -> None:
        self.tranformation_input = self.get_transformation_input()
        # Uitvoeren van de transformaties/aggregaties
        # daarna: geaggregeerde data wegschrijven

    @staticmethod
    def get_transformation_input() -> DataFrame:
        input_manager = InputManager()
        transformation_input: DataFrame = input_manager.get_input_data()
        return transformation_input