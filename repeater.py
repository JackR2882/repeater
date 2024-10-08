import requests
import request_parser
import re
import json

import csv
from time import perf_counter
import time
import random

from tkinter import messagebox


# output file for results
file_path = 'results.csv'

# clear results file of any existing data
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([])


# recursive function to every element of file1 with every element of file2 through fileN
# at maximum depth calls the request function with this list
def payload_recursion(depth, payload_dict, temp_list, request_class):
    
    if depth ==	len(payload_dict): # reached max depth
        for item in payload_dict[depth]:
            final_list = temp_list.copy()
            final_list.append(item)
            #print('sending: ' + str(final_list) + ' as payload(s)')
            request_class.request(final_list)
    else: # recurse
        for item in payload_dict[depth]:
            list = temp_list.copy()
            list.append(item)
            payload_recursion(depth+1, payload_dict, list, request_class)


# replaces everything between '§' symbols with replacement text 
def replace(text, replacements):  

    regex = re.compile('(§).*?(§)')
    
    for replacement in replacements:
        text = regex.sub(replacement, text, 1)

    return(text)


# request class to handle request parsing and execution of requests
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

        # parse request
        burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(replace(self.request_in, payloads).splitlines())
        burp_json = json.loads(burp_json)

        # send request
        t1 = perf_counter()
        res = session.post(burp_url, headers=burp_headers, cookies=burp_cookies, json=burp_json)
        ex_time = perf_counter() - t1
        
        # append results to results file
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[payloads, res, ex_time, res.headers['Content-Length']]])



def run(request_in, paired, delay):

    request_class = Request(request_in, delay)

    payload_count = int(request_in.count('§')/2)
    
    if payload_count < 1: # handle no payload location
         messagebox.showerror('Program Error', 'Error: no payload location selected!')
         return

    payload_dict = {}

    # load contents of payload files to memory
    for i in range(0, payload_count):
        try:
            with open("payload" + str(i+1) + ".txt", "r") as file_in:
                payload_dict[i+1] = file_in.read().splitlines()
        except:
            messagebox.showerror('Program Error', 'Error: please create payload' + str(i+1) + '.txt')
            return

    # combine elelments of payload files and send to request method
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
            #print('sending: ' + str(payload_arr) + ' as payload(s)')
            request_class.request(payload_arr)
    else:    
        payload_recursion(1, payload_dict, [], request_class)
