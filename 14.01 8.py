print ('Последовательность с нулём в конце')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print('Объект больше чем перед ним')

for i in range (len(A)):
    if A[i]>A[i-1]:
        S += 1
        

print(S-2)