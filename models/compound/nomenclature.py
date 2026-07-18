"""
Chemical Nomenclature Engine

This module is responsible for generating systematic names
for chemical compounds.
"""


# ==========================================================
# Public API
# ==========================================================

def generate_name(parsed, classification):
    """
    Generate the chemical name.

    Parameters
    ----------
    parsed : dict

    classification : dict

    Returns
    -------
    str
    """

    compound_type = classification["type"]

    generators = {

        "Acid": generate_acid_name,

        "Base": generate_base_name,

        "Salt": generate_salt_name,

        "Oxide": generate_oxide_name,

        "Molecular Compound": generate_molecular_name,

    }

    generator = generators.get(compound_type)

    if generator is None:

        return "Unknown"

    return generator(parsed)


# ==========================================================
# Acid
# ==========================================================

def generate_acid_name(parsed):
    """
    TODO:
    Implement acid nomenclature.
    """
    raise NotImplementedError(
        "Acid nomenclature has not been implemented yet."
    )


# ==========================================================
# Base
# ==========================================================

def generate_base_name(parsed):
    """
    TODO:
    Implement base nomenclature.
    """
    raise NotImplementedError(
        "Base nomenclature has not been implemented yet."
    )


# ==========================================================
# Salt
# ==========================================================

def generate_salt_name(parsed):
    """
    TODO:
    Implement salt nomenclature.
    """
    raise NotImplementedError(
        "Salt nomenclature has not been implemented yet."
    )


# ==========================================================
# Oxide
# ==========================================================

def generate_oxide_name(parsed):
    """
    TODO:
    Implement oxide nomenclature.
    """
    raise NotImplementedError(
        "Oxide nomenclature has not been implemented yet."
    )


# ==========================================================
# Molecular Compound
# ==========================================================

def generate_molecular_name(parsed):
    """
    TODO:
    Implement molecular compound nomenclature.
    """
    raise NotImplementedError(
        "Molecular nomenclature has not been implemented yet."
    )