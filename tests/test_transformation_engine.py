"""
File met tests voor de transformation engine.
"""
import os

from source_code.services.tranformation_engine import TransformationEngine

from dotenv import load_dotenv
load_dotenv()


def test_transformation_engine_run() -> None:
    transformation_engine = TransformationEngine()
    transformation_engine.run_transformations()
    print("transormation result", transformation_engine.transformation_result)
    assert transformation_engine.transformation_result is not None
    