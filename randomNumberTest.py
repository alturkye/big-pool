import zmq
import json

# set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REQ)

# connect to the microservice
socket.connect("tcp://localhost:5556")


# Test 1: Valid range

request = {
    "min": 1,
    "max": 10
}

print("Sending valid request...")
socket.send_json(request)

response = socket.recv_json()
print("Response:", response)


# Test 2: Invalid type

request = {
    "min": "a",
    "max": 10
}

print("\nSending invalid request...")
socket.send_json(request)

response = socket.recv_json()
print("Response:", response)


# Test 3: Another valid range

request = {
    "min": 50,
    "max": 100
}

print("\nSending another valid request...")
socket.send_json(request)

response = socket.recv_json()
print("Response:", response)