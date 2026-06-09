from src.algorithms.Algorithm import Algorithm

class NRU(Algorithm):
    def __init__(self):
        pass

    def select_victim(self, frames):
        class_0 = []
        class_1 = []
        class_2 = []
        class_3 = []

        for page in frames:
            if page is None:
                continue

            r = page.referenced
            m = page.modified

            if not r and not m:
                class_0.append(page)
            elif not r and m:
                class_1.append(page)
            elif r and not m:
                class_2.append(page)
            else:
                class_3.append(page)

        if class_0:
            return class_0[0]
        if class_1:
            return class_1[0]
        if class_2:
            return class_2[0]
        return class_3[0]