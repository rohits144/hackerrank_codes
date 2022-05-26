from collections import Counter

#total_shoes = int(input())
#shoe_size_dict = Counter(input().split(" "))
#total_customer = int(input())

total_shoes = 10
shoe_size_dict = Counter("2 3 4 5 6 8 7 6 5 18".split(" "))
total_customer = 6

temp_str = ['6 55', '6 45', '6 55', '4 40', '18 60', '10 50']

amount = 0
for i in range(total_customer):
    #data = input().split(" ")
    data = temp_str[i].split(" ")
    size, price = data[0], int(data[1])
    if size in shoe_size_dict.keys() and shoe_size_dict[size]>0:
        amount = amount + price
        shoe_size_dict[size] -= 1

print(amount)