import zmq
import hashlib

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5553")

print("Hasher Microservice running on port 5553...")

while True:
    request = socket.recv_json()

    if request.get("action") == "hash":
        password = request.get("password", "")

        # Create a secure SHA-256 hash of the password
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()

        socket.send_json({"status": "success", "hash": hashed_pw})
    else:
        socket.send_json({"status": "error", "message": "Unknown action"})