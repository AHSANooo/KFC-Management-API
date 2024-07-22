class FileLoader:
    def __init__(self, data_adapter):
        self.data_adapter = data_adapter

    def load(self):
        self.data_adapter.connect()
        data = self.data_adapter.load()
        self.data_adapter.disconnect()
        return data
