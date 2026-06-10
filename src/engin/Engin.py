from src.models.PageTable import PageTable
from src.algorithms.Algorithm import Algorithm
from src.engin.Logger import Logger


class Engine:
    def __init__(self, algorithm: Algorithm, trace, max_time=100, memory_size=100):
        self.trace = trace
        self.max_time = max_time
        self.page_table = PageTable(memory_size)
        self.algorithm = algorithm
        self.logger = Logger()

        self.time = 0
        self.index = 0

        self.page_faults = 0
        self.hits = 0
        self.replacements = 0
        self.write_backs = 0

    def process_event(self, event):
        process = event["process"]
        page = event["page"]
        op = event["op"]

        page_id = (process, page)

        result = self.page_table.access(
            page_id,
            op,
            self.algorithm,
            self.time
        )

        if result == "fault":
            self.page_faults += 1
            self.replacements += 1

        elif result == "hit":
            self.hits += 1

        if result == "write_back":
            self.write_backs += 1

    def step(self):
        event = self.trace[self.index]
        self.process_event(event)
        self.index += 1
        self.logger.log(self.page_table.frames, self.time)

    def run(self):
        while self.index < len(self.trace) and self.time < self.max_time:
            self.step()
            self.time += 1

    def get_metrics(self):
        total = self.page_faults + self.hits
        return {
            "page_faults": self.page_faults,
            "hits": self.hits,
            "hit_ratio": self.hits / total if total > 0 else 0,
            "replacements": self.replacements,
            "write_backs": self.write_backs
        }