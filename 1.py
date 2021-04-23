import sys

filename = sys.argv[1]
try:
    number = int(sys.argv[2])
except ValueError:
    exit("Extension number must be a valid integer.")

lines = []
with open(filename, "r") as f:
    lines = f.readlines()

try:
    f = open(filename + number, "w")
except ValueError:
    exit()

i = 0
while i < len(lines):
    bad = False
    words = lines[i].strip().split()
    for word in words:
        if word == "whale":
            bad = True
            break
    
    if not bad:
        f.write(lines[i])
f.close()