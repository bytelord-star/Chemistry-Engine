import json
from pathlib import Path
from typing import Any


# ==========================================================
# JSON Utilities
# ==========================================================

def load_json(path: Path, default: Any = None) -> Any:
    """
    Load a JSON file safely.

    Parameters
    ----------
    path : Path
        JSON file path.

    default : Any
        Value returned if loading fails.

    Returns
    -------
    Any
    """

    path = Path(path)

    if default is None:
        default = {}

    if not path.exists():
        return default

    if path.stat().st_size == 0:
        return default

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:

        return default


def save_json(path: Path, data: Any) -> None:
    """
    Save data as JSON.
    """

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
            ensure_ascii=False,
            sort_keys=False
        )


# ==========================================================
# Formula Utilities
# ==========================================================

def normalize_formula(formula: str) -> str:
    """
    Remove spaces around a chemical formula.
    """

    return formula.strip().replace(" ", "")