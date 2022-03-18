STRIKE = 10
LAST_FRAME = 9
"""BEFORE_LAST_FRAME = 8
FIRST_THROW = 0
LAST_BONUS_THROW = 2"""

def strike(scores: list, frame: int):
    return sum(scores[frame:frame+3])

def spare(scores: list, frame: int):
    return sum(scores[frame-1:frame+2])

"""def extra_points(scores: list):
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

def format_scores(pins_knock_down_list: list):
    scores = []
    frame = []
    first_chance = True
    for idx, value in enumerate(pins_knock_down_list):
        if len(scores) == LAST_FRAME:
            frame.append(value)
            if first_chance:
                first_chance = False
            else:
                if idx + 1 == len(pins_knock_down_list):
                    scores.append(frame)
        else:
            frame.append(value)
            if first_chance:
                if value == STRIKE:
                    frame.append(0)
                    scores.append(frame)
                    frame = []
                else:
                    first_chance = False
            else:
                scores.append(frame)
                frame = []
                first_chance = True
    return scores"""

def bowling_score(pins_knock_down_list : list):
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
    frame = 0
    last_chance = False
    first_throw = 0

    # scores = format_scores(pins_knock_down_list)

    for idx, throw in enumerate(pins_knock_down_list):
        if frame == LAST_FRAME:
            total += throw
        else:
            if throw == STRIKE:
                total += strike(pins_knock_down_list, idx)
                frame += 1
            elif last_chance:
                if (first_throw + throw) == 10:
                    total += spare(pins_knock_down_list, idx)
                else:
                    total += (first_throw + throw)
                last_chance = False
                frame += 1
            else:
                first_throw = throw
                last_chance = True
    return total

    """for frame, score in enumerate(scores):
        if extra_points(score):
            if score[FIRST_THROW] == STRIKE:
            #    total += strike(scores, frame)
                pass
            else:
            #    total += spare(scores, frame)
                pass
        else:
            #total += sum(score)
            pass"""


