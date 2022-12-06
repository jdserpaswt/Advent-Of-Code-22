# We define a set containing all winning cases
wins = {'A Y', 'B Z', 'C X'}
draws = {'A X', 'B Y', 'C Z'}
score = 0

with open('data/input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]
    for s in data:
        # check for win condition
        if s in wins:
            score += 6
        elif s in draws:
            score += 3
        
        move = s[-1]
        if move == 'X':
            score += 1
        elif move == 'Y':
            score += 2
        elif move == 'Z':
            score += 3

print(score)