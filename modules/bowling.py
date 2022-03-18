STRIKE = 10
SPARE = 10
LAST_FRAME = 9

class BowlingGame:
    def __init__(self) -> None:
        self.scores = list()
        self.multi = list()
        self.frames = 0
        self.chance = 0
        self.last_throw = 0

    def fromGame(self, throws):
        for throw in throws:
            

        return sum([x * y for x, y in zip(self.score, self.multi)])

    def addMulti(self, type):
        if self.frame == LAST_FRAME:
            pass

    def fromThrow(self, throw):
        if self.chance == 0:
            if throw == 10:
                self.addMulti('strike')
                self.scores.append(STRIKE)
            else:
                self.last_throw = throw
                self.chance += 1
        else:
            if self.last_throw + throw == SPARE:
                self.addMulti('spare')
            self.scores.append(self.last_throw + throw)
            self.chance = self.last_throw = 0

    def calculateScore(self, value):
        if type(value) == list:
            return self.fromGame(value)
        elif type(value) == int:
            return self.fromThrow(value)
        else:
            raise TypeError("Bad type of input !")