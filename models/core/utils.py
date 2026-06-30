import json
from pathlib import Path


# =========================
# JSON
# =========================

def load_json(path):

    path = Path(path)

    if not path.exists():

        return {}

    if path.stat().st_size == 0:

        return {}

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_json(path, data):

    path = Path(path)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# =========================
# Safe Get
# =========================

def safe_get(dictionary, key, default=None):

    if dictionary is None:

        return default

    return dictionary.get(
        key,
        default
    )


# =========================
# Normalize Formula
# =========================

def normalize_formula(formula):

    return formula.replace(
        " ",
        ""
    )