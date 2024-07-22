# src/managers/order_manager.py
from datetime import datetime
from typing import List, Dict
from src.core.file_loader import FileLoader
from src.core.file_saver import FileSaver
from src.core.service_locator import ServiceLocator

class OrderManager:
    def __init__(self, orders_dir: str, service_locator: ServiceLocator):
        self.orders_dir = orders_dir
        self.data_adapter = service_locator.get_data_adapter(self.orders_dir)
        self.file_loader = FileLoader(self.data_adapter)
        self.file_saver = FileSaver(self.data_adapter)
        self.orders = self.load_orders()

    def load_orders(self) -> List[Dict]:
        """
        Load orders from the file.

        Returns:
            list: List of orders.
        """
        try:
            orders = self.file_loader.load()
            if not isinstance(orders, list):
                orders = []
            return orders
        except FileNotFoundError:
            print('File not found')
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def save_orders(self):
        """
        Save orders to the file.
        """
        try:
            self.file_saver.save(self.orders)
        except Exception as e:
            print(f"Error saving orders: {e}")

    def place_order(self, customer_name: str, selected_items: List[str], payment_method: str, total: float,
                    total_discount: float, total_after_discount: float):
        """
        Place an order and store it.

        Args:
            customer_name (str): Name of the customer.
            selected_items (list): List of selected items.
            payment_method (str): Payment method used.
            total (float): Total amount before discount.
            total_discount (float): Total discount applied.
            total_after_discount (float): Total amount after discount.
        """
        order = {
            'customer_name': customer_name,
            'selected_items': selected_items,
            'payment_method': payment_method,
            'total': total,
            'total_discount': total_discount * 100,
            'total_after_discount': total_after_discount,
            'Datetime': datetime.now().strftime('%Y-%m-%d %H:%M'),
        }
        self.orders.append(order)
        self.save_orders()

    def get_order_count(self, customer_name: str) -> int:
        """
        Get the count of orders placed by a customer.

        Args:
            customer_name (str): Name of the customer.

        Returns:
            int: Number of orders placed by the customer.
        """
        return sum(1 for order in self.orders if order.get('customer_name') == customer_name)
