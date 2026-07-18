# ==========================================================
# Symmetric Nonpolar Molecules
# ==========================================================

NONPOLAR_EXCEPTIONS = {

    "CO2",
    "CH4",
    "BF3",
    "BeCl2",
    "CCl4",
    "CF4",
    "SiCl4",
    "SF6",
    "PF5",
    "SO3",
    "XeF2",
    "XeF4"

}


# ==========================================================
# Molecular Polarity
# ==========================================================

def predict_polarity(
    bond_type,
    formula
):
    """
    Predict molecular polarity.

    Parameters
    ----------
    bond_type : str

    formula : str

    Returns
    -------
    str
    """

    formula = formula.replace(" ", "")

    # ------------------------------------------------------

    if bond_type == "Metallic":

        return "Metallic"

    # ------------------------------------------------------

    if bond_type == "Ionic":

        return "Ionic Compound"

    # ------------------------------------------------------

    if bond_type == "Nonpolar Covalent":

        return "Nonpolar"

    # ------------------------------------------------------

    if bond_type == "Polar Covalent":

        if formula in NONPOLAR_EXCEPTIONS:

            return "Nonpolar"

        return "Polar"

    # ------------------------------------------------------

    if bond_type == "Covalent":

        if formula in NONPOLAR_EXCEPTIONS:

            return "Nonpolar"

        return "Unknown"

    # ------------------------------------------------------

    return "Unknown"