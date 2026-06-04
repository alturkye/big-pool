import zmq

from forex_python.converter import *

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5553")

while True:
    message=socket.recv_json()

    c=CurrencyRates()
    converted=c.convert("USD", message["currency"], message["dollars"])
    socket.send_json({"Converted": converted})