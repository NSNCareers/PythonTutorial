import json
import requests
from BackEndAutomation.utilities.endPoints import *
from BackEndAutomation.utilities.configuration import *


@Given(u"I read from a json file")
def steps_impl(context):
    context.endPointResource = ApiEndpoints.ShoppingAppEndPoint3
    context.endPointResource2 = ApiEndpoints.ShoppingAppEndPointV2


@when(u"I configure my request Url")
def step_impl(context):
    context.url = (
        getValueFromPropertiesFile("API", "shoppingAppUrl") + context.endPointResource
    )


@then(u"I send the put request")
def step_impl(context):
    content = requests.get(context.url)
    assert content.status_code == 200
