from src.algorithms.Algorithm import Algorithm
class LRU(Algorithm):
    def __init__(self):
        pass
    def select_victim(self, frames):
        victim = frames[0]
        for f in frames:
            if f.last_use > victim.last_use:
                victim = f
        return victim