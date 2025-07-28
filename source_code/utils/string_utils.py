"""
File met objecten voor het lezen van bestanden.
"""

def file_extention_from_path(path: str) -> str:
    file_extention = path.split(".")[-1]
    return file_extention