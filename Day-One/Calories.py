with open('data/input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]
    greatest = 0
    current = 0
    for s in data:
        #if we hit the end of an elf's list we reset counter
        if not s:
            current = 0
            continue
        #we assume that all input is clean and always a valid int
        current += int(s)
        #we check to see if the current number is the largest we've counted so far
        if current > greatest:
            greatest = current
    
    print("The largest sum is: ", greatest)