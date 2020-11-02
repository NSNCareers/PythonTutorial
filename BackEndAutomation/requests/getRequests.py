import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *


class GetShoppingData:

    endPointResource = ApiEndpoints.ShoppingAppEndPoint3
    endPointResource2 = ApiEndpoints.ShoppingAppEndPointV2

    # https://www.youtube.com/watch?v=06I63_p-2A4
    # https://stackoverflow.com/questions/46520127/vscode-import-error-for-python-module

    def getAllFromShoppingCart(self):
        # getUrl = self.shoppingAppUrl + self.endPoint
        # content = requests.get(getUrl)
        # url = self.shoppingAppUrl + self.ShoppingAppEndPoint
        url = (
            getValueFromPropertiesFile("API", "shoppingAppUrl") + self.endPointResource
        )
        content = requests.get(url)
        return content

    def getShoppingCartWithIdAuthentication(self, Id):
        # getUrl = self.shoppingAppUrl + self.endPoint
        # content = requests.get(getUrl)
        url = (
            getValueFromPropertiesFile("API", "shoppingAppUrl") + self.endPointResource
        )
        urlId = "{0}{1}".format(url, Id)
        content = requests.get(urlId)
        return content

    def getShoppingCartWithId(self, Id):
        # getUrl = self.shoppingAppUrl + self.endPoint
        # content = requests.get(getUrl)
        url = (
            getValueFromPropertiesFile("API", "shoppingAppUrl") + self.endPointResource
        )
        urlId = "{0}{1}".format(url, Id)
        content = requests.get(urlId)
        return content
