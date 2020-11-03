import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *
from BackEndAutomation.requestAuth.authentication import *


class GetCookiesData:

    endPointResource = ApiEndpoints.ShoppingAppEndPointV1
    endPointResource2 = ApiEndpoints.ShoppingAppEndPointV2

    # https://www.youtube.com/watch?v=06I63_p-2A4
    # https://stackoverflow.com/questions/46520127/vscode-import-error-for-python-module

    def getCookies(self):
        session = requests.session()
        cookies = {"visit-days": "February"}
        url = "http://qa.loginapp.nsncareers.com/"
        # Setting request cookies
        # session.get(url, cookies=cookies)
        # content = session.cookies.get_dict()
        content = session.get(url).history
        return content


# var = GetCookiesData().getCookies()
# print(var)
