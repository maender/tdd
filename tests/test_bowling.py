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
    scores = [(0, 0) for x in range(10)]
    assert bowling_score(scores) == 0
    