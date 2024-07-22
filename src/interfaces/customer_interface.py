from collections import Counter
from datetime import datetime
from src.managers.inventory_manager import InventoryManager
from src.managers.order_manager import OrderManager
from src.managers.product_manager import ProductManager
from src.managers.discount_manager import DiscountManager
from src.core.input_validator import InputValidator

class CustomerInterface:
    def __init__(self, orders_dir: str, products_dir: str, inventory_dir: str, service_locator):
        self.inventory_manager = InventoryManager(inventory_dir, service_locator)
        self.order_manager = OrderManager(orders_dir, service_locator)
        self.product_manager = ProductManager(products_dir, service_locator)
        self.customer_name = ""

    def start(self):
        self.welcome_screen()
        selected_items = self.select_items()
        if selected_items:
            payment_method = self.payment_method()
            total, discount, total_after_discount = self.apply_discounts(selected_items, payment_method)
            self.store_order(selected_items, payment_method, total_after_discount, discount, total)

    def welcome_screen(self):
        print("Welcome to KFC!\n")
        self.customer_name = input("Please enter your full name: ").strip().upper()
        while not InputValidator.validate_name(self.customer_name):
            print("\nInvalid input. Please enter a valid name.")
            self.customer_name = input("Please enter your full name: ").strip().upper()

    def get_available_items(self):
        available_items = {}
        for item, details in self.product_manager.get_products().items():
            if self.are_components_available(details['components']):
                available_items[item] = details
        return available_items

    def are_components_available(self, components):
        for component, count in components.items():
            if self.inventory_manager.get_available_quantity(component) < count:
                return False
        return True

    def select_items(self):
        selected_items = []
        available_items = self.get_available_items()

        if not available_items:
            print("\nSorry, no items are available at the moment.")
            return selected_items

        while True:
            print("\nAvailable items:")
            index = 1
            item_map = {}
            for item, details in available_items.items():
                price_info = f"Rs.{details['price']}"
                if 'discount' in details:
                    price_info += f" (Discount: {details['discount']}%)"
                print(f"{index}. {item}: {price_info}")
                item_map[index] = item
                index += 1

            print(f"{index}. Done")
            choice = input("\nEnter your choice (number): ").strip()
            if not InputValidator.validate_choice(choice, index):
                print("\nInvalid choice. Please enter a valid number.")
                continue

            if choice == str(index):
                break

            selected_item = item_map[int(choice)]
            selected_items.append(selected_item)
            print(f"{selected_item} added to cart.")
            self.update_inventory(selected_item)

        return selected_items

    def update_inventory(self, selected_item):
        components = self.product_manager.get_products()[selected_item]['components']
        for component, count in components.items():
            self.inventory_manager.update_inventory(component, count)

    def payment_method(self):
        payment_method = input("\nEnter payment method: \n1. Card\n2. Cash\n").strip().lower()
        while not InputValidator.validate_payment_method(payment_method):
            print("\nInvalid payment method. Please enter 1 or 2.")
            payment_method = input("\nEnter payment method: \n1. Card\n2. Cash\n").strip().lower()
        return payment_method

    def apply_discounts(self, selected_items, payment_method):
        total, discount, total_after_discount = DiscountManager.apply_discounts(
            selected_items,
            self.product_manager.get_products(),
            payment_method,
            self.order_manager.get_order_count(self.customer_name)
        )
        return total, discount, total_after_discount

    def store_order(self, selected_items, payment_method, total_after_discount, total_discount, total):
        self.order_manager.place_order(
            self.customer_name,
            selected_items,
            payment_method,
            total,
            total_discount,
            total_after_discount
        )
        item_summary = Counter(selected_items)
        item_summary_str = ', '.join(f"{item} x {count}" for item, count in item_summary.items())
        print("Order placed successfully!")
        print(f"Customer Name: {self.customer_name}")
        print(f"Items: {item_summary_str}")
        print(f"Payment Method: {payment_method.capitalize()}")
        print(f"Total Bill: Rs.{total}/-")
        print(f"Discount Applied: {total_discount * 100}%")
        print(f"Total Amount to be Paid: Rs.{total_after_discount:.2f}/-")
        print(f"Date and Time: {datetime.now().strftime('%Y-%m-%d   %H:%M')}")

