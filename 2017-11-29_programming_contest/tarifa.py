import sys

file = sys.stdin.readlines()

lines = []
for line in file:
    line = int(line.rstrip())
    lines.append(line)

X = lines[0]
N = lines[1]
data_used = lines[2:]

print(X)
print(N)
print(data_used)