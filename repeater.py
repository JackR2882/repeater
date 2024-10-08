# BROKEN WITH TWO PAYLOAD LOCATIONS, WHEN PAIRED = TRUE (NO STATUS CODE "200" IN RESPONSE)



import requests
import  multiprocessing as mp
import request_parser
import re
import json

import csv
from time import perf_counter
import time
import random

from tkinter import messagebox


file_path = 'results.csv'


## Clear CSV file of any exisiting data
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([])



def payload_recursion(depth, payload_dict, temp_list, request_class):
    if depth ==	len(payload_dict): # reached max depth
        for item in payload_dict[depth]:
            final_list = temp_list.copy()
            final_list.append(item)
            print('sending: ' + str(final_list) + ' as payload(s)')
            request_class.request(final_list)
    else: # recurse
        for item in payload_dict[depth]:
            list = temp_list.copy()
            list.append(item)
            payload_recursion(depth+1, payload_dict, list, request_class)



def replace(text, replacements):  

    regex = re.compile('(§).*?(§)')
    
    for replacement in replacements:
        text = regex.sub(replacement, text, 1)

    return(text)

class Request():


    def __init__(self, request_in, delay):
         self.request_in = request_in
         self.delay = delay

         self.file_path = 'results.csv'


    def request(self, payloads):

        if self.delay[0] != 0:
            # delay requried
            if self.delay[1]:
                # randomize bit set
                time.sleep((random.randint(0, int(self.delay[0]*2)))/1000)
            else:
                # randomize bit not set
                time.sleep((random.randint(0, int(self.delay[0])))/1000)


        session = requests.session()

        burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(replace(self.request_in, payloads).splitlines())
        
        # load payload as json
        burp_json = json.loads(burp_json)

        t1 = perf_counter()

        res = session.post(burp_url, headers=burp_headers, cookies=burp_cookies, json=burp_json)

        ex_time = perf_counter() - t1
        
        # Append data to CSV file
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[payloads, res, ex_time, res.headers['Content-Length']]])

        print(res)




def run(request_in, paired, delay):

    request_class = Request(request_in, delay)

    payload_count = int(request_in.count('§')/2)
    
    if payload_count < 1: # handle no payload location
         messagebox.showerror('Program Error', 'Error: no payload location selected!')
         return

    print(payload_count)

    payload_dict = {}


    for i in range(0, payload_count):
        try:
            with open("payload" + str(i+1) + ".txt", "r") as file_in:
                payload_dict[i+1] = file_in.read().splitlines()
                print("read: payload" + str(i+1) + ".txt")
        except:
            messagebox.showerror('Program Error', 'Error: please create payload' + str(i+1) + '.txt')
            return

    
    if paired:
	
        for i in range(0, len(payload_dict[1])):
            payload_arr = []
            try:
                for key in payload_dict:
                    payload_arr.append(payload_dict[key][i])
            except:
                # length mismatch
                print('ERROR length mismatch')
                break
            print('sending: ' + str(payload_arr) + ' as payload(s)')
            request_class.request(payload_arr)

    else:
    
        payload_recursion(1, payload_dict, [], request_class)
