from random import random, randint
from collections import deque

def generate_data(
    context_switch_probability=0.2,
    write_probability=0.2,
    n_processes=3,
    n_pages=5,
    length=50,
    context_size=3
):
    data = []

    context = deque()

    for _ in range(context_size):
        context.append(randint(0, n_processes - 1))

    current_process = context[0]

    for _ in range(length):

        if random() < context_switch_probability:
            current_process = randint(0, n_processes - 1)
            context.popleft()
            context.append(current_process)
        else:
            current_process = context[randint(0, len(context) - 1)]

        op = "write" if random() < write_probability else "read"

        data.append({
            "process": current_process,
            "page": randint(0, n_pages - 1),
            "op": op
        })

    return data