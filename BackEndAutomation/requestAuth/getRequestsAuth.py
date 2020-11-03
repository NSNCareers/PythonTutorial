import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *
from BackEndAutomation.requestAuth.authentication import *


class GetShoppingData:

    endPointResource = ApiEndpoints.ShoppingAppEndPointV1
    endPointResource2 = ApiEndpoints.ShoppingAppEndPointV2

    # https://www.youtube.com/watch?v=06I63_p-2A4
    # https://stackoverflow.com/questions/46520127/vscode-import-error-for-python-module

    def getAllFromShoppingCart(self, tokenId):

        auth = BearerAuth().getToken(tokenId)
        url = (
            getValueFromPropertiesFile(None, "API", "shoppingAppUrl")
            + self.endPointResource
        )
        content = requests.get(url, headers=auth, verify=True)
        return content

    def getShoppingCartWithId(self, Id):
        auth = BearerAuth().getToken(Id)
        url = (
            getValueFromPropertiesFile("API", "shoppingAppUrl") + self.endPointResource
        )
        urlId = "{0}{1}".format(url, Id)
        content = requests.get(urlId, headers=auth, verify=True)
        return content


var = GetShoppingData().getAllFromShoppingCart(875)
