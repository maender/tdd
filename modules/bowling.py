STRIKE = 10
STRIKE_OR_SPARE = 10

is_strike_at_last_frame = lambda x : x == 9
is_strike_or_spare = lambda x : sum(x) == 10
is_strike = lambda x : x[0] == 10

def calculate_second_strike_bonus(next_throws : list, idx : int):
    total = 0

    try:
        total = STRIKE + next_throws[idx + 2][0]
    except:
        total = STRIKE + next_throws[idx + 1][1]

    return total

def calculate_strike_bonus_at_regular_frame(next_throws : list, idx : int):
    total = 0

    if is_strike(next_throws[idx + 1]):
        total += calculate_second_strike_bonus(next_throws, idx)
    else:
        total = sum(next_throws[idx + 1])

    return total

def calculate_strike_bonus(next_throws : list, idx : int):
    total = 0

    if is_strike_at_last_frame(idx):
        total = sum(next_throws[idx][1:])
    else:
        total = calculate_strike_bonus_at_regular_frame(next_throws, idx)

    return total

def calculate_spare_bonus(next_throws : list, idx : int):
    total = 0

    try:
        total = next_throws[idx + 1][0]
    except:
        total = next_throws[idx][2]

    return total

def calculate_bonus(next_throws : list, idx : int, strike : bool):
    total = 0

    if strike:
        total = calculate_strike_bonus(next_throws, idx)
    else:
        total = calculate_spare_bonus(next_throws, idx)

    return total

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
            total += STRIKE_OR_SPARE + calculate_bonus(scores, idx, is_strike(score))
        else: total += sum(score)

    return total