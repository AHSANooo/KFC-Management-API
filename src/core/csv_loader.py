# src/core/csv_loader.py
import csv
from .file_loader import FileLoader

class CSVLoader(FileLoader):
    def load(self, file_path):
        """
        Load data from a CSV file.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            list of dicts: Loaded CSV data.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except IOError as e:
            raise IOError(f"Error loading CSV from '{file_path}': {e}")
