from models.core.acid_manager import find_acid
from models.core.base_manager import find_base
from models.core.element_manager import is_metal


# ==========================================================
# Compound Classification
# ==========================================================

def classify_compound(parsed):
    """
    Classify a parsed chemical compound.

    Parameters
    ----------
    parsed : dict
        Output of parse_formula()

    Returns
    -------
    dict
    """

    atoms = parsed["atoms"]

    polyatomic = parsed["polyatomic_ions"]

    symbols = list(atoms.keys())

    has_metal = any(

        is_metal(symbol)

        for symbol in symbols

    )

    has_hydrogen = "H" in atoms

    has_oxygen = "O" in atoms

    has_polyatomic = bool(polyatomic)

    # ======================================================
    # Metallic Element
    # ======================================================

    if len(symbols) == 1 and has_metal:

        return {

            "type": "Metal",

            "family": "Element",

            "subcategory": "Metallic",

            "contains_metal": True,

            "contains_polyatomic": False,

            "contains_hydrogen": False,

            "contains_oxygen": False

        }

    # ======================================================
    # Acid
    # ======================================================

    acid = find_acid(parsed["formula"])

    if acid:

        return {

            "type": "Acid",

            "family": "Inorganic",

            "subcategory": acid["acid_type"],

            "contains_metal": False,

            "contains_polyatomic": has_polyatomic,

            "contains_hydrogen": True,

            "contains_oxygen": has_oxygen

        }

    # ======================================================
    # Base
    # ======================================================

    base = find_base(parsed["formula"])

    if base:

        return {

            "type": "Base",

            "family": "Inorganic",

            "subcategory": "Hydroxide",

            "contains_metal": True,

            "contains_polyatomic": has_polyatomic,

            "contains_hydrogen": has_hydrogen,

            "contains_oxygen": has_oxygen

        }
    # ======================================================
    # Oxides
    # ======================================================

    if has_oxygen and len(symbols) == 2 and not has_hydrogen:

        subtype = (

            "Metal Oxide"

            if has_metal

            else

            "Nonmetal Oxide"

        )

        return {

            "type": "Oxide",

            "family": "Inorganic",

            "subcategory": subtype,

            "contains_metal": has_metal,

            "contains_polyatomic": False,

            "contains_hydrogen": False,

            "contains_oxygen": True

        }

    # ======================================================
    # Polyatomic Salt
    # ======================================================

    if has_metal and has_polyatomic:

        return {

            "type": "Salt",

            "family": "Ionic Compound",

            "subcategory": "Polyatomic Salt",

            "contains_metal": True,

            "contains_polyatomic": True,

            "contains_hydrogen": has_hydrogen,

            "contains_oxygen": has_oxygen

        }

    # ======================================================
    # Binary Salt
    # ======================================================

    if has_metal and len(symbols) == 2:

        return {

            "type": "Salt",

            "family": "Ionic Compound",

            "subcategory": "Binary Salt",

            "contains_metal": True,

            "contains_polyatomic": False,

            "contains_hydrogen": has_hydrogen,

            "contains_oxygen": has_oxygen

        }


    # ======================================================
    # Molecular Compound
    # ======================================================

    if not has_metal:

        return {

            "type": "Molecular Compound",

            "family": "Covalent Compound",

            "subcategory": "Nonmetal Compound",

            "contains_metal": False,

            "contains_polyatomic": has_polyatomic,

            "contains_hydrogen": has_hydrogen,

            "contains_oxygen": has_oxygen

        }

    # ======================================================
    # Unknown
    # ======================================================

    return {

        "type": "Unknown",

        "family": "Unknown",

        "subcategory": "Unknown",

        "contains_metal": has_metal,

        "contains_polyatomic": has_polyatomic,

        "contains_hydrogen": has_hydrogen,

        "contains_oxygen": has_oxygen

    }