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

# Визначення типів даних та створення таблиці "Клієнти"
create_clients_table_query = """
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    FirmName VARCHAR(255) NOT NULL,
    LegalEntity ENUM('юридична', 'фізична') NOT NULL,
    Address VARCHAR(255),
    Phone VARCHAR(20) COMMENT 'маска вводу',
    ContactPerson VARCHAR(255),
    BankAccount VARCHAR(20)
)
"""
cursor.execute(create_clients_table_query)

# Визначення типів даних та створення таблиці "Товари"
create_products_table_query = """
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    QuantityInStock INT NOT NULL
)
"""
cursor.execute(create_products_table_query)

# Визначення типів даних та створення таблиці "Продаж товарів"
create_sales_table_query = """
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    SaleDate DATE NOT NULL,
    ClientID INT,
    ProductID INT,
    QuantitySold INT NOT NULL,
    Discount DECIMAL(4, 2) CHECK (Discount >= 3 AND Discount <= 20),
    PaymentForm ENUM('готівковий', 'безготівковий') NOT NULL,
    NeedDelivery BOOLEAN,
    DeliveryCost DECIMAL(10, 2),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
"""
cursor.execute(create_sales_table_query)

# Підтвердження змін
connection.commit()

# Закриття підключення
cursor.close()
connection.close()