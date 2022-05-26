# s = "abcac"
# n = 1



def check(s,n):
    l = len(s)
    if n==0:
        print(0)

    elif n>l:
        fixed = int(n/l)
        extra = int(n%l)
        remaining_str = s[:extra] if extra != 0 else ""
        # print(fixed, extra, remaining_str)
        print(s.count("a")*fixed + remaining_str.count("a"))

    elif n<l:
        print(s[:n].count("a"))

    else:
        print(s.count("a"))


if __name__ == "__main__":
    s = "abcac"
    for n in range(10,20):
        print("\n n = ",n)
        check(s,n)
