# config/adapters/json_adapter.py
import json

class JSONDataAdapter:
    def __init__(self, file_path):
        self.file_path = file_path

    def connect(self):
        pass  # Connection setup if required

    def load(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def disconnect(self):
        pass  # Cleanup if required

    def load_order(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_order(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
