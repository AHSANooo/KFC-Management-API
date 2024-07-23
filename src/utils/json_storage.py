# src/utils/json_storage.py

import json
from pathlib import Path
from typing import Any

def read_json_file(file_path: str) -> Any:
    """Read JSON data from a file."""
    if not Path(file_path).exists():
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path: str, data: Any) -> None:
    """Write JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
