print ('Рост учеников:')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print ('Рост Пети')
X = int(input())

sorted(A) #удобно

for i in range (len(A)):
    if A[i]<X:
        print(X)
        break