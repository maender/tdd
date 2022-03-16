STRIKE = (10, 0)
LAST_FRAME_ONLY_STRIKES = (10, 10, 10)

STRIKE_SCORE = 10
STRIKE_OR_SPARE_SCORE = 10

end_of_unfinished_game = lambda x, idx : len(x) < 10 and idx == len(x) - 1
is_strike_or_spare = lambda x, idx : idx < 9 and sum(x) == 10
is_strike = lambda x : x[0] == 10

def calculate_second_strike_bonus(next_throws : list, idx : int):
    total = 0

    try:
        total = STRIKE_SCORE + next_throws[idx + 2][0]
    except:
        total = STRIKE_SCORE + next_throws[idx + 1][1]

    return total

def calculate_strike_bonus(next_throws : list, idx : int):
    total = 0

    if is_strike(next_throws[idx + 1]):
        total += calculate_second_strike_bonus(next_throws, idx)
    else:
        total = sum(next_throws[idx + 1])

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

def bowling_score(frames : list):
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
    for idx, frame in enumerate(frames):
        if end_of_unfinished_game(frames, idx):
            break
        elif is_strike_or_spare(frame, idx):
            total += STRIKE_OR_SPARE_SCORE + calculate_bonus(frames, idx, is_strike(frame))
        else: total += sum(frame)

    return total

def best_possible_score(frames : list):
    for i in range(len(frames) + 1, 10):
        frames.append(STRIKE)
    frames.append(LAST_FRAME_ONLY_STRIKES)

    return bowling_score(frames)