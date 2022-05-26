from collections import defaultdict
data = input().split(" ")
n, m = data[0], data[1]

n_array = [input() for i in range(int(n))]
m_array = [input() for i in range(int(m))]

# n_array = ["a", "a", "b", "a", "b", "a", "b"]
# m_array = ["a", "b"]

n_ddict = defaultdict(lambda: "-1")
for i, j in enumerate(n_array, start=1):
    if n_ddict[j] == "-1":
        n_ddict[j] = [str(i)]
    else:
        n_ddict[j].append(str(i))
        
# print(n_ddict)
# print(m_array)
#print final output
for i in m_array:
    print(" ".join(n_ddict[i])) if n_ddict[i] != "-1" else print("-1")