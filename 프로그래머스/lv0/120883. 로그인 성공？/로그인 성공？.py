def solution(id_pw, db):
    answer = 'fail'
    for i in id_pw:
        for j in db:
            if i == j[0]:
                if id_pw[1] == j[1]:
                    answer = "login"
                else:
                    answer = "wrong pw"
            
    return answer