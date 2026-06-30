import json

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


def electronegativity(symbol):

    element = get_element(symbol)

    if not element:

        return None

    return element.get("electronegativity")


# =========================
# Bond Type
# =========================

def calculate_bond_type(parsed):

    """
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

    elements = list(atoms.keys())


    # -----------------------------
    # Single Element
    # -----------------------------

    if len(elements) == 1:

        if is_metal(elements[0]):

            return "Metallic"

        return "Covalent"


    # -----------------------------
    # Polyatomic Ionic
    # -----------------------------

    if polyatomic:

        if any(

            is_metal(symbol)

            for symbol in elements

        ):

            return "Ionic"


    # -----------------------------
    # Ionic
    # -----------------------------

    metals = [

        e

        for e in elements

        if is_metal(e)

    ]

    nonmetals = [

        e

        for e in elements

        if not is_metal(e)

    ]

    if metals and nonmetals:

        return "Ionic"


    # -----------------------------
    # Binary Covalent
    # -----------------------------

    if len(elements) == 2:

        en1 = electronegativity(

            elements[0]

        )

        en2 = electronegativity(

            elements[1]

        )

        if (

            en1 is not None

            and

            en2 is not None

        ):

            diff = abs(

                en1 - en2

            )

            if diff < 0.4:

                return "Nonpolar Covalent"

            elif diff < 1.7:

                return "Polar Covalent"

            else:

                return "Ionic"


    # -----------------------------
    # Multi-element Covalent
    # -----------------------------

    return "Covalent"