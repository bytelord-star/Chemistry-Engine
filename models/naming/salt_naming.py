from models.core.element_manager import get_element, is_metal
from models.compound.ion_manager import get_polyatomic_by_formula

from models.naming.naming_rules import (
    to_ide,
    format_name,
)


# ==========================================================
# Private Helpers
# ==========================================================

def _get_metal(parsed):
    """
    Return the metal element dictionary.
    """

    for symbol in parsed["atoms"]:

        if is_metal(symbol):

            return get_element(symbol)

    return None


def _get_nonmetal(parsed):
    """
    Return the non-metal element dictionary.
    """

    for symbol in parsed["atoms"]:

        if not is_metal(symbol):

            return get_element(symbol)

    return None


def _get_polyatomic(parsed):

    ions = parsed.get("polyatomic_ions", [])

    if not ions:
        return None

    return ions[0]

# ==========================================================
# Salt Naming
# ==========================================================

def generate_salt_name(parsed):
    """
    Generate an IUPAC name for salts.

    Supported:

    Binary salts
        NaCl
        KBr
        MgS

    Polyatomic salts
        Na2SO4
        CaCO3
        NH4NO3

    Oxidation states for transition metals
    will be added in Version 0.2.
    """

    metal = _get_metal(parsed)

    if metal is None:

        return {

            "name": "Unknown Salt",

            "iupac_name": "Unknown Salt",

            "common_name": None,

        }

    # ------------------------------------------------------
    # Polyatomic Salt
    # ------------------------------------------------------

    ion = _get_polyatomic(parsed)

    if ion is not None:

        final_name = format_name(

            f"{metal['name']} {ion['name']}"

        )

        return {

            "name": final_name,

            "iupac_name": final_name,

            "common_name": None,

        }

    # ------------------------------------------------------
    # Binary Salt
    # ------------------------------------------------------

    nonmetal = _get_nonmetal(parsed)

    if nonmetal is None:

        return {

            "name": "Unknown Salt",

            "iupac_name": "Unknown Salt",

            "common_name": None,

        }

    anion = to_ide(

        nonmetal["name"]

    )

    final_name = format_name(

        f"{metal['name']} {anion}"

    )

    return {

        "name": final_name,

        "iupac_name": final_name,

        "common_name": None,

    }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    from models.parser.formula_parser import parse_formula

    tests = [

        "NaCl",

        "KBr",

        "MgS",

        "Na2SO4",

        "CaCO3",

        "NH4NO3",

    ]

    for formula in tests:

        print(formula)

        print(

            generate_salt_name(

                parse_formula(formula)

            )

        )

        print("-" * 40)