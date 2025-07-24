"""
File met tests voor het kunnen lezen van variablen uit de .env file.
"""
import os

from dotenv import load_dotenv
load_dotenv()

def test_read_env_variable():
    assert os.getenv("INPUT_FOLDER_PATH") != None