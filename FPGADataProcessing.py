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
    def
