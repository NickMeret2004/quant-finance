import numpy as np
import multiprocessing as mp
import time

# Simulating incoming tick data
def generate_ticks(num_ticks=1000):
    prices = np.random.uniform(99, 101, num_ticks)      #Simulated price range
    volumes = np.random.randint(10, 500, num_ticks)     #Simulated volume
    sides = np.random.choice(['bid', 'ask'], num_ticks)   #Random buy/sell
    return list (zip(sides, prices, volumes))           

# Order book processor
class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def update(self, tick):
        #updates the order book with incoming tick data
        side, price, volume = tick
        if side =='bid':
            self.bids.append((price, volume))
            self.bids.sort(reverse=True, key=lambda x: x[0])    #Sort bids descending
        else:
            self.aks.append((price, volume))
            self.asks.sort(reverse=True, key=lambda x: x[0])    #Sorts asks descending

    def best_bid_ask(self):
        #Returns the top bid and ask prices
        best_bid = self.bids[0] if self.bids else None  #Checks if there are any bids
        best_ask = self.asks[0] if self.asks else None  #Checks if there are any asks
        return best_bid, best_ask

#Function to process ticks
def process_ticks(order_book, tick_queue):
    while not tick_queue.empty():
        tick = tick_queue.get()
        order_book.update(tick)

# Simulate FPGA parallel processing using multiprocessing
def run_simulation():
    tick_data = generate_ticks(1000)
    order_book = OrderBook()

    tick_queue = mp.Queue()
    for tick in tick_data:
        tick_queue.put(tick)
