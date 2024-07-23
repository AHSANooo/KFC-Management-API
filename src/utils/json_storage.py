# src/utils/json_storage.py

import json
from typing import Dict, Any


def read_json_file(filepath: str) -> Dict[str, Any]:
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON file")


def write_json_file(filepath: str, data: Dict[str, Any]) -> None:
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
