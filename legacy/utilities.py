import json

def read_json(file_path: str):
    """Reads a JSON file and returns the parsed data."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def dict_to_string(data:dict) -> str:
    return json.dumps(data)