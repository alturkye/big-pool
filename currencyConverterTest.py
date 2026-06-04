import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5553")

print("Sending request...")

socket.send_json({
        "currency": "EUR",
        "dollars": 100
})

response = socket.recv_json()
print(response)

socket.send_json({
        "currency": "NZD",
        "dollars": 100
})

response = socket.recv_json()
print(response)