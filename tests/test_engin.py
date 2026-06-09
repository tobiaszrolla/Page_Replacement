from src.engin.Engin import Engine
from src.algorithms.NRU import NRU
from src.algorithms.LRU import LRU

def test_engine_run():
    trace = [
        {"process": 0, "page": 1, "op": "read"},
        {"process": 0, "page": 2, "op": "read"},
        {"process": 1, "page": 1, "op": "write"},
        {"process": 1, "page": 2, "op": "read"},
        {"process": 2, "page": 1, "op": "read"},
    ]

    engine = Engine(
        algorithm=LRU(),
        trace=trace,
        max_time=100,
        memory_size=2,
        table_size=10
    )

    engine.run()

    assert engine.index == len(trace)
    assert engine.time > 0
    assert engine.page_faults >= 0