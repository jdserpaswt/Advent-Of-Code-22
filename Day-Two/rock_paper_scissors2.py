moves = {"A": "Rock","B": "Paper","C": "Scissors"}
points_per_move = {"Rock": 1,"Paper": 2,"Scissors": 3}
points_per_result = {"X": 0,"Y": 3,"Z": 6}
final_score = 0

with open('data/input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]
    for line in data:
        score = 0
        #extract data
        opponent_move = moves[line[0]]
        outcome = line[-1]
        #check outcome
        if(outcome == 'X'):
            #check opponent move
            if(opponent_move == 'Rock'):
                score += points_per_move["Scissors"]
            if(opponent_move == 'Paper'):
                score += points_per_move["Rock"]
            if(opponent_move == 'Scissors'):
                score += points_per_move["Paper"]
        if(outcome == 'Y'):
            #on tie we just play same move.
            #so just choose opponent move on dictionary
            score += points_per_move[opponent_move]
        if(outcome == 'Z'):
            #check opponent move
            if(opponent_move == 'Rock'):
                score += points_per_move["Paper"]
            if(opponent_move == 'Paper'):
                score += points_per_move["Scissors"]
            if(opponent_move == 'Scissors'):
                score += points_per_move["Rock"]

        score += points_per_result[outcome]
        print(score)
        final_score += score
    print(final_score)