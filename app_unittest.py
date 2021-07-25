import unittest
from service import make_request


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(make_request("New York").get('message'), "math domain error")
        self.assertEqual(make_request("   ").get('message'), "list index out of range")
        self.assertEqual(str(make_request("Tomsk").get('min_distance')), str(4903.46563))
        self.assertEqual(str(make_request("Kazan").get('min_distance')), str(1025.30594))
        self.assertEqual(make_request("Hanoi").get('message'), "list index out of range")
        self.assertEqual(make_request(123).get('message'), "'int' object has no attribute 'replace'")
        self.assertEqual(make_request([1, 2, 3]).get('message'), "'list' object has no attribute 'replace'")


if __name__ == '__main__':
    unittest.main()
