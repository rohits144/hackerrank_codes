def minimumBribes(q):
    q = [int(i) for i in q]
    bribe = 0
    for i in range(len(q)-1,0, -1):
        # print("i=",i+1)
        if q[i] != i+1:
            if q[i-1] == i+1:
                bribe+=1
                q[i-1], q[i] = q[i], i+1
            elif q[i-2] == i+1:
                bribe+=2
                q[i-2], q[i-1], q[i] = q[i-1], q[i], i+1
            else:
                return "Too Chaotic"
        # print("b=",bribe)
    return bribe


print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))