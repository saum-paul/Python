from math import fsum, sqrt
from random import sample
from collections import defaultdict
from functools import partial
from typing import Iterable, Tuple, List, Sequence, DefaultDict, Dict
from pprint import pprint

Point = Tuple[int, ...]
Centroid = Point

def mean(data: Iterable[float]) -> float:
    '''Accurate Arithmetic mean'''
    data = list(data)
    return fsum(data) / len(data)


def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip) -> float:
    ''' Eucliadean Distance between 2 points'''
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, List[Point]]:
    ''' Group the datapoints to its closest centroid'''
    d: DefaultDict = defaultdict(list)
    for point in data:
        #closest_centroid = min(centroids, key=lambda centroid: dist(point, centroid))
        closest_centroid = min(centroids, key= partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    '''Compute the centrids of groups'''
    return [tuple(map(mean, zip(*group))) for group in groups]

def k_means(data: Iterable[Point], k: int=2, iterations: int=50) -> List[Centroid]:
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())

    return centroids

if __name__ == '__main__':
    
    points = [
        (10, 40, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23)
    ]

    centroids = k_means(points, k=3)
    pprint(centroids)
    d = assign_data(centroids, points)
    pprint(d)