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


def run(request, payload_location):

    burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(request.splitlines())

    def request(payload):
        #print('sending html request ... ... ...')
        session = requests.session()

        replaced_json = re.sub(r''+str(payload_location), payload, str(burp_json))

        #print('------------------')
        #print(burp_url)
        #print('------------------')
        #print(burp_headers)
        #print('------------------')
        #print(burp_cookies)
        #print('------------------')
        #print(replaced_json)
        #print('------------------')

        # load payload as json
        replaced_json = json.loads(replaced_json)

        t1 = perf_counter()

        res = session.post(burp_url, headers=burp_headers, cookies=burp_cookies, json=replaced_json)

        ex_time = perf_counter() - t1
        
        # Append data to CSV file
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[payload, res, ex_time, res.headers['Content-Length']]])

        #print(res)
        #print(res.headers)


    with open("payload.txt", "r") as file_in:
        payloads = file_in.read().splitlines()


    for payload in payloads:
        print("Sending " + payload + " as payload.")
        #parsed = request_parser.parse(request)
        request(payload)
