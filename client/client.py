import sys
import requests
import webbrowser
import random

def encrypt(decoy_site, real_url):                ##implement encryption for refracted request
    return padded



url = sys.argv[1]                                   ## add bound checks

with open("decoylist.txt", 'r') as file:              ##Choose a random decoysite
    lines = file.read().splitlines()
    decoy = random.choice(lines)

padded_url = encrypt(decoy, url)                    ##make the HTTPS request

try:                                                ##actually send HTTPS request
    response = requests.get(padded_url)
    if response.status_code == 200:
        print("HTTPS GET request successful.")
        webbrowser.open(response)                   ##opens it in a browser
    else:
        print(f"Failed: {response.status_code}")
except Exception as e:
    print(f"error")

##Need to add the part with invalid HTTPS request to decoysite to cancel, how to make invalid request?