import json

import json

class Logger:
    def __init__(self):
        self.snapshots = []

    def log(self, memory, time=None):
        data = []
        for p in memory:
            data.append(p.page_id if p else None)
        snapshot = {
            "time": time,
            "frames": data
        }

        self.snapshots.append(snapshot)

    def saveRawResults(self, path):
        with open(path, "w") as f:
            json.dump(self.snapshots, f, indent=2)

    def saveMetrics(self, path, metrics: dict):
        with open(path, "w") as f:
            json.dump(metrics, f, indent=2)