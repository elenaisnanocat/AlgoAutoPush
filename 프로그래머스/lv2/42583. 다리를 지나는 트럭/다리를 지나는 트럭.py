
def solution(bridge_length, weight, truck_weights):
    answer = 0
    n_truck = 0
    bridge_lst = [0] * bridge_length
    # print(bridge_lst)
    
    time = 0
    while bridge_lst:
        bridge_lst.pop(0)
        time += 1
        if truck_weights:
            if sum(bridge_lst) + truck_weights[0] <= weight:
                bridge_lst.append(truck_weights.pop(0))
            else:
                bridge_lst.append(0)
        # print(bridge_lst)
    return time