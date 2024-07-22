# src/core/file_loader.py
class FileLoader:
    def __init__(self, data_adapter):
        """
        Initialize the FileLoader with a data adapter.

        Args:
            data_adapter (DataAdapter): The data adapter to use for loading.
        """
        self.data_adapter = data_adapter

    def load(self):
        """
        Load data using the data adapter.

        Returns:
            any: Loaded data.
        """
        self.data_adapter.connect()
        try:
            data = self.data_adapter.load()
            return data
        except Exception as e:
            raise RuntimeError(f"Error loading data: {e}")
        finally:
            self.data_adapter.disconnect()
