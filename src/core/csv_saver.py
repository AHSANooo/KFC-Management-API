from .file_saver import FileSaver
import csv

class CSVSaver(FileSaver):
    def save(self, data, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
