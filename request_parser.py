# take raw burp request as input, and process it into variables
# variables are:
#   url
#   cookie_dict
#   header_dict
#   data_dict

def parse(payloads):

    cookie_dict = {}
    header_dict = {}
    data_dict = {}

    http_req = ""
    http_host = ""
    
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
            data_dict = payload
        elif 'POST' in payload or 'GET' in payload or 'PATCH' in payload or 'PUT' in payload or 'DELETE' in payload or 'HEAD' in payload: # need to add all other request types
            http_req = payload.split()[1]
        elif 'Host: ' in payload or 'host: ' in payload:
            http_host = payload.split()[1]
        elif payload != '':
            header = payload.split(': ')
            header_dict[header[0]] = header[1]

        url = 'http://' + http_host + http_req


    return(url, cookie_dict, header_dict, data_dict)
