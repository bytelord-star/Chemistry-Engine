import json

from models.core.acid_manager import find_acid

from config import ELEMENTS_PATH


# =========================
# Load Elements
# =========================

with open(
    ELEMENTS_PATH,
    "r",
    encoding="utf-8"
) as file:

    ELEMENTS = json.load(file)


# =========================
# Helpers
# =========================

def get_element(symbol):

    for element in ELEMENTS:

        if element["symbol"] == symbol:

            return element

    return None


def is_metal(symbol):

    element = get_element(symbol)

    if not element:

        return False

    return element["category"] in [

        "alkali_metal",

        "alkaline_earth_metal",

        "transition_metal",

        "post_transition_metal",

        "lanthanide",

        "actinide"

    ]


# =========================
# Classification
# =========================

def classify_compound(parsed):

    atoms = parsed["atoms"]

    polyatomic = parsed["polyatomic_ions"]

    symbols = list(atoms.keys())

    has_metal = any(

        is_metal(symbol)

        for symbol in symbols

    )

    has_hydrogen = "H" in atoms

    has_oxygen = "O" in atoms

    has_polyatomic = len(polyatomic) > 0

    # -------------------------
    # Metallic Element
    # -------------------------

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

    # -------------------------
    # Base
    # -------------------------

    if any(

        ion["formula"] == "OH"

        for ion in polyatomic

    ) and has_metal:

        return {

            "type": "Base",

            "family": "Inorganic",

            "subcategory": "Hydroxide",

            "contains_metal": True,

            "contains_polyatomic": True,

            "contains_hydrogen": True,

            "contains_oxygen": True

        }

    # -------------------------
    # Acid
    # -------------------------

    acid = find_acid(parsed["formula"])

    if acid:

        return {

            "type": "Acid",

            "family": acid.get("family", "Inorganic"),

            "subcategory": acid.get("subcategory", "Acid"),

            "contains_metal": False,

            "contains_polyatomic": has_polyatomic,

            "contains_hydrogen": True,

            "contains_oxygen": has_oxygen

        }
    # -------------------------
    # Polyatomic Salt
    # -------------------------

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

    # -------------------------
    # Binary Salt
    # -------------------------

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

    # -------------------------
    # Oxides
    # -------------------------

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

            "contains_hydrogen": has_hydrogen,

            "contains_oxygen": True

        }
    # -------------------------
    # Molecular Compound
    # -------------------------

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

    # -------------------------
    # Unknown
    # -------------------------

    return {

        "type": "Unknown",

        "family": "Unknown",

        "subcategory": "Unknown",

        "contains_metal": has_metal,

        "contains_polyatomic": has_polyatomic,

        "contains_hydrogen": has_hydrogen,

        "contains_oxygen": has_oxygen

    }