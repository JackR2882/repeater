# NEEDS CLEANING UP, BUT GOOD START TO PARSING REQUESTS
# SHOULD TEST WITH DIFFERENT REQUESTS TO MAKE SURE THEY'RE UNIFORM IN STRUCTURE



import re

# take raw burp request as input, and process it into variables
# variables are:
#   url
#   cookie_dict
#   header_dict
#   data_dict

#def parse(file_in):
#    print(file_in)

#with open("full_request.txt", "r") as file_in:
#    payloads = file_in.read().splitlines()

#print(payloads)



def parse(payloads):

    url = "http://" + payloads[1].split()[1] + payloads[0].split()[1]



    cookie_dict = {}
    header_dict = {}
    data_dict = {}

    for payload in payloads:
        # iterate through all lines in the payload category
        if 'Cookie:' in payload or 'cookie:' in payload:
            cookies = payload.split(';')
            for cookie in cookies:
                if ": " in cookie:
                    cookie = cookie.split()[1]
                split = cookie.split("=")
                cookie_dict[split[0]] = split[1]
        elif '{' in payload and '}' in payload:
            data_dict = payloads[19]
        elif 'POST' in payload or 'GET' in payload: # need to add all other request types
            print('Contains url!')
            # more complicated because it spans two lines which need to be combined
        elif payload != '':
            header = payload.split(': ')
            header_dict[header[0]] = header[1]


    return(url, cookie_dict, header_dict, data_dict)
