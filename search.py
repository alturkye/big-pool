import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")

print("Search Microservice running on port 5554...")

while True:
    request = socket.recv_json()

    if request.get("action") == "search":
        keyword = request.get("keyword", "").lower()
        deck = request.get("deck", [])

        # Filter the deck for the keyword in either the term or definition
        results = []
        for card in deck:
            if keyword in card.get("term", "").lower() or keyword in card.get("definition", "").lower():
                results.append(card)

        socket.send_json({"status": "success", "results": results})
    else:
        socket.send_json({"status": "error", "message": "Unknown action"})