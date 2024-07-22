# src/core/json_saver.py
import json
from .file_saver import FileSaver

class JSONSaver(FileSaver):
    """
    JSONSaver class for saving JSON data to a file.
    """

    def save_json(self, data, file_name: str):
        """
        Save JSON data to a file.

        Args:
            data (dict): Data to save as JSON.
            file_name (str): Name of the JSON file to save to.
        """
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving JSON to '{file_name}': {e}")
