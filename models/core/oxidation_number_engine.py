from models.core.element_manager import (
    get_oxidation_states,
)


# ==========================================================
# Known Oxidation Numbers
# ==========================================================

FIXED_OXIDATION = {

    "O": -2,

    "F": -1,

    "H": 1,

}


# ==========================================================
# Metal Oxidation Number
# ==========================================================

def calculate_metal_oxidation_state(parsed):
    """
    Calculate oxidation state of the metal
    in a binary metal oxide.

    Examples
    --------
    FeO    -> 2
    Fe2O3  -> 3
    Cu2O   -> 1
    CuO    -> 2
    SnO2   -> 4
    """

    atoms = parsed["atoms"]

    metal_symbol = None
    metal_count = 0

    oxygen_count = atoms.get("O", 0)

    # ---------------------------------------------
    # Find metal
    # ---------------------------------------------

    for symbol, count in atoms.items():

        if symbol == "O":

            continue

        states = get_oxidation_states(symbol)

        if not states:

            continue

        metal_symbol = symbol
        metal_count = count
        break

    if metal_symbol is None:

        return None

    oxygen_total = oxygen_count * FIXED_OXIDATION["O"]

    oxidation = -oxygen_total / metal_count

    if oxidation.is_integer():

        return int(oxidation)

    return oxidation


# ==========================================================
# Validation
# ==========================================================

def oxidation_state_is_valid(
    symbol,
    oxidation,
):
    """
    Check whether the calculated oxidation state
    exists in elements.json.
    """

    states = get_oxidation_states(symbol)

    return oxidation in states


# ==========================================================
# Roman Numerals
# ==========================================================

ROMAN = {

    1: "I",

    2: "II",

    3: "III",

    4: "IV",

    5: "V",

    6: "VI",

    7: "VII",

    8: "VIII",

}


def oxidation_to_roman(
    oxidation,
):

    return ROMAN.get(

        oxidation,

        str(oxidation),

    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    from models.parser.formula_parser import parse_formula

    tests = [

        "Na2O",

        "MgO",

        "FeO",

        "Fe2O3",

        "Cu2O",

        "CuO",

        "SnO",

        "SnO2",

    ]

    for formula in tests:

        parsed = parse_formula(formula)

        oxidation = calculate_metal_oxidation_state(parsed)

        print(

            formula,

            "->",

            oxidation,

            oxidation_to_roman(oxidation)

            if oxidation is not None

            else None,

        )