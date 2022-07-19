# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:36:36 2022

@author: rajen
"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os 
from time import sleep, time


  
def api_runner():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {"start": "1", "limit": "15", "convert": "USD"}
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "60e5c0b9-f766-4d82-809a-ed56f637ab00",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    df = pd.json_normalize(data["data"])
    df["timestamp"] = pd.Timestamp.now()

    if not os.path.isfile(r"API.csv"):
        df.to_csv(r"API.csv", header="column_names")
    else:
        df.to_csv(r"API.csv", mode="a", header=False)
        

sleep_min = 2 
for i in range(3):
    api_runner()
    print("API runner completed successfully")
    sleep(sleep_min * 60)
exit()