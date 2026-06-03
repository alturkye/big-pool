import zmq
from playsound import playsound
import threading

# audio path
SONG_PATH = "audio/ikoliks_aj-jazz-elevator-lounge-music-391978.mp3"

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

print("Elevator music service running on port 5557...")

def play_music():
    playsound(SONG_PATH)

while True:
    message = socket.recv_json()

    command = message.get("command")

    if command == "play":

        threading.Thread(target=play_music).start()

        socket.send_json({"status": True,"message": "Music started"})

    else:
        socket.send_json({"status": False,"message": "Unknown command"})