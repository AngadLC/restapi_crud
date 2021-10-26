import requests
import json
url = 'http://127.0.0.1:8000/classbasedapi/'

# get request
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url, data=json_data)
        
    response = r.json()
    print(response)
#for to read the data
# get_data()

# for to write the data
def post_data():
    data = {
        'name':'biplop',
        'roll':23,
        'city':'pokhara'
        }
    # print(data)
    # parse x:
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.post(url,data=json_data)
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
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.put(url,data=json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {
        'id':3,
        }
    # print(data)
    # parse x:
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.delete(url,data=json_data)
    data = r.json()
    print(data)

# delete_data()
