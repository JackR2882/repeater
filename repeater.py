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

    return(text)


def run(request_in, payload_count):

    #print(request_in)

    #burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(request_in.splitlines())

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


    #with open("payload.txt", "r") as file_in:
    #    payloads = file_in.read().splitlines()

    #with open("payload1.txt", "r") as file_in:
    #    payloads1 = file_in.read().splitlines()


    # Can assume 1 payload by default
    with open("payload1.txt", "r") as file_in:
        payloads1 = file_in.read().splitlines()
    
    
    if payload_count == 2:
        with open("payload2.txt", "r") as file_in:
            payloads2 = file_in.read().splitlines()
    elif payload_count == 3:
        with open("payload2.txt", "r") as file_in:
            payloads2 = file_in.read().splitlines()
        with open("payload3.txt", "r") as file_in:
            payloads3 = file_in.read().splitlines()


    # two modes, payload 'pairs' (n), or repeated payloads (n^3)

    paired = True # defines if the payloads are in pairs or not

    if paired:
        
        if payload_count == 1:
            for payload1 in payloads1:
                print("Sending: " + payload1 + " as payload(s).")
                request([payload1])
        elif payload_count == 2:
            for payload1, payload2 in zip(payloads1, payloads2):
                print("Sending: " + payload1 +  ", " + payload2 + " as payload(s).")
                request([payload1, payload2])
        elif payload_count == 3:
            for payload1, payload2, payload3 in zip(payloads1, payloads2, payloads3):
                print("Sending: " + payload1 +  ", " + payload2 + ", " + payload3 + " as payload(s).")
                request([payload1, payload2, payload3])

        #for payload1, payload2, payload3 in zip(payloads1, payloads2, payloads3):
        #    print("Sending: " + payload1 +  ", " + payload2 + ", " + payload3 + " as payload(s).")

            #parsed = request_parser.parse(request)
        #    request([payload1, payload2, payload3])

    else:

        if payload_count == 1:
            for payload1 in payloads1:
                print("Sending: " + payload1 + " as payload(s).")
                request([payload1])

        if payload_count == 2:
            for payload1 in payloads1:
                for payload2 in payloads2:
                    print("Sending: " + payload1 +  ", " + payload2 + " as payload(s).")
                    request([payload1, payload2])

        if payload_count == 3:
            for payload1 in payloads1:
                for payload2 in payloads2:
                    for payload3 in payloads3:
                        print("Sending: " + payload1 +  ", " + payload2 + ", " + payload3 + " as payload(s).")
                        request([payload1, payload2, payload3])
