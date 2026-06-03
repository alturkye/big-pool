import zmq

# Connect to the music service
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

print("Sending play command...")

socket.send_json({"command": "play"})

response = socket.recv_json()

print("Response:")
print(response)

socket.close()
context.term()