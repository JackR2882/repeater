
Functions similarly to burp's intruder tool in sniper mode with a single payload location.

To run:
    - Run repeater_main.py
    - Paste full request from burp into 'html request' text box.
    - Identify payload location and copy this into 'payload' text box. (Must be an exact match).
        e.g. For {password:'some_password_here'}, use some_password_here in 'payload' text box.
    - Create file called 'payload.txt' and paste attack wordlist in there, must be in the following format:
        payload 1
        payload 2
        payload 3
        ...
        payload n
    - Press the attack button, results will be published into 'results.csv', fields are as follows:
        payload ! http response ! response time ! response length


TO DO:
    - Implement mutiple payload locations.
    - Implement multiple 