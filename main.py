import os
from src.interfaces.customer_interface import CustomerInterface
from src.core.service_locator import ServiceLocator


def list_files_in_directory(directory_path):
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        if not files:
            print(f"No files found in directory: {directory_path}")
            return files
        return files
    except FileNotFoundError:
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")


def main():
    # Initialize service locator
    service_locator = ServiceLocator()

    # Directories for data files
    orders_dir_path = "config/orders"
    products_dir_path = "config/products"
    inventory_dir_path = "config/inventory"

    # Get files from directories
    order_files = list_files_in_directory(orders_dir_path)
    product_files = list_files_in_directory(products_dir_path)
    inventory_files = list_files_in_directory(inventory_dir_path)

    if not order_files:
        print("No order files found.")
        orders_file = None
    else:
        orders_file = os.path.join(orders_dir_path, order_files[0])

        if not product_files:
            print("No product files found.")
            return
        products_file = os.path.join(products_dir_path, product_files[0])

    if not inventory_files:
        print("No inventory files found.")
        inventory_file = None
    else:
        inventory_file = os.path.join(inventory_dir_path, inventory_files[0])

    # Create CustomerInterface instance
    customer_interface = CustomerInterface(orders_file, products_file, inventory_file, service_locator)

    # Start the application
    customer_interface.start()


if __name__ == "__main__":
    main()
