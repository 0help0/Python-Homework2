#1
print ('Введите список, закончив его числом 0')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
print('Введите число k')
k = int(input())
dl = len(A)
while k in A:
    A.remove(k)
A.pop(0)
A.pop(len(A)-1)

print (A)

#2
print ('Введите число А')
A = int(input())
fib = [0]*10000
fib[1] = 1 
for i in range(2,A+5):
        fib[i] = fib[i-2] + fib[i-1]
        if A == fib[i]:
            print(' ',i)
            break
        elif A<i:
            print (-1)


#3
print ('Введите значения списка, закончив их нулём')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())

sorted(A)

print(A[2])

#4
print ('Введите значения списка, закончив их нулём')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
sorted(A)
print(A)
for i in range(0,len(A)-1):
    if A[i] == A[i+1]:
        S += 1

print(S)


#5
print ('Введите значения списка, закончив их нулём')
A = [1]
B = 0 
C = -1
D = 0
buff = 1
while buff != 0:
    i +=1
    A.insert(C,(buff))
    buff = int(input())

A.pop(0)
A.pop(len(A)-1)
    
N = A 

for C in range(len(A)-1):
    for D in range(len(A)-1):
        if (A[C] == A[D]) and (C!=D):
            N[C] = 0
            N[D] = 0

while 0 in N:
    N.remove(0)

print (N)

#6
print ('Введите значения списка, закончив их нулём')
A = [1]
B = 0 
C = -1
D = 0
buff = 1
while buff != 0:
    C += 1
    A.insert(C,(buff))
    buff = int(input())
A.pop(0)
A.pop(len(A)-1)
print(A)
N = A
for C in range (1,(len(A) // 2) * 2):
    buff = A[C - 1]
    N[C] = buff
    print(A[C - 1])
    buff = A[i]
    N[C - 1] = buff
print(N)

#7
print ('Введите значения списка, закончив их нулём')
A = [1]
B = 0 
C = -1
D = 0
buff = 1
while buff != 0:
    C += 1
    A.insert(C,(buff))
    buff = int(input())
A.pop(0)
A.pop(len(A) - 1)
print('Введите k')
k = int(input())
k -= 1
v = k
for i in range(k + 1,len(A)):
    A.insert(v,A[C])
    A.pop(A[C + 1])
    v += 1
A.pop()
print(A)

#8
print ('Введите значения списка, закончив их нулём')
A = [1]
B = 0 
C = -1
D = 0
buff = 1
while buff != 0:
    C +=1
    A.insert(C,(buff))
    buff = int(input())
A.pop(0)
A.pop(len(A)-1)
print('Введите k')
k = int(input())
print('Введите C')
M = int(input())
A.append(M)
A[k+1] = A[len(A)-1]
A.pop()
print(A)
