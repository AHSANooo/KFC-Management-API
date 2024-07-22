# src/core/json_loader.py
import json
from .file_loader import FileLoader

class JSONLoader(FileLoader):
    def load(self, file_path):
        """
        Load JSON data from a file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict: Loaded JSON data.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except IOError as e:
            raise IOError(f"Error loading JSON from '{file_path}': {e}")
