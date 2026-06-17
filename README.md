# Process Scheduler

This is a project created for a university class. It implements five Page replacment algorithms:
FIFO, LFU, MFU, LRU, NRU.

It also provides a research environment and a graphical user interface (GUI).  
The project is written in Python.

---

## Research Environment

You can create examples by specifying:

- probability of context change
- probabilty of page replacment
- context size
- working set size
- number of pages per process
- number of process

For the execution engine, you can configure:
- memory size
- simulation end time

---

## How to Run

1. Clone the repository

2. Create a virtual environment:
    ```bash
    python -m venv path/to/venv
    ```

3. Activate the virtual environment:

    Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

    Windows:
    ```bash
    venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run app:
    ```bash
    python main.py
    ```
    
