with open('page_order_rules.txt', 'r') as file:
    rules = list(map(lambda x: [int(a) for a in x.strip().split('|')], file.readlines()))
rules_1 = list(map(lambda x: x[0], rules))
rules_2 = list(map(lambda x: x[1], rules))

with open('page_order_updates.txt', 'r') as file:
    updates = list(map(lambda x: [int(a) for a in x.strip().split(',')], file.readlines()))

def correct_line(line):
    for i in range(len(line)):
        for j in range(len(line)):
            m = j
            for k in [l for l, val in enumerate(rules_1) if val == line[j]]:
                if rules_2[k] in line[:m]:
                    line[m], line[line.index(rules_2[k])], m = rules_2[k], line[m], line.index(rules_2[k])
    return line

middle_sum = 0
for line in updates:
    correct = True
    for i in range(len(line)):
        for index in [j for j, val in enumerate(rules_1) if val == line[i]]:
            if rules_2[index] in line[:i]:
                correct = False
    if not correct:
        new_line = correct_line(line)
        middle_sum += new_line[len(new_line) // 2]
print(middle_sum)
