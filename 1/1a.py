with open('1.txt') as f:
    lines = f.readlines()
    count = 0
    for idx, l in enumerate(lines):
        if idx != 0 and int(l) > int(lines[idx-1]):
            count += 1
    print(count)
