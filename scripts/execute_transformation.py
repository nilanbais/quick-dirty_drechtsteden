"""
Script voor het configureren en starten van de transformaties.
"""
from source_code.services.automation_engine import AutomationEngine

if __name__ == '__main__':
    transformation_engine = AutomationEngine()
    transformation_engine.run_transformations()