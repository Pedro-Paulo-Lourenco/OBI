N, K = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')].sort(reverse=True)
print(A[K-1])
