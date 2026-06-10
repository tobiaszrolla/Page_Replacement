from src.engin.Engin import Engine
from src.algorithms.LRU import LRU

def test_engine_run():
    trace = [
        {"process": 0, "page": 1, "op": "read"},
        {"process": 0, "page": 2, "op": "read"},
        {"process": 0, "page": 1, "op": "write"},
        {"process": 1, "page": 1, "op": "write"},
        {"process": 0, "page": 1, "op": "write"},
        {"process": 1, "page": 2, "op": "read"},
        {"process": 2, "page": 1, "op": "read"},
        {"process": 1, "page": 1, "op": "read"},
        {"process": 2, "page": 1, "op": "read"},
        {"process": 2, "page": 1, "op": "read"},
        {"process": 0, "page": 1, "op": "read"}
    ]

    engine = Engine(
        algorithm=LRU(),
        trace=trace,
        max_time=6,
        memory_size=3,
    )

    engine.run()

    assert engine.page_table.frames[0].page_id[0] == 0
    assert engine.page_table.frames[0].page_id[1] == 1
    assert engine.page_table.frames[1].page_id[0] == 1
    assert engine.page_table.frames[1].page_id[1] == 2