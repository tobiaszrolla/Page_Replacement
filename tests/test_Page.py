from src.models.PageTable import PageTable
def test_Page():
    MEMORY_SIZE = 100
    p_table = PageTable(MEMORY_SIZE)

    assert p_table.pages_in_memory == 0
    assert len(p_table.frames) == MEMORY_SIZE