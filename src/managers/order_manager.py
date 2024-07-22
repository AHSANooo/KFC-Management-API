from datetime import datetime
from typing import List, Dict
from src.core.file_loader import FileLoader
from src.core.file_saver import FileSaver
from src.core.service_locator import ServiceLocator


# from config.adapters.adapters import DataAdapterFactory

class OrderManager:
    def __init__(self, orders_dir: str, service_locator: ServiceLocator):
        self.file_path = orders_dir
        self.orders_dir = orders_dir
        self.data_adapter = service_locator.get_data_adapter(self.orders_dir)
        self.service_locator = service_locator
        self.file_loader = FileLoader(self.data_adapter)
        self.file_saver = FileSaver(self.data_adapter)
        self.orders = self.load_orders()

    def load_orders(self):
        loader = self.service_locator.get_data_adapter(self.file_path)
        if loader is None:
            print('No data adapter found for the given file path')
            return []  # Return an empty list or handle as appropriate

        try:
            orders = loader.load()
            if not isinstance(orders, list):
                orders = []
            return orders
        except FileNotFoundError:
            print('File not found')
            return []  # Return an empty list or handle as appropriate
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []  # Return an empty list or handle as appropriate
    def save_orders(self):
        try:
            loader = self.service_locator.get_data_adapter(self.file_path)
            loader.save_order(self.orders)
        except Exception as e:
            print(f"Error saving orders: {e}")

    def place_order(self, customer_name: str, selected_items: List[str], payment_method: str, total: float,
                    total_discount: float, total_after_discount: float):
        order = {
            'customer_name': customer_name,
            'selected_items': selected_items,
            'payment_method': payment_method,
            'total': total,
            'total_discount': total_discount*100,
            'total_after_discount': total_after_discount,
            'Datetime': datetime.now().strftime('%Y-%m-%d   %H:%M'),
        }
        self.orders.append(order)
        self.save_orders()

    def get_order_count(self, customer_name: str) -> int:
        count = sum(1 for order in self.orders if order.get('customer_name') == customer_name)
        return count
