with open('location_ids.txt', 'r') as file:
    data = file.readlines()

list1 = []
list2 = []

for a in data:
    b = a.strip().split('   ')
    list1.append(int(b[0]))
    list2.append(int(b[1]))

similarity_score = 0

for a in list1:
    similarity_score += a * list2.count(a)

print(similarity_score)
