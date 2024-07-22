# src/interfaces/customer_interface.py
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
        """
        Start the customer interface, displaying the welcome screen and handling item selection and payment.
        """
        self.welcome_screen()
        selected_items = self.select_items()
        if selected_items:
            payment_method = self.payment_method()
            total, discount, total_after_discount = self.apply_discounts(selected_items, payment_method)
            self.store_order(selected_items, payment_method, total_after_discount, discount, total)

    def welcome_screen(self):
        """
        Display the welcome screen and prompt the user for their name.
        """
        print("Welcome to KFC!\n")
        self.customer_name = input("Please enter your full name: ").strip().upper()
        while not InputValidator.validate_name(self.customer_name):
            print("\nInvalid input. Please enter a valid name.")
            self.customer_name = input("Please enter your full name: ").strip().upper()

    def get_available_items(self):
        """
        Get the list of available items based on the current inventory.

        Returns:
            dict: A dictionary of available items with their details.
        """
        available_items = {}
        for item, details in self.product_manager.get_products().items():
            if self.are_components_available(details['components']):
                available_items[item] = details
        return available_items

    def are_components_available(self, components):
        """
        Check if all components for an item are available in the inventory.

        Args:
            components (dict): Dictionary of components and their required quantities.

        Returns:
            bool: True if all components are available, False otherwise.
        """
        for component, count in components.items():
            if self.inventory_manager.get_available_quantity(component) < count:
                return False
        return True

    def select_items(self):
        """
        Prompt the user to select items from the available options.

        Returns:
            list: A list of selected items.
        """
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
        """
        Update the inventory based on the selected item.

        Args:
            selected_item (str): The item that was selected.
        """
        components = self.product_manager.get_products()[selected_item]['components']
        for component, count in components.items():
            self.inventory_manager.update_inventory(component, count)

    def payment_method(self):
        """
        Prompt the user to select a payment method.

        Returns:
            str: The selected payment method.
        """
        payment_method = input("\nEnter payment method: \n1. Card\n2. Cash\n").strip().lower()
        while not InputValidator.validate_payment_method(payment_method):
            print("\nInvalid payment method. Please enter 1 or 2.")
            payment_method = input("\nEnter payment method: \n1. Card\n2. Cash\n").strip().lower()
        return payment_method

    def apply_discounts(self, selected_items, payment_method):
        """
        Apply discounts based on selected items and payment method.

        Args:
            selected_items (list): List of selected items.
            payment_method (str): Payment method used.

        Returns:
            tuple: A tuple containing the total amount, discount amount, and total amount after discount.
        """
        total, discount, total_after_discount = DiscountManager.apply_discounts(
            selected_items,
            self.product_manager.get_products(),
            payment_method,
            self.order_manager.get_order_count(self.customer_name)
        )
        return total, discount, total_after_discount

    def store_order(self, selected_items, payment_method, total_after_discount, total_discount, total):
        """
        Store the order and print the order summary.

        Args:
            selected_items (list): List of selected items.
            payment_method (str): Payment method used.
            total_after_discount (float): Total amount after applying discounts.
            total_discount (float): Discount amount.
            total (float): Total amount before applying discounts.
        """
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
