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

# 1. Відобразити всі продажі, які були оплачені готівкою. Відсортувати їх по назві клієнта за алфавітом;
query1 = """
SELECT Sales.*, Clients.FirmName
FROM Sales
JOIN Clients ON Sales.ClientID = Clients.ClientID
WHERE Sales.PaymentForm = 'готівковий'
ORDER BY Clients.FirmName;
"""
cursor.execute(query1)
result1 = cursor.fetchall()
print("Результат 1:")
for row in result1:
    print(row)

# 2. Відобразити всі продажі, по яких потрібна була доставка;
query2 = """
SELECT *
FROM Sales
WHERE NeedDelivery = 1;
"""
cursor.execute(query2)
result2 = cursor.fetchall()
print("\nРезультат 2:")
for row in result2:
    print(row)

# 3. Порахувати суму та суму з урахуванням скидки, яку треба сплатити кожному клієнту (запит з обчислювальним полем);
query3 = """
SELECT Clients.FirmName, 
       SUM(Sales.QuantitySold * Products.Price) AS TotalAmount,
       SUM(Sales.QuantitySold * (Products.Price - (Products.Price * Sales.Discount / 100))) AS TotalAmountWithDiscount
FROM Sales
JOIN Clients ON Sales.ClientID = Clients.ClientID
JOIN Products ON Sales.ProductID = Products.ProductID
GROUP BY Clients.FirmName;
"""
cursor.execute(query3)
result3 = cursor.fetchall()
print("\nРезультат 3:")
for row in result3:
    print(row)

# 4. Відобразити всі покупки вказаного клієнта (запит з параметром);
# Припустимо, що ми хочемо відобразити покупки для клієнта з ID = 1
client_id_param = 1
query4 = f"""
SELECT Sales.*, Clients.FirmName
FROM Sales
JOIN Clients ON Sales.ClientID = Clients.ClientID
WHERE Sales.ClientID = {client_id_param};
"""
cursor.execute(query4)
result4 = cursor.fetchall()
print("\nРезультат 4:")
for row in result4:
    print(row)

# 5. Порахувати кількість покупок, які зробив кожен клієнт (підсумковий запит);
query5 = """
SELECT Clients.FirmName, COUNT(*) AS PurchaseCount
FROM Sales
JOIN Clients ON Sales.ClientID = Clients.ClientID
GROUP BY Clients.FirmName;
"""
cursor.execute(query5)
result5 = cursor.fetchall()
print("\nРезультат 5:")
for row in result5:
    print(row)

# 6. Порахувати суму, яку сплатив кожен клієнт за готівковим та безготівковим розрахунком (перехресний запит);
query6 = """
SELECT Clients.FirmName, 
       SUM(CASE WHEN Sales.PaymentForm = 'готівковий' THEN (Sales.QuantitySold * Products.Price) ELSE 0 END) AS CashTotal,
       SUM(CASE WHEN Sales.PaymentForm = 'безготівковий' THEN (Sales.QuantitySold * Products.Price) ELSE 0 END) AS NonCashTotal
FROM Sales
JOIN Clients ON Sales.ClientID = Clients.ClientID
JOIN Products ON Sales.ProductID = Products.ProductID
GROUP BY Clients.FirmName;
"""
cursor.execute(query6)
result6 = cursor.fetchall()
print("\nРезультат 6:")
for row in result6:
    print(row)

# Закриття підключення
cursor.close()
connection.close()
