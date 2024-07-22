from .file_loader import FileLoader
import csv

class CSVLoader(FileLoader):
    def load(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
