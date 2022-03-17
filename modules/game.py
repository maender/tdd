from modules.bowling import bowling_score

class Game:
    def __init__(self, pin_collector=None, display=None) -> None:
        self.pin_collector = pin_collector
        self.display = display
        self.fallen = list()

    def calculate_score(self):
        return bowling_score(self.fallen)

    def play(self):
        while True:
            try:
                a = self.pin_collector.fallen()
                self.fallen.append(a)
            except:
                break

        score = self.calculate_score()
        self.display.display_score(score)
