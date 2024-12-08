with open('reactor_reports.txt', 'r') as file:
    data = file.readlines()

reports = []
for line in data:
    reports.append(list(map(int, line.strip().split(' '))))

def is_cont(report):
    original = report[:]
    report.sort()
    if original == report or original == report[::-1]:
        return True
    return False

def has_proper_steps(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

safe_reports = 0
for report in reports:
    if is_cont(report) and has_proper_steps(report):
        safe_reports += 1
print(safe_reports)
