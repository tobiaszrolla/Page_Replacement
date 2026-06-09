from src.data.generateData import generate_data
def test_generate_data():
    SWICH_PROB = 0.3
    WRITE_PROB = 0.5
    N_PROC = 5
    N_PAGES = 10
    LEN = 50
    CTX = 3


    data = generate_data(SWICH_PROB,
                         WRITE_PROB,
                         N_PROC,
                         N_PAGES,
                         LEN,
                         CTX
                         )
    assert len(data) == LEN