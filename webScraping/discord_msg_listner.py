# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:45:21 2022

@author: rajen
"""

import json
import threading
import time
import websocket

def send_json_request(ws, request):
    ws.send(json.dumps(request))
    
def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)
    
def heartbeat(interval, ws):
    print('Heartbeat begin')
    
    while True:
        time.sleep(interval)
        heartbeatJSON = {
              "op":1,
              "d":"null"
              }
        send_json_request(ws, heartbeatJSON)
        print("Heartbeat Sent")
        
        
ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
event = receive_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval']/1000
threading._start_new_thread(heartbeat,(heartbeat_interval, ws))

token = 'OTAyNDcxMzE2NDM3ODcyNjYw.GGrPmA.aLIA0D9Ja91kL40YL1UymACfXQjmxj3GMpfClA'
payload = {
    
    "op":2,
    "d":{
        "token":token,
        "properties":{
            "$os":"windows",
            "$browser":"chrome",
            "$device":"pc"
            }
        }
    
    
    }
send_json_request(ws,payload)

while True:
    event = receive_json_response(ws)
    
    try:
        print(f"{event['d']['author']['username']}: {event['d']['content']}")
        op_code = event('op')
        if op_code == 11:
            print('heartbeat received')
            
    except:
        pass
        
    