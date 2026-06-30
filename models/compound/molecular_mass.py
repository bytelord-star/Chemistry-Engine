import json
import sys
from pathlib import Path

# ========= Project Root =========

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

from config import ELEMENTS_PATH
from models.parser.formula_parser import parse_formula


# ========= Load Elements =========

with open(
    ELEMENTS_PATH,
    "r",
    encoding="utf-8"
) as file:

    elements = json.load(file)


# ========= Find Element =========

def get_element(symbol):

    return next(

        (
            e for e in elements
            if e["symbol"].lower()
            ==
            symbol.lower()
        ),

        None

    )


# ========= Calculate Molar Mass =========

def calculate_molar_mass(atoms):

    total_mass = 0

    for symbol, count in atoms.items():

        element = get_element(symbol)

        if not element:
            raise ValueError(f"Element {symbol} not found.")

        total_mass += element["atomic_weight"] * count

    return round(total_mass, 4)


# ========= Main =========

def main():

    while True:

        print(
            "\n===== MOLAR MASS CALCULATOR ====="
        )

        formula = input(
            "Formula (exit): "
        ).strip()

        if formula.lower() == "exit":
            break

        try:

            mass = calculate_molar_mass(
                formula
            )

            print(
                f"\nMolar Mass = "
                f"{mass} g/mol"
            )

        except ValueError as error:

            print(
                f"\n❌ {error}"
            )


if __name__ == "__main__":
    main()