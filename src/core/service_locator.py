# src/core/service_locator.py
from config.adapters.adapters import DataAdapterFactory

class ServiceLocator:
    def __init__(self):
        self._data_adapters = {}

    def get_data_adapter(self, file_path):
        """
        Get a data adapter for the specified file path.

        Args:
            file_path (str): Path to the data file.

        Returns:
            DataAdapter: The data adapter for the given file path.
        """
        if file_path not in self._data_adapters:
            self._data_adapters[file_path] = DataAdapterFactory.get_adapter(file_path)
        return self._data_adapters[file_path]
