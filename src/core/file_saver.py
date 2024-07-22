class FileSaver:
    def __init__(self, data_adapter):
        self.data_adapter = data_adapter

    def save(self, data):
        self.data_adapter.connect()
        self.data_adapter.save(data)
        self.data_adapter.disconnect()
