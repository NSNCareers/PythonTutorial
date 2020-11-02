import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *


class PostShoppingData:

    endPointResource = ApiEndpoints.ShoppingAppEndPoint3

    def updateExistingShoppingCart(self):
        with open("src/appData/postData.json", "r") as file:
            # json.Loads() converts string to dictionary
            # json.Load() converts file to dictionary
            contentDict = json.load(file)
            contentJson = json.dumps(contentDict).replace("'", "")
            url = (
                getValueFromPropertiesFile("API", "shoppingAppUrl")
                + self.endPointResource
            )
            content = requests.post(url, contentJson)
            return content