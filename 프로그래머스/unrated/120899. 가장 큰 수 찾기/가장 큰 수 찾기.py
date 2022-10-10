def solution(array):
    answer = []
    m_array = max(array)
    answer.append(m_array)
    for i in array:
        if i == m_array:
            idx = array.index(i)
            answer.append(idx)
    return answer