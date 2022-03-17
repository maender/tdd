STRIKE = 10
LAST_FRAME = 9
BEFORE_LAST_FRAME = 8
FIRST_THROW = 0
LAST_BONUS_THROW = 2

def extra_points(scores: list):
    if sum(scores) == STRIKE:
        return True

def strike_in_a_row(scores: list, frame: int):
    return scores[frame + 1][FIRST_THROW] == STRIKE

def last_frame(frame: int):
    return frame == LAST_FRAME

def before_last_frame(frame: int):
    return frame == BEFORE_LAST_FRAME

def strike(scores: list, frame: int):
    if last_frame(frame):
        return sum(scores[frame])
    elif strike_in_a_row(scores, frame):
        if before_last_frame(frame):
            return sum(scores[frame]) + sum(scores[frame + 1][:LAST_BONUS_THROW])
        else:
            return sum(scores[frame]) + sum(scores[frame + 1]) + scores[frame + 2][FIRST_THROW]
    else:
        return sum(scores[frame]) + sum(scores[frame + 1])

def spare(scores: list, frame: int):
    if frame == LAST_FRAME:
        return sum(scores[frame])
    else:
        return sum(scores[frame]) + scores[frame + 1][FIRST_THROW]

def bowling_score(scores : list):
    '''
    In:
    Scores is a list of 10 lists (x, y)
    can be (x, y, z) last frame if spare or strike
    where x is the number of keel fallen for first throw
    and y for the second throw of the frame
    (and z for the third)

    Out:
    Point total
    '''

    total = 0
    for frame, score in enumerate(scores):
        if extra_points(score):
            if score[FIRST_THROW] == STRIKE:
                total += strike(scores, frame)
            else:
                total += spare(scores, frame)
        else:
            total += sum(score)

    return total
