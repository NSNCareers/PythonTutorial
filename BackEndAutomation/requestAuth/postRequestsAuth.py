import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *
from BackEndAutomation.requestAuth.authentication import *


class PostShoppingData:

    endPointResource = ApiEndpoints.ShoppingAppEndPoint3

    def updateExistingShoppingCart(self, tokenId):

        auth = BearerAuth().getToken(tokenId)
        with open("BackEndAutomation/testData/putData.json", "r") as file:
            # json.Loads() converts string to dictionary
            # json.Load() converts file to dictionary
            contentDict = json.load(file)
            contentJson = json.dumps(contentDict)
            Id = 4001
            name = "Hunter"

            url = (
                getValueFromPropertiesFile(None, "API", "shoppingAppUrl")
                + self.endPointResource
            )
            content = requests.post(url, data=contentJson, headers=auth, verify=True)
        return content


var = PostShoppingData().updateExistingShoppingCart(8760)
