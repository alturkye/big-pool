import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5553")

fileDir="./files"
os.makedirs(fileDir,exist_ok=True)
#receive binary data while the other end is sending
while True:
    request = socket.recv_multipart()
    fileName=request[0]
    chunk=request[1]
    fileName=fileName.decode("utf-8")
    chunk=chunk.decode("utf-8")
    filePath=os.path.join(fileDir,fileName)

    if chunk==b"":
        socket.send_string("File Received, Complete")
        continue
    with open(filePath, "ab") as f:
        f.write(chunk)
    socket.send_string("Receiving")