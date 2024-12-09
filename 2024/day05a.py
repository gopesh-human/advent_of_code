with open('page_order_rules.txt', 'r') as file:
    rules = list(map(lambda x: [int(a) for a in x.strip().split('|')], file.readlines()))
rules_1 = list(map(lambda x: x[0], rules))
rules_2 = list(map(lambda x: x[1], rules))

with open('page_order_updates.txt', 'r') as file:
    updates = list(map(lambda x: [int(a) for a in x.strip().split(',')], file.readlines()))

middle_sum = 0
for line in updates:
    correct = True
    for i in range(len(line)):
        for index in [j for j, val in enumerate(rules_1) if val == line[i]]:
            if rules_2[index] in line[:i]:
                correct = False
    if correct:
        middle_sum += line[len(line) // 2]
print(middle_sum)
