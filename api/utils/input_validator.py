# api/utils/input_validator.py
from pydantic import BaseModel, ValidationError
from typing import Any

class InputValidator:
    @staticmethod
    def validate_model(model: BaseModel, data: Any) -> BaseModel:
        try:
            validated_data = model(**data)
            return validated_data
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")

# Example usage:
# validated_product = InputValidator.validate_model(Product, product_data)
