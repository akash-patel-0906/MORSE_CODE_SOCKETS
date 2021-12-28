import socket
import time
from typing import final

HOST = '10.0.0.78' 
PORT = 4445      


communication_array=[]


MORSE_CODE_DICT={
    'A' : [50, 100],
    'B' : [100, 50, 50, 50],
    'C' : [100,50, 100, 50],
    'D' : [100, 50, 50],
    'E' : [50],
    'F' : [50, 50, 100, 50],
    'G' : [100, 100, 50],
    'H' : [50, 50, 50, 50],
    'I' : [50, 50],
    'J' : [50, 100, 100, 100],
    'K' : [100, 50, 100],
    'L' : [50, 100, 50, 50],
    'M' : [100, 100],
    'N' : [100, 50],
    'O' : [100, 100, 100],
    'P' : [50, 100, 100, 50],
    'Q' : [100, 100, 50, 100],
    'R' : [50, 100, 50],
    'S' : [50, 50, 50],
    'T' : [100],
    'U' : [50, 50, 100],
    'V' : [50, 50, 50, 100],
    'W' : [50, 100, 100],
    'X' : [100, 50, 50, 100],
    'Y' : [100, 50, 100, 100],
    'X' : [100, 100, 50, 50],
    ' ' : [500]
}

def decode_array():
    working_arr=[] # holds current letter
    final_message=''  #final message
    for value in communication_array:
        if(value!=250):
            working_arr.append(value)
        else:
            for key in MORSE_CODE_DICT:
                if MORSE_CODE_DICT[key] == working_arr:
                    final_message = final_message+key
            working_arr.clear()

    print(final_message) # print final message


def listner():
    previous_time=0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen() # enables server to accept connections
            current_time = round(time.time() * 1000) # get current time
            conn, addr = s.accept() # waits for connection (blocks/hangs)
            current_time = round(time.time() * 1000)
        
            with conn:
                print('Connected by', addr)
                print('time', current_time)
                difference = current_time-previous_time
                print('Distance between times', difference)
                if(difference >= 5000 and previous_time!=0):
                    break
                communication_array.append(int((difference/10)*10 - difference%10))
                previous_time=current_time

    communication_array.pop(0)

    decode_array()

def main():

    listner()

main()
