from src.models.PageTable import PageTable
from src.algorithms.Algorithm import Algorithm
class Engine:
    def __init__(self, algorithm : Algorithm, trace, max_time=100, memory_size = 100, table_size = 1000):
        self.trace = trace
        self.max_time = max_time
        self.page_table = PageTable(memory_size, table_size)
        self.algorithm = algorithm 

        self.time = 0
        self.index = 0

        # statystyki
        self.page_faults = 0
        self.context_switches = 0
        self.io_operations = 0

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

        if result == "io":
            self.io_operations += 1

    def step(self):
        event = self.trace[self.index]
        self.process_event(event)
        self.index += 1
    def run(self):
        while self.index < len(self.trace) and self.time < self.max_time:
            self.step()
            self.time += 1