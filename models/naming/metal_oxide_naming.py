from models.core.element_manager import (
    get_element,
    is_metal,
    get_oxidation_states,
)

from models.core.oxidation_number_engine import (
    calculate_metal_oxidation_state,
    oxidation_state_is_valid,
)

from models.naming.naming_rules import (
    format_name,
)


# ==========================================================
# Metal Oxide Naming
# ==========================================================

ROMAN_NUMERALS = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
}


def generate_metal_oxide_name(parsed):
    """
    Generate Stock IUPAC names for metal oxides.

    Examples
    --------
    Na2O   -> Sodium Oxide
    MgO    -> Magnesium Oxide
    FeO    -> Iron(II) Oxide
    Fe2O3  -> Iron(III) Oxide
    Cu2O   -> Copper(I) Oxide
    CuO    -> Copper(II) Oxide
    """

    atoms = parsed["atoms"]

    symbols = list(atoms.keys())

    if len(symbols) != 2:

        return {
            "name": "Unknown Oxide",
            "iupac_name": "Unknown Oxide",
            "common_name": None,
        }

    metal_symbol = None

    for symbol in symbols:

        if is_metal(symbol):
            metal_symbol = symbol
            break

    if metal_symbol is None:

        return {
            "name": "Unknown Oxide",
            "iupac_name": "Unknown Oxide",
            "common_name": None,
        }

    metal = get_element(metal_symbol)

    if metal is None:

        return {
            "name": "Unknown Oxide",
            "iupac_name": "Unknown Oxide",
            "common_name": None,
        }

    oxidation_states = get_oxidation_states(
        metal_symbol
    )

    # =====================================================
    # Fixed oxidation metals
    # =====================================================

    if len(oxidation_states) <= 1:

        final_name = format_name(
            f"{metal['name']} Oxide"
        )

        return {
            "name": final_name,
            "iupac_name": final_name,
            "common_name": None,
        }

    # =====================================================
    # Variable oxidation metals
    # =====================================================

    oxidation = calculate_metal_oxidation_state(parsed)

    if not oxidation_state_is_valid(
        metal_symbol,
        oxidation,
    ):
        oxidation = oxidation_states[0]

    roman = ROMAN_NUMERALS.get(
        oxidation,
        str(oxidation),
    )

    final_name = format_name(
        f"{metal['name']}({roman}) Oxide"
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
        "Na2O",
        "MgO",
        "FeO",
        "Fe2O3",
        "Cu2O",
        "CuO",
    ]

    for formula in tests:

        print(formula)

        print(
            generate_metal_oxide_name(
                parse_formula(formula)
            )
        )

        print("-" * 40)