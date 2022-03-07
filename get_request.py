#!/usr/bin/python
import json
import threading
import requests

# Define a function for the thread
def do_curl(id: str):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer <token>'
        }
    res = requests.get('http://localhost:5000/sites', headers=headers)
    print(res)


# Create five threads as follows
if __name__ == '__main__':
    try:
        _1 = threading.Thread(target=do_curl)
        _2 = threading.Thread(target=do_curl)
        _3 = threading.Thread(target=do_curl)
        _4 = threading.Thread(target=do_curl)
        _5 = threading.Thread(target=do_curl)
        _1.start()
        _2.start()
        _3.start()
        _4.start()
        _5.start()

    except:
        print("Error: unable to start thread")

    while 1:
        pass
