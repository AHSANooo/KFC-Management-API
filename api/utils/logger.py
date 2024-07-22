# api/utils/logger.py
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.info("This is an info message")
# logger.error("This is an error message")
