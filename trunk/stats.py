class Stats:
    correct = 0
    incorrect = 0

    @property
    def sum(self):
        return self.correct + self.incorrect

    @property
    def mean(self):
        if self.sum:
            return 1.0 * self.correct / self.sum
        else:
            return 0

    @property
    def mean_percent(self):
        return self.mean * 100
