import sys

N, M = map(int, input().split())
number_pokemon = 1
pokemon_dict1 = {}
pokemon_dict2 = {}

for _ in range(1,N+1):
    name = str(sys.stdin.readline()).strip()
    pokemon_dict1[number_pokemon] = name
    pokemon_dict2[name] = number_pokemon
    number_pokemon += 1

for _ in range(M):
    pokemon = str(sys.stdin.readline()).strip()
    if pokemon.isdigit():
        print(pokemon_dict1[int(pokemon)])
    else:
        print(pokemon_dict2[pokemon])