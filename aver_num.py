N = int(input('input : '))

print(type(N))

num = []
for i in range(0, N):
    num.append(int(input()))

sum = 0
for i in range(0, N):
    sum += num[i]

print(sum)



