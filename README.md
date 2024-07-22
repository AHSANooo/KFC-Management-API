# KFC Order Management CLI App

This project is a Python-based CLI application designed to simulate a KFC restaurant's order management system. The application handles products, inventory, and discounts, ensuring a realistic and efficient order management experience. It utilizes JSON and CSV data handling and includes comprehensive input validation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Additional Information](#additional-information)

## Introduction

Welcome to the KFC Order Management CLI App! This project aims to provide a robust and flexible system for managing orders, inventory, and discounts in a simulated KFC restaurant environment. The application is designed for ease of use and modularity, ensuring it can be easily extended and maintained.

## Features

- Manages products with detailed information including price, components, and discounts.
- Handles inventory updates and checks for product availability based on component stock.
- Processes customer orders and calculates applicable discounts.
- Utilizes JSON and CSV for flexible data handling.
- Ensures correct user inputs with comprehensive validation.

## Installation

### Requirements

Before running the application, ensure you have the following installed:

- Python 3.x

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/kfc-order-management-cli.git
    cd kfc-order-management-cli
    ```

2. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure your data files are correctly placed in the `config` directory.

## How to Use

1. Run the application:
    ```sh
    python main.py
    ```

2. Follow the prompts to place orders, manage inventory, and apply discounts.

3. The system will guide you through the order process, from selecting items to finalizing the payment.

## Additional Information

- The application is designed with modularity in mind, allowing easy extension and maintenance.
- It uses a service locator pattern for flexible and scalable management of data adapters and other services.
- Comprehensive logging and validation ensure a smooth and error-free user experience.

Feel free to explore and modify the code to suit your specific needs!
