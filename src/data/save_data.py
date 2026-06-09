import json
from datetime import datetime

def save_data(
    data,
    file_path,
    n_processes=None,
    n_pages=None,
    context_size=None
):
    output = {
        "meta": {
            "created_at": datetime.now().isoformat(),
            "n_processes": n_processes,
            "n_pages": n_pages,
            "context_size": context_size,
            "length": len(data)
        },
        "trace": data
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)