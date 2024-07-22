from typing import Dict
from ..core.file_loader import FileLoader
from ..core.file_saver import FileSaver
from ..core.service_locator import ServiceLocator

class ProductManager:
    def __init__(self, products_file: str, service_locator: ServiceLocator):
        self.products_file = products_file
        self.data_adapter = service_locator.get_data_adapter(self.products_file)
        self.file_loader = FileLoader(self.data_adapter)
        self.file_saver = FileSaver(self.data_adapter)
        self.products = self.load_products()

    def load_products(self) -> Dict[str, Dict]:
        try:
            products = self.file_loader.load()
            return products
        except Exception as e:
            print(f"Error loading products: {e}")
            return {}

    def save_products(self):
        try:
            self.file_saver.save(self.products)
        except Exception as e:
            print(f"Error saving products: {e}")

    def get_products(self) -> Dict[str, Dict]:
        return self.products

    def add_product(self, product_id: str, product_data: Dict):
        self.products[product_id] = product_data
        self.save_products()

    def remove_product(self, product_id: str):
        if product_id in self.products:
            del self.products[product_id]
            self.save_products()
        else:
            print(f"Product ID {product_id} not found")

    def update_product(self, product_id: str, product_data: Dict):
        if product_id in self.products:
            self.products[product_id].update(product_data)
            self.save_products()
        else:
            print(f"Product ID {product_id} not found")
