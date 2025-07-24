"""
Script voor het configureren en starten van de transformaties.
"""
from source_code.services.tranformation_engine import TransformationEngine

if __name__ == '__main__':
    transformation_engine = TransformationEngine()
    transformation_engine.run_transformations()