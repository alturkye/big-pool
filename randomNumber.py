import zmq
import json
import random

# set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP) # rep = reply, the listener
socket.bind("tcp://*:5558")

print("Random number generator service is running on port 5558...")

while True:
    message = socket.recv_json()
    # gets the min a nd max range from the message
    min = message['min']
    max = message['max']
    num_int = 0
    # checks if the ranges are valid integers
    if not isinstance(min, int) or not isinstance(max, int):
        socket.send_json({"status": False, "message": "Either the range values are not ints or they were not included"})
    else:
        num_int = random.randint(min, max)
        socket.send_json({"status": True, "number": num_int})

    
