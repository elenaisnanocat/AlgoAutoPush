'''
경로1 경로2 비용

Kruskal 알고리즘의 동작
1. 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
   즉, 가장 낮은 가중치를 먼저 선택한다. 사이클을 형성하는 간선을 제외한다. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.
'''

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])
    connected = set([costs[0][0]])
    
    while len(connected) != n: #연결된 경로가 섬 개수랑 같지 않을때
        for cost in costs:
            if cost[0] in connected and cost[1] in connected: #경로 이미 있을경우
                continue
            if cost[0] in connected or cost[1] in connected: #없을 경우
                connected.update([cost[0], cost[1]]) 
                answer += cost[2] #비용 추가
                break
    return answer