"""
File met tests voor de input manager.
"""
import os

from source_code.services.input_manager import InputManager

from dotenv import load_dotenv
load_dotenv()

def test_previous_handles_sets():
    manager_object = InputManager()
    assert manager_object != None