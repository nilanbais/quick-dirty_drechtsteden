"""
Script voor het configureren en starten van de transformaties.
"""
from source_code.services.automation_engine import AutomationEngine



def main():
    transformation_engine = AutomationEngine(output_file_name='rapportage_dataset.csv')
    transformation_engine.run_transformations()
    transformation_engine.store_transformation_dataset(transformation_engine.transformation_result)

if __name__ == '__main__':
    main()
