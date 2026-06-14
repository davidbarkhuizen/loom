def dicts_to_table(data: list[dict[str, str]] | None) -> str | None:
    if not data:
        return None

    expected_keys = list(data[0].keys())

    for idx, row in enumerate(data):
        if list(row.keys()) != expected_keys:
            raise ValueError("Inconsistent dictionary keys across rows")

    headers = "| " + " | ".join(expected_keys) + " |"
    separators = "| " + " | ".join("---" for _ in expected_keys) + " |"

    rows = [
        "| " + " | ".join(row[key] for key in expected_keys) + " |"
        for row in data
    ]

    return "\n".join([headers, separators] + rows)