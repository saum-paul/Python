from collections import Counter

colors = 'red red red green green blue'.split()

# Counter
c = Counter(colors)
c.elements()
c.values()
c.most_common(2)
c.keys()

# Statistics
from statistics import mean, median, mode, stdev, pstdev

data = [10, 25, 30, 35, 40, 50]
mean(data)
median(data)
mode(colors)
stdev(data)
pstdev(data)

# Distributions
from random import random, seed, uniform, triangular, gauss, expovariate

random()
seed(12345)
random()
uniform(1000, 2000)
triangular(1000, 2000)
gauss(100, 15)
expovariate(.5)

data = [triangular(1000, 1100) for i in range(1000)]
mean(data)
stdev(data)
data = [uniform(1000, 1100) for i in range(1000)]
mean(data)
stdev(data)

from random import choice, choices, sample, shuffle
data = ['win', 'lose', 'draw', 'play again', 'double win']

choice(data)
choices(data, k=3)
choices(data, k=6)
sample(data, k=3) # No repeat

Counter(choices(data, k=10))

choices(data, [5,4,3,2,1], k=20)
Counter(choices(data, [5,4,3,2,1], k=30))

shuffle(data)
data

sorted(sample(range(1,70), k=5))

import glob
glob.glob('congress_data\*')

import csv

with open('congress_data\\congress_votes_114-2016_s116.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)


names = 'racheal mathew raymond'.split()
colors = 'blue red yellow green'.split()
cities = 'austin dallas houston boston liverpool houston dallas'.split()

# Indexing is slow
for i in range(len(names)):
    print(names[i].upper())

for name in names:
    print(name.upper())


for i in range(len(names)):
    print(i+1, names[i].upper())

for i, name in enumerate(names, start=1):
    print(i, name)

# Reverse print
for i in range(len(colors) -1, -1, -1):
    print(colors[i])

for color in reversed(colors):
    print(color)

for name, color in zip(names, colors):
    print(name, color)

for color in sorted(colors):
    print(color)

for color in sorted(colors, key=len):
    print(color)

for city in cities:
    print(city)

for city in set(cities):
    print(city)

for city in sorted(set(cities)):
    print(city)

for i, city in enumerate(sorted(set(cities)), start=1):
    print(i, city)

for i, city in enumerate(map(str.upper, sorted(set(cities))), start=1):
    print(i, city)


from collections import Counter
c = Counter()
c['red'] += 1
c['red'] += 1
c['blue'] += 1
c.most_common(1)
c.most_common(2)
list(c.elements())

