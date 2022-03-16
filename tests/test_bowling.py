import pytest
from modules.bowling import bowling_score


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
    frames = [(0, 0) for x in range(10)]
    assert bowling_score(frames) == 0

def test_gameWith10Pts():
    frames = [(1, 0) for x in range(10)]
    assert bowling_score(frames) == 10

def test_gameWithOneSpareAtFisrtFrame():
    frames = [(1, 0) for x in range(10)]
    frames[0] = (9, 1)
    assert bowling_score(frames) == 20

def test_gameWithOneSpareAtLastFrame():
    frames = [(1, 0) for x in range(10)]
    frames[-1] = (9, 1, 0)
    assert bowling_score(frames) == 19

def test_gameWithOneStrikeAtFirstFrame():
    frames = [(1, 0) for x in range(10)]
    frames[0] = (10, 0)
    assert bowling_score(frames) == 20

def test_gameWithOneStrikeAtLastFrame():
    frames = [(1, 0) for x in range(10)]
    frames[-1] = (10, 0, 0)
    assert bowling_score(frames) == 19

def test_gameWithOnlySpares():
    frames = [(9, 1) for x in range(10)]
    frames[-1] = (9, 1, 1)
    assert bowling_score(frames) == 182

def test_gameWith2StrickesInARowAtBegin():
    frames = [(1, 0) for x in range(10)]
    frames[0] = frames[1] = (10,0)
    assert bowling_score(frames) == 40

def test_gameWith2StrickesInARowAtEnd():
    frames = [(1, 0) for x in range(10)]
    frames[-2] = (10, 0)
    frames[-1] = (10, 0, 0)
    assert bowling_score(frames) == 38

def test_gameWithOnlyStrikes():
    frames = [(10, 0) for x in range(10)]
    frames[-1] = (10, 10, 10)
    assert bowling_score(frames) == 300

def test_fromRandomGame():
    frames = [(7, 1), (5, 4), (5, 2), (6, 4), (4, 1), (8, 1), (2, 8), (0, 1), (7, 0), (10, 10, 9)]
    assert bowling_score(frames) == 99

    frames = [(7, 1), (1, 9), (8, 2), (4, 5), (10, 0), (4, 0), (9, 0), (4, 4), (1, 7), (2, 8, 10)]
    assert bowling_score(frames) == 112
