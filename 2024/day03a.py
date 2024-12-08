import re

with open('corrupted_memory.txt', 'r') as file:
    data = file.read()

instructions = re.findall("mul\\([0-9]+,[0-9]+\\)", data)

result = 0

for inst in instructions:
    nums = list(map(int, inst[4:-1].split(',')))
    if nums[0] > 999 or nums[1] > 999:
        continue
    result += nums[0] * nums[1]
print(result)