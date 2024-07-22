# src/utils/input_validator.py
import re
from typing import Any

class InputValidator:
    @staticmethod
    def is_non_empty_string(value: str) -> bool:
        """
        Check if the value is a non-empty string.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if value is a non-empty string, False otherwise.
        """
        return isinstance(value, str) and bool(value.strip())

    @staticmethod
    def is_positive_integer(value: Any) -> bool:
        """
        Check if the value is a positive integer.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if value is a positive integer, False otherwise.
        """
        return isinstance(value, int) and value > 0

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Check if the email is valid.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if email is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_payment_method(method: str) -> bool:
        """
        Check if the payment method is valid.

        Args:
            method (str): The payment method to check ('card' or 'cash').

        Returns:
            bool: True if payment method is valid, False otherwise.
        """
        return method in ['card', 'cash']

    @staticmethod
    def is_valid_product_data(data: dict) -> bool:
        """
        Validate the product data dictionary.

        Args:
            data (dict): Product data dictionary.

        Returns:
            bool: True if product data is valid, False otherwise.
        """
        required_keys = ['name', 'price']
        if not all(key in data for key in required_keys):
            return False
        if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
            return False
        if 'discount' in data and not isinstance(data['discount'], (int, float)):
            return False
        return True
