def solution(age):
    answer = ''
    age = str(age)
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in age:
        answer += alpha[int(i)]
    return answer