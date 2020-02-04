from typing import *

x: int = 10

def f0(x, y):
    return x + y

f0(1, 2)
f0('hello', 'world')
f0('hello', 1)


def f1(x: int, y: int) -> int:
    return x + y

f1(1, 2)
f1('hello', 'world')
f1('hello', 1)

x = {}

def g(x: Sequence[int]) -> None:
    print(len(x))
    for i in x:
        print(type(i))
    
g([1,2,3])
g('abcde')
g(['1', 1, '2'])

def g1(x: List[int]) -> None:
    print(len(x))
    for i in x:
        print(type(i))

g1([1,2,3])
g1((1,2,3))

def g2(x: Tuple[int, int, int]) -> None:
    print(len(x))
    for i in x:
        print(type(i))

g2((1,2,3))
g2((1,'2',3))

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

Point0 = NamedTuple('Point', [('x', int), ('y', str)])


# Grouping with Default Dict
from collections import defaultdict

d = defaultdict(set)
d['t'].add('tom')
d['t'].add('ted')
d['t'].add('ted')
d['m'].add('mary')
d['m'].add('martha')

from pprint import pprint
pprint(d, width=40)

names = '''betty beatrice bob bart daviv martha mary mars tim tom ted wallace'''.split()


d = defaultdict(list)

for name in names:
    feature = name[0]
    d[feature].append(name)

pprint(d)

d = defaultdict(list)
for name in names:
    feature = name[-1]
    d[feature].append(name)

pprint(d)

d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)

pprint(d)

e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre', 'gratis']
}

s2e = defaultdict(list)

for eng, spanish_words in e2s.items():
    for spanish_word in spanish_words:
        s2e[spanish_word].append(eng)

e2s = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}

s2e = {span: eng for eng, span in e2s.items()}
s2e

pprint(sorted(names, key=len))

list(zip('abcde','fghijk'))

from itertools import zip_longest

list(zip_longest('abcde','fghijk'))
list(zip_longest('abcde','fghijk', fillvalue='x'))

# Transpose Matrix
m = [
    [10, 20],
    [30, 40],
    [50, 60]
]

list(zip([10, 20], [30, 40], [50, 60]))

list(zip(*m))

# Flattern a list
[x for row in m for x in row]