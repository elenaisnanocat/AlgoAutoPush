def solution(phone_number):
    answer = ''
    ph = ''
    for i in range(len(phone_number)-4):
        ph += '*'
    ph += phone_number[-4:]
    answer = ph
    return answer