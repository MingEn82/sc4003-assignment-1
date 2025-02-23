import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def clear_scores(self):
        self.scores.clear()
    
    def show_plot(self, smoothen=False):
        x = [i+1 for i in range(len(self.scores))]
        if smoothen:
            y = self._smoothen_rewards(self.scores)
        else:
            y = self.scores
        plt.plot(x, y)
        plt.xlabel("Iterations")
        plt.ylabel("Cumulative Rewards")
        plt.show()
    
    def _smoothen_rewards(self, rewards, smoothing_factor=0.9):
        smoothed_rewards = [rewards[0]]
        for reward in rewards[1:]:
            smoothed_rewards += [
                smoothed_rewards[-1] * smoothing_factor
                + reward * (1 - smoothing_factor)
            ]
        return smoothed_rewards