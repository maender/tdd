def handle_strike():
    pass

def handle_spare(scores: list, frame: int):
    try:
        return 10 + scores[frame+1][0]
    except:
        return sum(scores[frame])

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
        if sum(score) == 10:
            if score[0] == 10:
                pass
            else:
                total += handle_spare(scores, idx)
        else:
            total += sum(score)

    return total