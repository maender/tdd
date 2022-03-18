import pytest
from modules.bowling import BowlingGame

STRIKE = (10, 0)

'''
Games are represented by a list of 10 tuples of 2 throws
Strikes are represented by the (10, 0) tuple except for last frame
because then you have 3 throws
'''

# [0,10,10,10,10,10,10,10,10,10,10,10,10]

def test_emptyGameFull():
    frames = [0 for x in range(20)]
    assert BowlingGame().calculateScore(frames) == 0

def test_emptyGameIte():
    frames = [0 for x in range(20)]

# def test_gameWith10Pts():
#     frames = [1, 0,1, 0,1, 0,1, 0,1, 0,1, 0,1, 0,1, 0,1, 0,1, 0]
#     assert bowling_score(frames) == 10

# def test_gameWithOneSpareAtFisrtFrame():
#     frames = [9, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#     assert bowling_score(frames) == 20

# def test_gameWithOneSpareAtLastFrame():
#     frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 9, 1, 0]
#     assert bowling_score(frames) == 19

# def test_gameWithOneStrikeAtFirstFrame():
#     frames = [10, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#     assert bowling_score(frames) == 20

# def test_gameWithOneStrikeAtLastFrame():
#     frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 10, 0, 0]
#     assert bowling_score(frames) == 19

# def test_gameWithOnlySpares():
#     frames = [9, 1,9, 1,9, 1,9, 1,9, 1,9, 1,9, 1,9, 1,9, 1,9, 1,1]
#     assert bowling_score(frames) == 182

# def test_gameWith2StrickesInARowAtBegin():
#     frames = [10, 10, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#     assert bowling_score(frames) == 40

# def test_gameWith2StrickesInARowAtEnd():
#     frames = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 10, 10, 0, 0]
#     assert bowling_score(frames) == 38

# def test_gameWithOnlyStrikes():
#     frames = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#     assert bowling_score(frames) == 300

# def test_fromRandomGame():
#     frames = [7, 1, 5, 4, 5, 2, 6, 4, 4, 1, 8, 1, 2, 8, 0, 1, 7, 0, 10, 10, 9]
#     assert bowling_score(frames) == 99

