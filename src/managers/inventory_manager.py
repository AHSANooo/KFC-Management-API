# src/managers/inventory_manager.py
from typing import Dict
from ..core.file_loader import FileLoader
from ..core.file_saver import FileSaver
from ..core.service_locator import ServiceLocator

class InventoryManager:
    def __init__(self, inventory_dir: str, service_locator: ServiceLocator):
        self.inventory_dir = inventory_dir
        self.data_adapter = service_locator.get_data_adapter(self.inventory_dir)
        self.file_loader = FileLoader(self.data_adapter)
        self.file_saver = FileSaver(self.data_adapter)
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, int]:
        """
        Load inventory from the file.

        Returns:
            dict: Dictionary of inventory items with their quantities.
        """
        try:
            inventory = self.file_loader.load()
            return inventory
        except Exception as e:
            print(f"Error loading inventory: {e}")
            return {}

    def save_inventory(self):
        """
        Save inventory to the file.
        """
        try:
            self.file_saver.save(self.inventory)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def update_inventory(self, product_id: str, quantity: int):
        """
        Update the inventory with the given product ID and quantity.

        Args:
            product_id (str): Product ID to be updated.
            quantity (int): Quantity to be updated.
        """
        if product_id in self.inventory:
            self.inventory[product_id] -= quantity
            if self.inventory[product_id] <= 0:
                del self.inventory[product_id]
        else:
            self.inventory[product_id] = -quantity
        self.save_inventory()

    def check_availability(self, product_id: str, quantity: int) -> bool:
        """
        Check if the given quantity of the product is available in the inventory.

        Args:
            product_id (str): Product ID to check.
            quantity (int): Quantity to check.

        Returns:
            bool: True if available, False otherwise.
        """
        return self.inventory.get(product_id, 0) >= quantity

    def get_available_quantity(self, component: str) -> int:
        """
        Get the available quantity of the given component.

        Args:
            component (str): Component to check.

        Returns:
            int: Available quantity of the component.
        """
        return self.inventory.get(component, 0)
