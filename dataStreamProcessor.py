import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    bids = data['bids'][:5]         #Top 5 bid prices
    asks = data['asks'][:5]         #Top 5 ask prices

    print("--- Order Book Snapshot ---")
    print("Bids (Buy Orders):")
    for price, volume in bids:
        print(f"Price: {price}, Volume: {volume}")

    print("Asks (Ask Orders):")
    for price, volume in asks:
        print(f"Price: {price}, Volume: {volume}")

    print("----------------------------\n")

