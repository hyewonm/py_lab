Fn = [1, 1]
N = int(input('fibonacci number? : '))
for i in range(2, N):
    Fn.append(Fn[i-1] + Fn[i-2])
for i in range(0, N):
    if i == N-1:
        print(Fn[i])
    else:
        print(Fn[i], end = ',')

print('F',N, "=", Fn[N-1])