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

    cookies = payloads[16].split(';')
    for cookie in cookies:
        if ": " in cookie:
            cookie = cookie.split()[1]
        split = cookie.split("=")
        cookie_dict[split[0]] = split[1]



    header_dict = {}

    header1 = payloads[3].split(': ')
    header_dict[header1[0]] = header1[1]
    header2 = payloads[4].split(': ')
    header_dict[header2[0]] = header2[1]
    header3 = payloads[5].split(': ')
    header_dict[header3[0]] = header3[1]
    header4 = payloads[6].split(': ')
    header_dict[header4[0]] = header4[1]
    header5 = payloads[7].split(': ')
    header_dict[header5[0]] = header5[1]
    header6 = payloads[8].split(': ')
    header_dict[header6[0]] = header6[1]
    header7 = payloads[9].split(': ')
    header_dict[header7[0]] = header7[1]
    header8 = payloads[10].split(': ')
    header_dict[header8[0]] = header8[1]
    header9 = payloads[11].split(': ')
    header_dict[header9[0]] = header9[1]
    header10 = payloads[12].split(': ')
    header_dict[header10[0]] = header10[1]
    header11 = payloads[13].split(': ')
    header_dict[header11[0]] = header11[1]
    header12 = payloads[14].split(': ')
    header_dict[header12[0]] = header12[1]
    header13 = payloads[15].split(': ')
    header_dict[header13[0]] = header13[1]
    header14 = payloads[17].split(': ')
    header_dict[header14[0]] = header14[1]



    data_dict = {}

    datas = re.sub('\{|\}|\"', '', payloads[19]).split(',')
    for data in datas:
        data = data.split(':')
        data_dict[data[0]] = data[1]

    return(url, cookie_dict, header_dict, data_dict)