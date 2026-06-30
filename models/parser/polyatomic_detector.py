import json

from config import ELEMENTS_PATH


# =========================
# Load Database
# =========================

POLYATOMIC_PATH = (
    ELEMENTS_PATH.parent /
    "polyatomic_ions.json"
)

with open(

    POLYATOMIC_PATH,

    "r",

    encoding="utf-8"

) as file:

    POLYATOMIC_IONS = json.load(file)


# =========================
# Detect Polyatomic Ions
# =========================

def detect_polyatomic_ions(formula):

    """
    Detect polyatomic ions inside
    a chemical formula.

    Returns
    -------
    list
    """

    clean_formula = (

        formula

        .replace("(", "")

        .replace(")", "")

    )

    detected = []

    for ion in POLYATOMIC_IONS:

        if ion["formula"] not in clean_formula:

            continue

        count = 1

        import re

        match = re.search(

            rf"{ion['formula']}(\d*)",

            clean_formula

        )

        if match:

            number = match.group(1)

            if number:

                count = int(number)

        detected.append({

            "name": ion["name"],

            "formula": ion["formula"],

            "charge": ion["charge"],

            "count": count,

            "category": ion["category"],

            "ion_type": ion["ion_type"]

        })

    return detected


# =========================
# Test
# =========================

if __name__ == "__main__":

    while True:

        formula = input(

            "\nFormula: "

        )

        if formula == "exit":

            break

        print(

            detect_polyatomic_ions(

                formula

            )

        )