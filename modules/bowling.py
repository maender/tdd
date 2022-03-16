is_strike_or_spare = lambda x : sum(x) == 10
is_strike = lambda x : x[0] == 10

def handle_strike(scores: list, frame: int):
    try:
        if is_strike(scores[frame+1]):
            if frame == 8:
                return 20 + scores[frame+2][0] + scores[frame+2][1]
            else:
                return 20 + scores[frame+2][0]
        else:
            return 10 + sum(scores[frame + 1])
    except: return sum(scores[frame])

def handle_spare(scores: list, frame: int):
    try: return 10 + scores[frame+1][0]
    except: return sum(scores[frame])

def bowling_score(scores : list):
    '''
    In:
    Scores is a list of 10 tuples (x, y)
    can be (x, y, z) last frame if spare or strike
    where x is the number of keel fallen for first throw
    and y for the second throw of the frame
    (and z for the third)

    Out:
    Point total
    '''

    total = 0
    for idx, score in enumerate(scores):
        if is_strike_or_spare(score):
            if is_strike(score): total += handle_strike(scores, idx)
            else: total += handle_spare(scores, idx)
        else: total += sum(score)

    return total