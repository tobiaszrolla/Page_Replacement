from src.algorithms.Algorithm import Algorithm
class LFU(Algorithm):
    def __init__(self):
        pass
    def select_victim(self, frames):
        victim = frames[0]
        for f in frames:
            if f.use_counter < victim.use_counter:
                victim = f
        return victim