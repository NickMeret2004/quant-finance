#Knock out option pricing
import numpy as np

S0 = 100                #initial stock price
B = 120                 #barrier level
K = 105                 #strike price
r = 0.2                 #risk free rate
sigma = 0.25            #volatility
T = 1                   #time to maturity (1 year)
n_steps = 252           #number of steps in simulation (trading days per year)
n_simulations = 1000    #number of simulations ran

dt = T / n_steps        #time step size

payoffs = []

for i in range (n_simulations):
    S_t = S0
    barrier_breached = False

    for j in range (n_steps):
        dw = np.random.normal(0, np.sqrt(dt))                   #brownian motion (generates randum num from normal distribution)
        S_t *= np.exp((r-0.5 * sigma ** 2) * dt + sigma * dw)   #stock price update

        #(r-0.5 * sigma **2) * dt is stocks natural growth rate
        #(sigma * dw) represents random fluctations 

        if S_t >= B:
            barrier_breached = True
            break

    if not barrier_breached:
        payoffs.append(max(S_t - K, 0))     #call option payoff


#option price computation
option_price = np.exp(-r * T) * np.mean(payoffs)
print(f"Knock-out option price: {option_price:.4f}")




