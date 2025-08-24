# This Python file uses the following encoding: utf-8
import time
import requests
import json

url0 = "https://uiapi2.saapa.ir/api/ebills/GetBills?_timeStamp={}".format(round(time.time() * 1000))
url1 = "https://uiapi2.saapa.ir/api/ebills/GetPowerBillData"
url2 = "https://uiapi2.saapa.ir/api/ebills/PlannedBlackoutsReport"

# Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IntcIlVzZXJJcFwiOm51bGwsXCJVc2VySWRcIjozODcyNzczLFwiU2Vzc2lvbktleVwiOm51bGx9IiwiZXhwIjoxNzcwNzA1MjkxLCJpYXQiOjE3NTQ4MDc2OTEsIm5iZiI6MTc1NDgwNzY5MX0.Y44yzlx-fZa8_lISnSiB_Kg78oyGL8ZZE4fkWt-NCr4
# Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IntcIlVzZXJJcFwiOm51bGwsXCJVc2VySWRcIjozODcyNzczLFwiU2Vzc2lvbktleVwiOm51bGx9IiwiZXhwIjoxNzcwNDQxMzAxLCJpYXQiOjE3NTQ1NDM3MDEsIm5iZiI6MTc1NDU0MzcwMX0.BeAoCG2z8fS6YDyrTwZolRuGKLlZUAL6_WKHBrase7w
head = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IntcIlVzZXJJcFwiOm51bGwsXCJVc2VySWRcIjozODcyNzczLFwiU2Vzc2lvbktleVwiOm51bGx9IiwiZXhwIjoxNzcwNzA1MjkxLCJpYXQiOjE3NTQ4MDc2OTEsIm5iZiI6MTc1NDgwNzY5MX0.Y44yzlx-fZa8_lISnSiB_Kg78oyGL8ZZE4fkWt-NCr4",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
"Accept" : "application/json, text/plain, */*"}

data = {"bill_identifier":"1344616505224"}
data1 = {"bill_id":"1344616505224","from_date":"1404/04/22","to_date":"1404/04/27"}

response1 = requests.get(url0,  headers=head)                             
# print(response1.text)                            

response1 = requests.post(url1, data=json.dumps(data))
# print(response1.json())

response = requests.post(url2, headers=head, data=json.dumps(data1))
t = response.json()

for i in t.get("data"):
    print(i["outage_date"])
    print(i["outage_time"])
    print(i["outage_stop_time"])
    print(i["outage_address"])
