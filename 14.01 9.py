print ('Последовательность с нулём в конце')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print('Объектов которые больше чем по сторонам')

for i in range (1,(len(A)-2)):
    if (A[i]>A[i-1]) and (A[i]>A[i+1]):
        S += 1
        

print(S) 