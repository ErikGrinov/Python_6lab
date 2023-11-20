import mysql.connector

# Параметри підключення до бази даних
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "mypassword",
    "database": "mydatabase"
}

# Створення підключення
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Додавання реальних даних у таблицю "Клієнти"
insert_clients_data_query = """
INSERT INTO Clients (FirmName, LegalEntity, Address, Phone, ContactPerson, BankAccount)
VALUES
    ('ABC Electronics', 'юридична', '123 Main St, CityA, CountryA', '+123456789012', 'John Doe', '12345678901234567890'),
    ('XYZ Retail', 'фізична', '456 Oak St, CityB, CountryB', '+198765432109', 'Jane Smith', '09876543210987654321'),
    ('Tech Solutions LLC', 'юридична', '789 Maple St, CityC, CountryC', '+112233445511', 'Alex Johnson', '11223344551122334455'),
    ('Best Deals Co.', 'фізична', '101 Pine St, CityD, CountryD', '+554433221155', 'Emily Brown', '55443322115544332211')
"""
cursor.execute(insert_clients_data_query)

# Додавання реальних даних у таблицю "Товари"
insert_products_data_query = """
INSERT INTO Products (ProductName, Price, QuantityInStock)
VALUES
    ('Laptop', 899.99, 50),
    ('Smartphone', 499.99, 100),
    ('Smart TV', 699.99, 30),
    ('Wireless Headphones', 129.99, 80),
    ('Digital Camera', 299.99, 40),
    ('Tablet', 349.99, 60),
    ('Gaming Console', 449.99, 20),
    ('Fitness Tracker', 79.99, 150),
    ('Bluetooth Speaker', 59.99, 120),
    ('External Hard Drive', 129.99, 50)
"""
cursor.execute(insert_products_data_query)

# Додавання реальних даних у таблицю "Продаж товарів"
insert_sales_data_query = """
INSERT INTO Sales (SaleDate, ClientID, ProductID, QuantitySold, Discount, PaymentForm, NeedDelivery, DeliveryCost)
VALUES
    ('2023-01-05', 1, 3, 5, 10.0, 'готівковий', 1, 15.00),
    ('2023-02-12', 2, 1, 8, 5.5, 'безготівковий', 0, NULL),
    ('2023-03-20', 3, 5, 15, 8.2, 'готівковий', 1, 20.00),
    ('2023-04-03', 4, 2, 10, 15.0, 'безготівковий', 0, NULL),
    ('2023-05-17', 1, 7, 12, 12.5, 'готівковий', 0, NULL),
    ('2023-06-22', 2, 9, 18, 6.8, 'безготівковий', 1, 25.00),
    ('2023-07-08', 3, 4, 6, 3.0, 'готівковий', 1, 18.00),
    ('2023-08-14', 4, 6, 20, 17.5, 'безготівковий', 0, NULL),
    ('2023-09-19', 1, 8, 7, 9.0, 'готівковий', 0, NULL),
    ('2023-10-25', 2, 10, 14, 11.2, 'безготівковий', 1, 22.00),
    ('2023-11-30', 3, 3, 9, 6.0, 'готівковий', 0, NULL),
    ('2023-12-10', 4, 5, 11, 14.8, 'безготівковий', 1, 30.00),
    ('2024-01-15', 1, 1, 13, 13.3, 'готівковий', 1, 15.00),
    ('2024-02-20', 2, 2, 16, 16.7, 'безготівковий', 0, NULL),
    ('2024-03-25', 3, 6, 8, 8.8, 'готівковий', 0, NULL),
    ('2024-04-03', 4, 9, 19, 19.5, 'безготівковий', 1, 25.00),
    ('2024-05-10', 1, 10, 10, 10.0, 'готівковий', 1, 18.00),
    ('2024-06-15', 2, 8, 14, 14.5, 'безготівковий', 0, NULL),
    ('2024-07-20', 3, 7, 7, 7.2, 'готівковий', 1, 22.00),
    ('2024-08-25', 4, 4, 12, 12.8, 'безготівковий', 0, NULL)
"""
cursor.execute(insert_sales_data_query)

# Підтвердження змін
connection.commit()

# Закриття підключення
cursor.close()
connection.close()
