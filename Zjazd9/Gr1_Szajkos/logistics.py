"""
Biedny rybak nie wie gdzie mieszkać :(
data/cities.txt to mapa terenu.
Literki to nazwy miast.
Musimy obliczyć, które 4 miasta rybak może najszybciej objechać,
żeby zużyć jak najmniej paliwa/czasu.

1. Parsowanie pliku. Utwórz obiekty klasy City, w których zawszesz jego współrzędne.
2. Klasa "Map". Metoda "distance" obliczy odległość między dwoma zadanymi miastami.
3. Używając city_map.distance(city_a, city_b) znajdź najkrótszą 'pętlę' 4 miast
"""
from math import sqrt
from logistics_utils.loader import load_cities, City
from itertools import permutations


def distance(city_a: City, city_b: City) -> float:
    x_distance = abs(city_a.x - city_b.x)
    y_distance = abs(city_a.y - city_b.y)
    return sqrt(x_distance**2 + y_distance**2)


def city_loop_distance(cities: list[City]) -> float:
    """city_a, city_b, city_c, city_d"""
    total_distance = 0
    for i in range(len(cities)-1):
        total_distance += distance(cities[i], cities[i+1])
    total_distance += distance(cities[0], cities[-1])
    return total_distance


def find_shortest_loop_of_cities(cities: list[City], loop_size: int):
    perm = permutations(cities, loop_size)
    results = []
    for permutation in perm:
        loop_distance = city_loop_distance(list(permutation))
        results.append((permutation, loop_distance))
    return min(results, key=lambda result: result[1])


def main():
    cities = load_cities("data/cities.txt")
    print(find_shortest_loop_of_cities(cities, 4))


if __name__ == '__main__':
    main()
