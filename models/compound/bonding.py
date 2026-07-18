from models.core.element_manager import (
    is_metal,
    get_electronegativity
)


# ==========================================================
# Bond Type
# ==========================================================

def calculate_bond_type(parsed):
    """
    Determine the primary bond type of a compound.

    Parameters
    ----------
    parsed : dict
        Output of parse_formula()

    Returns
    -------
    str
    """

    atoms = parsed["atoms"]

    polyatomic = parsed["polyatomic_ions"]

    symbols = list(atoms.keys())

    # ======================================================
    # Single Element
    # ======================================================

    if len(symbols) == 1:

        if is_metal(symbols[0]):
            return "Metallic"

        return "Covalent"

    # ======================================================
    # Ionic Compound (Metal + Polyatomic Ion)
    # ======================================================

    if polyatomic and any(
        is_metal(symbol)
        for symbol in symbols
    ):

        return "Ionic"

    # ======================================================
    # Ionic Compound (Metal + Nonmetal)
    # ======================================================

    metals = [
        symbol
        for symbol in symbols
        if is_metal(symbol)
    ]

    nonmetals = [
        symbol
        for symbol in symbols
        if not is_metal(symbol)
    ]

    if metals and nonmetals:
        return "Ionic"

    # ======================================================
    # Binary Covalent Compound
    # ======================================================

    if len(symbols) == 2:

        en1 = get_electronegativity(symbols[0])

        en2 = get_electronegativity(symbols[1])

        if en1 is not None and en2 is not None:

            difference = abs(en1 - en2)

            if difference < 0.4:
                return "Nonpolar Covalent"

            elif difference < 1.7:
                return "Polar Covalent"

            else:
                return "Ionic"

    # ======================================================
    # Multi-element Covalent Compound
    # ======================================================

    electronegativities = []

    for symbol in symbols:

        en = get_electronegativity(symbol)

        if en is not None:

            electronegativities.append(en)

    if len(electronegativities) >= 2:

        difference = (
            max(electronegativities)
            -
            min(electronegativities)
        )

        if difference < 0.4:
            return "Nonpolar Covalent"

        elif difference < 1.7:
            return "Polar Covalent"

    # ======================================================
    # Default
    # ======================================================

    return "Covalent"