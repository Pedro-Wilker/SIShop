import sqlite3 

connection = sqlite3.connect("sishop.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL UNIQUE,
        Office VARCHAR(255) NOT NULL,
        Salary FLOAT NOT NULL,
        Password VARCHAR(255) NOT NULL,
        Phone VARCHAR(20),  -- Alterado para VARCHAR para acomodar números de telefone
        Birth DATE
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(255) NOT NULL,
        Cod_Product INTEGER NOT NULL UNIQUE,
        Bar_Cod INTEGER NOT NULL UNIQUE,
        Price_Buy REAL NOT NULL,  -- Alterado para REAL
        Price_Sale REAL NOT NULL  -- Removida a vírgula extra
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS financier(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Cash_Reserve REAL NOT NULL,  -- Alterado para REAL
        Gain INTEGER,
        Expense INTEGER,
        Id_Product INTEGER NOT NULL,
        FOREIGN KEY (Id_Product) REFERENCES products(Id)  -- Definindo chave estrangeira corretamente
    );
""")

print("Connecting to database is successful")