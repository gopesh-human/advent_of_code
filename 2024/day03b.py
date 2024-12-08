import re

with open('corrupted_memory.txt', 'r') as file:
    data = file.read()

raw_instructions = re.findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)", data)

instructions = []
do = True
for inst in raw_instructions:
    if do and inst == "don't()":
        do = False
    elif not do and inst == "do()":
        do = True
    elif do and inst != "do()":
        instructions.append(inst)

print(instructions)
result = 0

for inst in instructions:
    nums = list(map(int, inst[4:-1].split(',')))
    if nums[0] > 999 or nums[1] > 999:
        continue
    result += nums[0] * nums[1]
print(result)
