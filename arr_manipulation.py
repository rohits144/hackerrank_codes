n = 10
q = [[1,2,100], [2,5,100], [3,4,100]]
arr = [0] * (n + 1)

for i in q:
    arr[i[0]-1]+=i[2]
    arr[i[1]]-=i[2]

max = 0
curr = 0
for i in range(n):
    curr += arr[i]
    max=curr if max<curr else max

print(max)