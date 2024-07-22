# src/utils/logger.py
import logging

class Logger:
    @staticmethod
    def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
        """
        Setup a logger for the application.

        Args:
            name (str): The name of the logger.
            log_file (str): The file to which logs will be written.
            level (int): The logging level (e.g., logging.DEBUG, logging.INFO).

        Returns:
            logging.Logger: Configured logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def log_info(logger: logging.Logger, message: str):
        """
        Log an informational message.

        Args:
            logger (logging.Logger): The logger to use.
            message (str): The message to log.
        """
        logger.info(message)

    @staticmethod
    def log_error(logger: logging.Logger, message: str):
        """
        Log an error message.

        Args:
            logger (logging.Logger): The logger to use.
            message (str): The message to log.
        """
        logger.error(message)

    @staticmethod
    def log_debug(logger: logging.Logger, message: str):
        """
        Log a debug message.

        Args:
            logger (logging.Logger): The logger to use.
            message (str): The message to log.
        """
        logger.debug(message)
