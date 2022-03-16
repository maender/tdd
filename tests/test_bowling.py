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
    frames = [[0, 0] for x in range(10)]
    assert bowling_score(frames) == 0

def test_GameWith10Pts():
    frames = [[1, 0] for x in range(10)]
    assert bowling_score(frames) == 10

def test_GameWithOneSpareAtFisrtFrame():
    frames = [[1, 0] for x in range(10)]
    frames[0] = [9, 1]
    assert bowling_score(frames) == 20

def test_GameWithOneSpareAtLastFrame():
    frames = [[1, 0] for x in range(10)]
    frames[-1] = [9, 1, 0]
    assert bowling_score(frames) == 19
    