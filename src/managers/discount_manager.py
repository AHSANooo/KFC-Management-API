# src/managers/discount_manager.py
from typing import List, Dict

class DiscountManager:
    @staticmethod
    def apply_discounts(selected_items: List[str], products: Dict[str, Dict], payment_method: str, order_count: int) -> (float, float, float):
        """
        Apply discounts based on selected items, payment method, and order count.

        Args:
            selected_items (list): List of selected item IDs.
            products (dict): Dictionary of products with their details.
            payment_method (str): Payment method used ('1' for card, '2' for cash).
            order_count (int): Number of orders placed by the customer.

        Returns:
            tuple: Total amount, discount applied, and total after discount.
        """
        total = sum(products[item]['price'] for item in selected_items)
        discount = 0

        if payment_method == '1':
            payment_method = 'card'
            discount += 0.05
        elif payment_method == '2':
            payment_method = 'cash'

        if order_count > 0:
            discount += 0.027
            if order_count > 10:
                discount += 0.12
                discount -= 0.027

        for item in selected_items:
            if 'discount' in products[item]:
                item_discount = products[item]['discount'] / 100
                total -= products[item]['price'] * item_discount

        total_after_discount = total * (1 - discount)
        return total, discount, total_after_discount
