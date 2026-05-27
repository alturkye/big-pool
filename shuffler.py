import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Shuffler Microservice running on port 5555...")

while True:
    request = socket.recv_json()

    if request.get("action") == "shuffle":
        # Get the deck from the request, shuffle it, and send it back
        deck = request.get("deck", [])
        random.shuffle(deck)
        socket.send_json({"status": "success", "shuffled_deck": deck})
    else:
        socket.send_json({"status": "error", "message": "Unknown action"})