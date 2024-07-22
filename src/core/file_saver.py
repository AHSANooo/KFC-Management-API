# src/core/file_saver.py
class FileSaver:
    def __init__(self, data_adapter):
        """
        Initialize the FileSaver with a data adapter.

        Args:
            data_adapter (DataAdapter): The data adapter to use for saving.
        """
        self.data_adapter = data_adapter

    def save(self, data):
        """
        Save data using the data adapter.

        Args:
            data (any): Data to save.
        """
        self.data_adapter.connect()
        try:
            self.data_adapter.save(data)
        except Exception as e:
            raise RuntimeError(f"Error saving data: {e}")
        finally:
            self.data_adapter.disconnect()
