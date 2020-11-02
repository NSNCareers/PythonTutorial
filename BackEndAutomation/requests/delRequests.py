import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *


class DelShoppingData:

    endPointResource = ApiEndpoints.ShoppingAppEndPoint3

    def deleteExistingShoppingCart(self, Id):
        url = (
            getValueFromPropertiesFile("API", "shoppingAppUrl") + self.endPointResource
        )
        urlId = "{0}{1}".format(url, Id)
        results = requests.delete(urlId)
        return results