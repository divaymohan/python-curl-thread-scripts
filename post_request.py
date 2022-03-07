#!/usr/bin/python
import json
import threading
import requests

# Define a function for the thread
def do_curl(id: str):
    #Header
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer <token>',  
        'Content-Type': 'application/json'
        }
    # Modify data according to need
    data = {
        "site_id": id,
        "site_details": {
            "customer_id": "123",
            "region": "abc",
            "platform_account_id": "string",
            "platform_type": "aws"
        }
    }
    res = requests.post('http://localhost:5000/sites', headers=headers, data= json.dumps(data))
    print(res)


# Create five threads as follows
if __name__ == '__main__':
    try:
        _1 = threading.Thread(target=do_curl, args=("123483",))
        _2 = threading.Thread(target=do_curl,args=('12346',))
        _3 = threading.Thread(target=do_curl,args=('12347',))
        _4 = threading.Thread(target=do_curl,args=('12348',))
        _5 = threading.Thread(target=do_curl,args=('123459',))
        _1.start()
        _2.start()
        _3.start()
        _4.start()
        _5.start()

    except:
        print("Error: unable to start thread")

    while 1:
        pass
