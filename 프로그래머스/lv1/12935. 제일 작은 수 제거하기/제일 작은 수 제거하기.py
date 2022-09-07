def solution(arr):
    if len(arr) != 1:
        min_num = min(arr)
        arr.remove(min_num)
        ans = arr
        return ans
    else:
        ans = [-1]
        return ans