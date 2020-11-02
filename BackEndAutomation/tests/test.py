from BackEndAutomation.requests.getRequests import GetShoppingData
import unittest


class GetRequestTests(unittest.TestCase):

    getShoppingData = GetShoppingData()

    def test_for_200_status_code(self):
        results = self.getShoppingData.getAllFromShoppingCart().status_code
        self.assertEquals(results, 200)

    def test_for_object_count(self):
        results = self.getShoppingData.getAllFromShoppingCart().headers["Content-Type"]
        self.assertEquals(results, "application/json; charset=utf-8")


if __name__ == "__main__":
    unittest.main()
