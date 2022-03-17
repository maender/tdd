STRIKE = (10, 0)
LAST_FRAME_ONLY_STRIKES = (10, 10, 10)

STRIKE_SCORE = 10
SPARE_SCORE = 10
STRIKE_OR_SPARE_SCORE = 10

end_of_unfinished_game = lambda x, idx : len(x) < 10 and idx == len(x) - 1
is_strike_or_spare = lambda x, idx : idx < 9 and sum(x) == 10
is_strike = lambda x : x[0] == 10
next_n_throws = lambda x, idx, n : x[idx + 1: idx + 1 + n]

is_strike_or_spare_at_last_frame = lambda frame, idx : (frame[0] == 10 or sum(frame[:2]) == 10) and idx == 9
is_strike_new = lambda throw, chance, frame : throw == 10 and chance == 0 and frame <= 9

# def calculate_second_strike_bonus(next_throws : list, idx : int):
#     total = 0

#     try:
#         total = STRIKE_SCORE + next_throws[idx + 2][0]
#     except:
#         total = STRIKE_SCORE + next_throws[idx + 1][1]

#     return total

def calculate_strike_bonus(next_throws : list):
    return sum(next_throws)

def calculate_spare_bonus(next_throws : list):
    return sum(next_throws)

def calculate_bonus(next_throws : list, idx : int, strike : bool):
    total = 0

    # if strike:
    #     total = calculate_strike_bonus(next_throws, idx)
    # else:
    total = calculate_spare_bonus(next_throws, idx)

    return total

def format_input(throws : list):
    out = list()

    throw = 0
    throw1 = 0
    throw2 = 0
    frame = 0
    for val in throws:
        if val == 10 and throw == 0 and frame < 9:
            out.append(STRIKE)
            frame += 1
        elif throw == 0:
            throw1 = val
            throw += 1
        elif frame < 9:
            out.append((throw1, val))
            throw = 0
            frame += 1
        elif throw < 2:
            throw2 = val
            throw += 1
        else:
            out.append((throw1, throw2, val))
            throw += 1
    if throw < 3:
        out.append((throw1, throw2))
    return out

def bowling_score(throws : list):
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

    frames = format_input(throws)
    total = 0
    totalStrikes_and_spares = 0
    frame = 0
    chance = 0
    first_throw_of_frame = 0
    for idx, throw in enumerate(throws):
        if is_strike_new(throw, chance, frame):
            totalStrikes_and_spares += STRIKE_SCORE + calculate_strike_bonus(next_n_throws(throws, idx, 2))
            frame += 1
        elif chance == 1:
            frame += 1
            chance = 0
            if first_throw_of_frame + throw == 10:
                totalStrikes_and_spares += SPARE_SCORE + calculate_spare_bonus(next_n_throws(throws, idx, 1))
            else:
                pass
        else:
            first_throw_of_frame = throw
            chance += 1

    for idx, frame in enumerate(frames):
        if is_strike_or_spare(frame, idx):
            pass
            # if end_of_unfinished_game(frames, idx):
            #     break
            # if not is_strike(frame):
            #     total += STRIKE_OR_SPARE_SCORE + calculate_bonus(frames, idx, is_strike(frame))
        elif not is_strike_or_spare_at_last_frame(frame, idx):
            total += sum(frame)

    return total + totalStrikes_and_spares

def best_possible_score(frames : list):
    for i in range(len(frames) + 1, 10):
        frames.append(STRIKE)
    frames.append(LAST_FRAME_ONLY_STRIKES)

    return bowling_score(frames)
