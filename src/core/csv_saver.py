# src/core/csv_saver.py
import csv
from .file_saver import FileSaver


class CSVSaver(FileSaver):
    def save(self, data, file_path):
        """
        Save data to a CSV file.

        Args:
            data (list of dicts): Data to save as CSV.
            file_path (str): Path to the CSV file.
        """
        try:
            with open(file_path, 'w', newline='') as file:
                if not data:
                    raise ValueError("No data provided for saving.")

                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        except IOError as e:
            raise IOError(f"Error saving CSV to '{file_path}': {e}")
