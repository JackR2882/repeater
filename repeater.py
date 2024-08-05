# CHECK BENCHMARK.TXT, PROCESSES DONT SEEM TO AFFECT EXECUTION TIME, POSSIBLY DUE TO LOCK ON NETWORK INTERFACE (NO CONCURRENT REQUESTS)
# MIGHT AS WELL USE A SIMPLE LOOP



import requests
import  multiprocessing as mp
import request_parser
import re
import json

import csv
from time import perf_counter

file_path = 'results.csv'


# Clear CSV file of any exisiting data
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([])


def replace(text, replacements):    
    
    #replacements = 
    #replacements = ['admin@juice-sh.op', 'admin123']  

    regex = re.compile('(§).*?(§)')
    #print(regex)
    
    for replacement in replacements:
        text = regex.sub(replacement, text, 1)

    #print(text)

    return(text)


def run(request_in):

    #print(request_in)

    burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(request_in.splitlines())

    def request(payloads):
        #print('sending html request ... ... ...')
        session = requests.session()

        #print(type(request))
        #print(request)

        #replace(request_in)

        burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(replace(request_in, payloads).splitlines())
        
        # load payload as json
        burp_json = json.loads(burp_json)

        t1 = perf_counter()

        res = session.post(burp_url, headers=burp_headers, cookies=burp_cookies, json=burp_json)

        ex_time = perf_counter() - t1
        
        # Append data to CSV file
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[payloads, res, ex_time, res.headers['Content-Length']]])

        print(res)


    with open("payload.txt", "r") as file_in:
        payloads = file_in.read().splitlines()

    with open("payload1.txt", "r") as file_in:
        payloads1 = file_in.read().splitlines()


    for payload, payload1 in zip(payloads, payloads1):
        print("Sending: " + payload +  ", " + payload1 + " as payload(s).")

        #parsed = request_parser.parse(request)
        request([payload, payload1])
