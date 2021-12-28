#!/usr/bin/env python3

import socket
import time



HOST = '10.0.0.78'  # The server's hostname or IP address
PORT = 4445     # The port used by the server

# dot = 50 ms
# dash = 100ms
# distance between letters = 250 ms
# distance between words = 500 ms


MORSE_CODE_DICT={
    'A' : [50, 100, 250],
    'B' : [100, 50, 50, 50,250],
    'C' : [100,50, 100, 50,250],
    'D' : [100, 50, 50,250],
    'E' : [50,250],
    'F' : [50, 50, 100, 50,250],
    'G' : [100, 100, 50,250],
    'H' : [50, 50, 50, 50,250],
    'I' : [50, 50,250],
    'J' : [50, 100, 100, 100,250],
    'K' : [100, 50, 100,250],
    'L' : [50, 100, 50, 50,250],
    'M' : [100, 100,250],
    'N' : [100, 50,250],
    'O' : [100, 100, 100,250],
    'P' : [50, 100, 100, 50,250],
    'Q' : [100, 100, 50, 100,250],
    'R' : [50, 100, 50,250],
    'S' : [50, 50, 50,250],
    'T' : [100,250],
    'U' : [50, 50, 100,250],
    'V' : [50, 50, 50, 100,250],
    'W' : [50, 100, 100,250],
    'X' : [100, 50, 50, 100,250],
    'Y' : [100, 50, 100, 100,250],
    'X' : [100, 100, 50, 50,250],
    ' ' : [500, 250]
}


text=[] # holds string

# fills text array
def fill_array(string):
    for key in string:
        for value in MORSE_CODE_DICT[key]:
            text.append(value)
    text.append(5000) # marks end of the string
    text.append(0)

def execute():
    for distance in text: #iterate over array
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT)) #connect to server
            print(distance)
        time.sleep(distance/1000) # sleep value of distance

def main():
    user_input = input("What morse message do you want to send? ")
    fill_array(user_input.upper())          
    execute()
main()