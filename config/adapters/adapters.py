# config/adapters/__init__.py
from .json_adapter import JSONDataAdapter
from .csv_adapter import CSVDataAdapter
import os


class DataAdapterFactory:
    @staticmethod
    def get_adapter(file_path):
        # Check if the file exists before proceeding
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            return None

        _, ext = os.path.splitext(file_path)
        if ext == '.json':
            return JSONDataAdapter(file_path)
        elif ext == '.csv':
            return CSVDataAdapter(file_path)
        else:
            raise ValueError("Unsupported file format")
