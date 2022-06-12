A = int(input())
B = int(input())
C = int(input())

ABC = list(str(A*B*C))

zero = 0
one = 0
two =0
three =0
fo = 0
five = 0
six = 0
se = 0
eight = 0
nin = 0
#
for i in range(len(ABC)):

    if ABC[i] == '0':
        zero += 1
    elif ABC[i] == '1':
        one += 1
    elif ABC[i] == '2':
        two += 1
    elif ABC[i] == '3':
        three += 1
    elif ABC[i] == '4':
        fo += 1
    elif ABC[i] == '5':
        five += 1
    elif ABC[i] =='6':
        six += 1
    elif ABC[i] == '7':
        se += 1
    elif ABC[i] == '8':
        eight += 1
    elif ABC[i] == '9':
        nin += 1


print(zero)
print(one)
print(two)
print(three)
print(fo)
print(five)
print(six)
print(se)
print(eight)
print(nin)

