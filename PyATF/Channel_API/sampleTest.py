import requests
import json


BASE_URL = "http://reqres.in/"
PARAM = "page=2"

# GET Method

respo = requests.get(BASE_URL+"api/users?",params=PARAM)
print(respo)        #Used to print only status
#print(resp.json()) #Used to print
print(json.dumps(respo.json(),indent=4))   #Used to print json response in proper formate


resp = respo.json()
#import ipdb; ipdb.set_trace()

#print(len(resp["total"]))

for i in resp["data"]:
    list = (i["first_name"])
    print(i["first_name"])

