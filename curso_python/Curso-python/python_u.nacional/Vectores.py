vector_v = [int(elemento) for elemento in input().split()]
vector_u = [int(elemento) for elemento in input().split()]
print(vector_u)
print(vector_v)

n = len(vector_u)
n2 = len(vector_v)

x = 0

for i in range(n):
    x = vector_u[i] * vector_v[i] + x

print(x)