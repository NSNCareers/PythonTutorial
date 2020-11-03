import pyodbc
from BackEndAutomation.utilities.configuration import *

cnxn = getSQLConnection("shoppingCartDB")
cursor = cnxn.cursor()


class DBRequests:
    def db_Querry(self):

        # Sample select query
        cursor.execute("select * from dbo.ShoppingCarts")
        row = cursor.fetchone()
        # fetch all data
        rows = cursor.fetchall()
        # print(getAll)
        # print(getAll[2])
        # Retrive first data
        # print(row)
        # Retrive second coloumn
        # print(rows[0])
        # gets all columns and iterates through
        for r in rows:
            if r[0] == 5002:
                indexThree = r[2]
                print(indexThree)
        cnxn.close()

    def insert_Querry(self):
        # Sample insert query
        cursor.execute(
            """
        INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) 
        VALUES (?,?,?,?,?)""",
            "SQL Server Express New 20",
            "SQLEXPRESS New 20",
            0,
            0,
            pyodbc.Timestamp,
        )
        cnxn.commit()
        row = cursor.fetchone()

        while row:
            print("Inserted Product key is " + str(row[0]))
            row = cursor.fetchone()
        cnxn.close()


if __name__ == "__main__":
    var = DBRequests().db_Querry()
