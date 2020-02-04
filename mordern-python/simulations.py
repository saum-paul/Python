from random import *
from statistics import *
from collections import *

# Create a ROullette table of 18 red, 18 black and 2 green slots

population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2

choice(population)
[choice(population) for i in range(6)]

choices(population, k=6)

choices(['red', 'black', 'green'], [18, 18, 2], k=6)

deck = Counter(tens=16, lows=36)

deck = list(deck.elements())

deal = sample(deck, 52)
remainder = deal[20:]
Counter(remainder)

# simulate 7 spins of a biased coin
pop = ['heads', 'tails']
cumwt = [0.6, 1.0]

choices(pop, cum_weights=cumwt, k=7)
choices(['heads', 'tails'], cum_weights=[0.6, 1.0], k=7)

choices(['heads', 'tails'], cum_weights=[0.6, 1.0], k=7).count('heads')

choices(['heads', 'tails'], cum_weights=[0.6, 1.0], k=7).count('heads') > 5

trial = lambda: choices(['heads', 'tails'], cum_weights=[0.6, 1.0], k=7).count('heads') > 5

trial()

n = 1000

sum(trial() for i in range(n))

from math import factorial as fact

fact(3)
fact(4)


def comb(n, r):
    return fact(n) // (fact(r) * fact(n-r))

comb(10, 4 )

sample(range(10000), 5)

median(sample(range(10000), 5))

n = 10000

n//4 <= median(sample(range(n), 5)) < 3 * n // 4

trial = lambda: n//4 <= median(sample(range(n), 5)) < 3 * n // 4

trial()

sum(trial() for i in range(n))/ n

timings = [7.18, 8.59, 9.07, 12.24, 8.68, 7.39, 6.98, 7.31, 7.61, 10.02, 8.16]

mean(timings)
stdev(timings)

def bootstrap(data):
    return choices(data, k=len(data))

bootstrap(timings)

mean(bootstrap(timings))

means = sorted(mean(bootstrap(timings)) for i in range(n))

means[:20]

means[-20:]

means[500]

means[-500]

# Simulate Service wait time

from statistics import mean, stdev
from random import expovariate, gauss

avg_arrival_time = 5.6
avg_service_time = 4.8
stdev_service_time = 0.5

num_waitiing = 0
arrivals = []
starts = []
arrival = service_end = 0.0

for i in range(20000):
    if arrival <= service_end:
        num_waitiing += 1
        arrival += expovariate(1.0/ avg_arrival_time)
        arrivals.append(arrival)
        
    else:
        num_waitiing -= 1
        service_start = service_end if num_waitiing else arrival
        service_time = gauss(avg_service_time, stdev_service_time)
        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for arrival, start in zip(arrivals, starts)]
print(f'Mean wait {mean(waits): .1f}, Std. Dev wait {stdev(waits): .2f}')


