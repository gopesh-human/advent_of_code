with open('reactor_reports.txt', 'r') as file:
    data = file.readlines()

reports = []
for line in data:
    reports.append(list(map(int, line.strip().split(' '))))

def is_cont(report):
    sorted_report = report[:]
    sorted_report.sort()
    if sorted_report == report or sorted_report == report[::-1]:
        return True
    return False

def has_proper_steps(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

def problem_dampner(report):
    for i in range(len(report)):
        new_report = report[:]
        new_report.pop(i)
        if is_cont(new_report) and has_proper_steps(new_report):
            return True
    return False

safe_reports = 0
for report in reports:
    if is_cont(report) and has_proper_steps(report):
        safe_reports += 1
    elif problem_dampner(report):
        safe_reports += 1
print(safe_reports)
