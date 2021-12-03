with open('1a.txt') as f:
    lines = f.readlines()
    nums = [int(l) for l in lines]
    count = 0
    for idx, l in enumerate(nums):
        if idx > 1 and idx < len(nums):
            w1 = sum(nums[idx-2:idx+1])
            w2 = sum(nums[idx-1:idx+2])
            if w2 > w1:
                count += 1
    print(count)
