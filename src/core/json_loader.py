from .file_loader import FileLoader
import json

class JSONLoader(FileLoader):
    def load(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
