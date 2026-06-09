import os
import tempfile

from src.data.generateData import generate_data
from src.data.load_data import load_data
from src.data.save_data import save_data 


def test_save_and_load_trace():
    SWICH_PROB = 0.3
    WRITE_PROB = 0.5
    N_PROC = 5
    N_PAGES = 10
    LENGTH = 50
    CTX = 3

    data = generate_data(
        SWICH_PROB,
        WRITE_PROB,
        N_PROC,
        N_PAGES,
        LENGTH,
        CTX
    )

    # tymczasowy plik
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        path = tmp.name

    try:
        # zapis
        save_data(
            data,
            path,
            n_processes=N_PROC,
            n_pages=N_PAGES,
            context_size=CTX
        )

        # odczyt
        meta, loaded_data = load_data(path)

        # 1. długość
        assert len(loaded_data) == LENGTH

        # 2. dane identyczne (ważne!)
        assert loaded_data == data

        # 3. meta sanity check
        assert meta["n_processes"] == N_PROC
        assert meta["n_pages"] == N_PAGES
        assert meta["context_size"] == CTX

    finally:
        os.remove(path)