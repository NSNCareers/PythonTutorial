import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *


class BearerAuth:

    endPointResource = ApiEndpoints.ShoppingAppEndPointV1
    endPointResource2 = ApiEndpoints.ShoppingAppEndPointV2

    def getToken(self, tokenId):
        # getUrl = self.shoppingAppUrl + self.endPoint
        # content = requests.get(getUrl)
        url = (
            getValueFromPropertiesFile(None, "API", "shoppingAppUrl")
            + self.endPointResource2
        )
        urlId = "{0}{1}".format(url, tokenId)
        token = requests.get(urlId).text
        bearerToken = "Bearer " + token
        headers = {
            "Authorization": bearerToken,
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
        }
        return headers
