import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *
from BackEndAutomation.requestAuth.authentication import *


class PutShoppingData:

    endPointResource = ApiEndpoints.ShoppingAppEndPoint3

    def createNewShoppingCart(self, tokenId):
        auth = BearerAuth().getToken(tokenId)
        with open("BackEndAutomation/testData/putData.json", "r") as file:
            # json.Loads() converts string to dictionary
            # json.Load() converts file to dictionary
            contentDict = json.load(file)
            contentJson = json.dumps(contentDict)
            url = (
                getValueFromPropertiesFile(None, "API", "shoppingAppUrl")
                + self.endPointResource
            )
            content = requests.put(url, data=contentJson, headers=auth, verify=True)
            return content


var = PutShoppingData().createNewShoppingCart(234)
print(var)