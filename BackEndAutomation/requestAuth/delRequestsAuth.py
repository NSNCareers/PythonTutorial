import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *
from BackEndAutomation.requestAuth.authentication import *


class DelShoppingDataAuth:

    endPointResource = ApiEndpoints.ShoppingAppEndPointV1

    def deleteExistingShoppingCart(self, Id):
        auth = BearerAuth().getToken(Id)
        url = (
            getValueFromPropertiesFile("API", "shoppingAppUrl") + self.endPointResource
        )
        urlId = "{0}{1}".format(url, Id)
        results = requests.delete(urlId, headers=auth, verify=True)
        return results