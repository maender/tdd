from modules.bowling_refactoring import bowling_score  # format_scores


'''
Cas limites :   spare au dernier lancer
                strike au dernier ou avant dernier lancer

Tests à faire : partie avec que des lancers à 0
                partie avec que des open frames
                partie avec que des spares
                partie avec que des strikes
                mix sans puis avec spare / strike à la fin
'''

def test_emptyGame():
    frames = [0 for x in range(20)]
    assert bowling_score(frames) == 0

def test_GameWith10Pts():
    frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert bowling_score(frames) == 10

def test_GameWithOneStrikeAtFirstFrame():
    frames = [10, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert bowling_score(frames) == 20

def test_GameWithOneStrikeAtLastFrame():
    frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 10, 0, 0]
    assert bowling_score(frames) == 19

def test_GameWithOneSpareAtFisrtFrame():
    frames = [9, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert bowling_score(frames) == 20

def test_GameWithOneSpareAtLastFrame():
    frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 9, 1, 0]
    assert bowling_score(frames) == 19

def test_GameWithOnlySpares():
    frames = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 1]
    assert bowling_score(frames) == 182

def test_GameWith2StrickesInARowAtBegin():
    frames = [10, 10, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert bowling_score(frames) == 40

def test_GameWith2StrickesInARowAtEnd():
    frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 10, 10, 0]
    assert bowling_score(frames) == 38

def test_GameWithOnlyStrikes():
    frames = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert bowling_score(frames) == 300

"""def test_FormatScore():
    frames = [10, 8, 2, 7, 0, 10, 1, 7, 9, 1, 10, 8, 2, 9, 1, 10, 10, 10]
    assert format_scores(frames) == [[10, 0], [8, 2], [7, 0], [10, 0], [1, 7], [9, 1], [10, 0], [8, 2], [9, 1], [10, 10, 10]]"""