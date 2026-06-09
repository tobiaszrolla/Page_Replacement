from src.algorithms.Algorithm import Algorithm

class FIFO(Algorithm):
    def __init__(self):
        self.queue = []

    def select_victim(self, frames):
        for f in frames:
            if f is not None and f not in self.queue:
                self.queue.append(f)

        victim = self.queue.pop(0)
        return victim