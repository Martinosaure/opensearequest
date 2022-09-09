from datetime import datetime
import requests
import json
import os
import time

#Defining the range for the amount of token 

for i in range(0,10000):
        start = 1+i
        url = f"https://api.opensea.io/api/v1/asset/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/{start}/" #URL, change Contract address to desired
        headers = {
        "Accept": "application/json",
        "X-API-KEY": "" #API Key from OpenSea
        }
        r = requests.get(url, headers=headers,)
        data = r.json() #Storing JSON Response 
        final = data['supports_wyvern'] #This is the key that interest us
        id = data['name'] #Name and ID of the NFT , in this case , Doodle #XXXX

        msgsales = (str(final)) 
        msgsecond = (str(id))
        sellable = 'True' 
        if msgsales != sellable:
            print(msgsecond + " Has been reported on OpenSea") #If reported, print 
        else:
            print("Nothing.. Still digging") #If not reported, dig
