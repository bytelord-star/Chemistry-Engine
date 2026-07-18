from models.core.element_manager import is_metal
from models.core.polyatomic_manager import get_polyatomic_by_formula


# ==========================================================
# Helpers
# ==========================================================

def _symbols(parsed):

    return list(parsed["atoms"].keys())


# ==========================================================
# Cation
# ==========================================================

def get_cation(parsed):
    """
    Return cation information.

    Returns
    -------
    dict | None
    """

    for symbol in _symbols(parsed):

        if is_metal(symbol):

            return {

                "symbol": symbol,

                "count": parsed["atoms"][symbol],

            }

    polyatomic = parsed["polyatomic_ions"]

    for ion in polyatomic:

        data = get_polyatomic_by_formula(ion)

        if data and data["ion_type"] == "cation":

            return data

    return None


# ==========================================================
# Anion
# ==========================================================

def get_anion(parsed):
    """
    Return anion information.

    Returns
    -------
    dict | None
    """

    polyatomic = parsed["polyatomic_ions"]

    for ion in polyatomic:

        data = get_polyatomic_by_formula(ion)

        if data and data["ion_type"] == "anion":

            return data

    for symbol in _symbols(parsed):

        if symbol == "O":

            continue

        if not is_metal(symbol):

            return {

                "symbol": symbol,

                "count": parsed["atoms"][symbol],

            }

    if "O" in parsed["atoms"]:

        return {

            "symbol": "O",

            "count": parsed["atoms"]["O"],

        }

    return None


# ==========================================================
# Classification
# ==========================================================

def is_binary_salt(parsed):

    return (

        len(parsed["polyatomic_ions"]) == 0

    )


def is_polyatomic_salt(parsed):

    return (

        len(parsed["polyatomic_ions"]) > 0

    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    from models.parser.formula_parser import parse_formula

    tests = [

        "NaCl",

        "Na2SO4",

        "CaCO3",

        "NH4Cl",

    ]

    for formula in tests:

        parsed = parse_formula(formula)

        print()

        print(formula)

        print(get_cation(parsed))

        print(get_anion(parsed))