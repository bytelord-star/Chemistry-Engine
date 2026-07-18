import re

from config import ELEMENTS_PATH
from models.core.utils import load_json


# ==========================================================
# Database
# ==========================================================

POLYATOMIC_PATH = (
    ELEMENTS_PATH.parent /
    "polyatomic_ions.json"
)

POLYATOMIC_IONS = load_json(
    POLYATOMIC_PATH,
    default=[]
)


# ==========================================================
# Detect Polyatomic Ions
# ==========================================================

def detect_polyatomic_ions(
    formula: str,
) -> list[dict]:
    """
    Detect polyatomic ions inside a
    validated chemical formula.
    """

    clean_formula = (
        formula
        .replace("(", "")
        .replace(")", "")
    )

    detected = []

    for ion in POLYATOMIC_IONS:

        pattern = rf"{re.escape(ion['formula'])}(\d*)"

        for match in re.finditer(
            pattern,
            clean_formula
        ):

            count = (
                int(match.group(1))
                if match.group(1)
                else 1
            )

            detected.append({

                "name": ion["name"],

                "formula": ion["formula"],

                "charge": ion["charge"],

                "count": count,

                "category": ion["category"],

                "ion_type": ion["ion_type"],

            })

    return detected