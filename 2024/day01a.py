with open('location_ids.txt', 'r') as file:
    data = file.readlines()

list1 = []
list2 = []

for a in data:
    b = a.strip().split('   ')
    list1.append(int(b[0].strip()))
    list2.append(int(b[1].strip()))

sum_diff = 0

for _ in range(len(list1)):
    sum_diff += abs(min(list1) - min(list2))
    list1.remove(min(list1))
    list2.remove(min(list2))
print(sum_diff)
