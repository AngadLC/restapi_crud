import requests
import json
url = 'http://127.0.0.1:8000/api/'

# get request
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url, headers= headers, data=json_data)
    
    response = r.json()
    print(response)
#for to read the data
get_data(1)

# for to write the data
def post_data():
    data = {
        'name':'angad',
        'roll':23,
        'city':'pokhara'
        }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.post(url,data=json_data, headers=headers)
    data = r.json()
    print(data)

# post_data()

# update data
def update_data():
    data = {
        'id':2,
        'name':'Angad',
        'roll':11,
        'city':'Kusham'
        }
    # print(data)
    # parse x:
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.put(url,data=json_data, headers= headers)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id':3,
        }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.delete(url,headers =headers ,data=json_data)
    data = r.json()
    print(data)

# delete_data()
