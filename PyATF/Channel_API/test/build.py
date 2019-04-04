import requests
import json
import unittest
from Channel_API.routing.config import configuration
from Channel_API.routing import operations
from Channel_API.routing.payloads import req1


class makeService(unittest.TestCase):



    def setUp(self):
        print("Set Up Success")

    def tearDown(self):
        print("Tear Down Success")


    def test_getReq(self):
        resp1 = requests.get(configuration.BASE_URL+"api/users?",params=operations.PARAM)
        print(resp1.json())


    def test_postReq(self):
        print("POST**********REQUEST")
        resp2 = requests.post(configuration.BASE_URL+"api/users?",data=req1.postRequest2)
        print(resp2.json())

    def test_putReq(self):
        print("PUT**********REQUEST")
        resp3 = requests.put(configuration.BASE_URL+"api/users?",data=req1.putRequest1)
        print(resp3.json())

    def test_deletReq(self):
        print("DELET**********REQUEST")
        resp4 = requests.delete(configuration.BASE_URL+"api/users?",params=operations.deleteParam)
        print(resp4.json())


if __name__ == '__main__':
    unittest.main