# src/core/input_validator.py
import re

class InputValidator:
    @staticmethod
    def validate_name(name):
        """
        Validate that the name contains only letters and spaces.

        Args:
            name (str): Name to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return re.match("^[A-Za-z ]+$", name) is not None

    @staticmethod
    def validate_choice(choice, options):
        """
        Validate that the choice is a digit and within the allowed range.

        Args:
            choice (str): Choice to validate.
            options (int): Maximum valid choice number.

        Returns:
            bool: True if valid, False otherwise.
        """
        return choice.isdigit() and 1 <= int(choice) <= options

    @staticmethod
    def validate_quantity(qty, max_qty):
        """
        Validate that the quantity is a digit and within the allowed range.

        Args:
            qty (str): Quantity to validate.
            max_qty (int): Maximum valid quantity.

        Returns:
            bool: True if valid, False otherwise.
        """
        return qty.isdigit() and 1 <= int(qty) <= max_qty

    @staticmethod
    def validate_payment_method(payment_method):
        """
        Validate that the payment method is valid.

        Args:
            payment_method (str): Payment method to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return payment_method in ['1', '2']
