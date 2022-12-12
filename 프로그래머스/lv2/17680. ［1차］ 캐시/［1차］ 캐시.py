def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize >= 1:
            #cache miss 아직 없음
            if city not in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
            #cache hit 이미 있음
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        #cacheSize가 1보다 작은 경우 cache에 저장이 불가능함으로 cache miss
        else:
            time += 5
    return time