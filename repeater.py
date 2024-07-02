# CHECK BENCHMARK.TXT, PROCESSES DONT SEEM TO AFFECT EXECUTION TIME, POSSIBLY DUE TO LOCK ON NETWORK INTERFACE (NO CONCURRENT REQUESTS)
# MIGHT AS WELL USE A SIMPLE LOOP



import requests
import  multiprocessing as mp
import request_parser

import time
import os



#def split():
#    # splits the payload into chunks for processes to work on
#    print("...")


with open("full_request.txt", "r") as req:
    payloads = req.read().splitlines()
    burp_url, burp_cookies, burp_headers, burp_json = request_parser.parse(payloads)


def request(payload):
    print('sending html request ... ... ...')
    session = requests.session()

    res = session.post(burp_url, headers=burp_headers, cookies=burp_cookies, json=burp_json)

    #print(res)


with open("payload.txt", "r") as file_in:
    payloads = file_in.read().splitlines()
print(payloads)


for payload in payloads:
    print("Sending " + payload + " as payload.")
    #parsed = request_parser.parse(request)
    request(payload)



#if __name__ == '__main__':
#    mp.freeze_support()

#    core_count = mp.cpu_count()
    #print(core_count)

#    t1 = time.time()

#    request(1)

    #p1 = mp.Process(target=request, args=(1,))
    #p2 = mp.Process(target=request, args=(2,))
    #p3 = mp.Process(target=request, args=(3,))
    #p4 = mp.Process(target=request, args=(4,))

    #p1.start()
    #p2.start()
    #p3.start()
    #p4.start()

    #p1.join()
    #p2.join()
    #p3.join()
    #p4.join()

#    t2 = time.time()

#    print('time elapsed: ' + str(t2-t1))

    #f = open("payload.txt", "r")
    #print(f.read())
    #print((f.read()[1]))