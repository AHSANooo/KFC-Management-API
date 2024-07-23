# KFC-Management-API

This project is a FastAPI-based web application designed to simulate a KFC restaurant's management system. The application handles products, inventory, orders, and authentication, ensuring a realistic and efficient management experience. It utilizes JSON data handling and includes comprehensive input validation and logging.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Additional Information](#additional-information)

## Introduction

Welcome to the KFC Management System! This project aims to provide a robust and flexible system for managing products, inventory, and orders in a simulated KFC restaurant environment. The application is designed for ease of use and modularity, ensuring it can be easily extended and maintained.

## Features

- Manages products with detailed information including price, components, and discounts.
- Handles inventory updates and checks for product availability based on component stock.
- Processes customer orders and calculates applicable discounts.
- Utilizes JSON for flexible data handling.
- Ensures correct user inputs with comprehensive validation.
- Implements authentication to secure endpoints.
- Provides RESTful API endpoints for integration and scalability.

## Installation

### Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

### Setup

Clone the repository:

```sh
git clone https://github.com/AHSANooo/KFC-Management-API.git
cd kfc-management-system
```



### Install required packages:

```sh
pip install -r requirements.txt
```

Ensure your data files are correctly placed in the config directory.

### How to Use

Run the application:

```sh

uvicorn main:app --reload
```
Access the application at: 
```sh
http://127.0.0.1:8000.
```
The application provides API endpoints for managing products, inventory, and orders. Use a tool like Postman or cURL to interact with the API.

### Additional Information

The application is designed with modularity in mind, allowing easy extension and maintenance.
It uses a service locator pattern for flexible and scalable management of data adapters and other services.
Comprehensive logging and validation ensure a smooth and error-free user experience.

Feel free to explore and modify the code to suit your specific needs!

Feel free to customize the repository URL and any other details specific to your project.
