import mysql.connector
from prettytable import PrettyTable

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

def print_table(cursor, query, table_name):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    table = PrettyTable(columns)
    table.add_rows(rows)
    print(f"\nTable: {table_name}")
    print(table)

# Виведення даних кожної таблиці
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    # Виведення даних таблиці
    print_table(cursor, f"SELECT * FROM {table_name};", f"Data in {table_name}")

# Виконання кількох запитів
queries = [
    """
    SELECT Sales.*, Clients.FirmName
    FROM Sales
    JOIN Clients ON Sales.ClientID = Clients.ClientID
    WHERE Sales.PaymentForm = 'готівковий'
    ORDER BY Clients.FirmName;
    """,
    """
    SELECT Sales.*
    FROM Sales
    WHERE Sales.NeedDelivery = 1;
    """,
    """
    SELECT Clients.FirmName, 
        SUM(CASE WHEN Sales.PaymentForm = 'готівковий' THEN (Sales.QuantitySold * Products.Price * (1 - Sales.Discount / 100)) ELSE 0 END) AS TotalAmount
    FROM Sales
    JOIN Clients ON Sales.ClientID = Clients.ClientID
    JOIN Products ON Sales.ProductID = Products.ProductID
    GROUP BY Clients.FirmName;
    """,
    """
    SELECT Sales.*, Clients.FirmName
    FROM Sales
    JOIN Clients ON Sales.ClientID = Clients.ClientID
    WHERE Sales.ClientID = 4;
    """,
    """
    SELECT Clients.FirmName, COUNT(*) AS PurchaseCount
    FROM Sales
    JOIN Clients ON Sales.ClientID = Clients.ClientID
    GROUP BY Clients.FirmName;
    """,
    """
    SELECT Clients.FirmName, 
       SUM(CASE WHEN Sales.PaymentForm = 'готівковий' THEN (Sales.QuantitySold * Products.Price) ELSE 0 END) AS CashTotal,
       SUM(CASE WHEN Sales.PaymentForm = 'безготівковий' THEN (Sales.QuantitySold * Products.Price) ELSE 0 END) AS NonCashTotal
    FROM Sales
    JOIN Clients ON Sales.ClientID = Clients.ClientID
    JOIN Products ON Sales.ProductID = Products.ProductID
    GROUP BY Clients.FirmName;
    """
]

for idx, query in enumerate(queries, 1):
    print_table(cursor, query, f"Query {idx}")

# Закриття підключення
cursor.close()
connection.close()
