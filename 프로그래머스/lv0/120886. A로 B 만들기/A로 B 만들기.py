def solution(before, after):
    answer = 0
    dic_b = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    dic_a = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    
    for i in dic_b:
        # print(i)
        for j in before:
            if i == j:
                dic_b[i] += 1
    print(dic_b)
    
    for i in dic_a:
        # print(i)
        for j in after:
            if i == j:
                dic_a[i] += 1
    print(dic_a)
    
    if dic_b == dic_a:
        return 1
    else:
        return 0
    