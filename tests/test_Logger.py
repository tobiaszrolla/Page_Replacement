import json
from pathlib import Path

from src.engin.Engin import Engine
from src.algorithms.LFU import LFU
from src.data.generateData import generate_data

def test_logger_save_to_file():

    trace = generate_data(0.2, 0.2, 100, 10, 1000, 10)
    engine = Engine(
        algorithm=LFU(),
        trace=trace,
        max_time=700,
        memory_size=10,
        table_size=10
    )

    engine.run()

    Path("out").mkdir(exist_ok=True)

    path = "out/logger_test.json"
    path2 = "out/metric_test.json"

    engine.logger.saveRawResults(path)
    engine.logger.saveMetrics(path2, engine.get_metrics())

    with open(path, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert "frames" in data[0]

    print("\nZapisano plik:", path)