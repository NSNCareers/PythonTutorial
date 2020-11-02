class Cart:
    def getShoppingCart(self, IdUpdate, customerName):
        shioppingCart = {
            "Id": IdUpdate,
            "Gender": "Male",
            "Item": [
                {
                    "Id": IdUpdate,
                    "CartId": IdUpdate,
                    "ItemName": customerName,
                    "Size": 1,
                    "Weight": 2,
                    "Seller": "string",
                }
            ],
            "CustomerName": "string",
            "OrderQuantity": "string",
            "Price": 3,
            "Address": {
                "Id": IdUpdate,
                "CartId": IdUpdate,
                "Street": "string",
                "HouseNumber": 40,
                "PostCode": "string",
                "Town": "string",
            },
            "Message": "my name is " + customerName,
        }
        return shioppingCart