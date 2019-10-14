#!/usr/bin/python3
import requests
"""
POST - Vote 1024 times in my
"""
url = 'http://158.69.76.135/level0.php'
my_voted = {'id': 885, 'holdthedoor': 'submit'}
print("--- Init program ---")
print("...")
for i in range(1, 1023):
    requests.post(url, my_voted)
print("--- Comlete ---")
