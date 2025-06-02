import json
import os

LOG_FILE = "logs.json"

def log_click_to_file(entry):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_logs_for_code(code):
    import json
    import os

    LOG_FILE = "logs.json"

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    return [entry for entry in data if entry["short_code"] == code]
