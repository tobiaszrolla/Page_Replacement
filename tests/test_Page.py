from src.models.PageTable import PageTable
def test_Page():
    TABLE_SIZE = 1000
    MEMORY_SIZE = 100
    p_table = PageTable(MEMORY_SIZE, TABLE_SIZE)

    assert p_table.table_size == TABLE_SIZE
    assert p_table.pages_in_memory == 0
    assert len(p_table.frames) == MEMORY_SIZE