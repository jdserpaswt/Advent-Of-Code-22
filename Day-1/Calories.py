from heapq import heappop, heappush


with open('data/input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]
    calories = []
    current = 0
    for s in data:
        #if we hit the end of an elf's list we reset counter
        #negate and add to heap (min-heap)
        if not s:
            heappush(calories, current * -1)
            current = 0
            continue
        #we assume that all input is clean and always a valid int
        current += int(s)
    
    elf_one = heappop(calories) * -1
    elf_two = heappop(calories) * -1
    elf_three = heappop(calories) * -1

    print("The largest sum is: ", elf_one)
    print("The second sum is: ", elf_two)
    print("The third sum is: ", elf_three)

    print("The three elves are carrying a total of: ", elf_one + elf_two + elf_three)