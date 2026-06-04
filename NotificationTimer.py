import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5553")

while True:
    message=socket.recv_json()
    seconds=message['time']
    #wait and then notify
    time.sleep(seconds)
    socket.send("Time Is Up!")
