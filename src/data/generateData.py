from random import random, randint
from collections import deque, defaultdict

def generate_data(
    context_switch_probability=0.2,
    write_probability=0.2,
    n_processes=3,
    n_pages=20,
    length=50,
    context_size=3,
    page_reuse=0.7,
    working_set_size=5
):
    data = []

    context = deque()
    for _ in range(context_size):
        context.append(randint(0, n_processes - 1))

    working_set = defaultdict(list)

    for p in range(n_processes):
        working_set[p] = [randint(0, n_pages - 1) for _ in range(working_set_size)]

    current_process = context[0]

    for _ in range(length):

        # zmiana procesu
        if random() < context_switch_probability:
            current_process = randint(0, n_processes - 1)
            context.popleft()
            context.append(current_process)

        else:
            current_process = context[randint(0, len(context) - 1)]

        if working_set[current_process] and random() < page_reuse:
            current_page = working_set[current_process][randint(0, len(working_set[current_process]) - 1)]
        else:
            current_page = randint(0, n_pages - 1)
            working_set[current_process].append(current_page)

            if len(working_set[current_process]) > context_size:
                working_set[current_process].pop(0)

        op = "write" if random() < write_probability else "read"

        data.append({
            "process": current_process,
            "page": current_page,
            "op": op
        })

    return data