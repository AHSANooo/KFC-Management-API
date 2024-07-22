# src/managers/product_manager.py
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
        """
        Load products from the file.

        Returns:
            dict: Dictionary of products with their details.
        """
        try:
            products = self.file_loader.load()
            return products
        except Exception as e:
            print(f"Error loading products: {e}")
            return {}

    def save_products(self):
        """
        Save products to the file.
        """
        try:
            self.file_saver.save(self.products)
        except Exception as e:
            print(f"Error saving products: {e}")

    def get_products(self) -> Dict[str, Dict]:
        """
        Get the dictionary of products.

        Returns:
            dict: Dictionary of products.
        """
        return self.products

    def add_product(self, product_id: str, product_data: Dict):
        """
        Add a new product or update an existing product.

        Args:
            product_id (str): ID of the product to be added or updated.
            product_data (dict): Data of the product.
        """
        self.products[product_id] = product_data
        self.save_products()

    def remove_product(self, product_id: str):
        """
        Remove a product by its ID.

        Args:
            product_id (str): ID of the product to be removed.
        """
        if product_id in self.products:
            del self.products[product_id]
            self.save_products()
        else:
            print(f"Product ID {product_id} not found")

    def update_product(self, product_id: str, product_data: Dict):
        """
        Update an existing product.

        Args:
            product_id (str): ID of the product to be updated.
            product_data (dict): Data to update.
        """
        if product_id in self.products:
            self.products[product_id].update(product_data)
            self.save_products()
        else:
            print(f"Product ID {product_id} not found")
