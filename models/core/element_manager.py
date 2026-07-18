from config import ELEMENTS_PATH

from models.core.utils import load_json


# ==========================================================
# Database
# ==========================================================

ELEMENTS = load_json(
    ELEMENTS_PATH,
    default=[]
)

ELEMENT_INDEX = {

    element["symbol"]: element

    for element in ELEMENTS

}


# ==========================================================
# Metal Categories
# ==========================================================

METAL_CATEGORIES = {

    "alkali_metal",

    "alkaline_earth_metal",

    "transition_metal",

    "post_transition_metal",

    "lanthanide",

    "actinide",

}


# ==========================================================
# Core
# ==========================================================

def get_element(
    symbol: str,
):

    if not symbol:

        return None

    return ELEMENT_INDEX.get(

        symbol.strip().capitalize()

    )


# ==========================================================
# Internal Helper
# ==========================================================

def _get_field(
    symbol: str,
    field: str,
):

    element = get_element(symbol)

    if element is None:

        return None

    return element.get(field)


# ==========================================================
# Public Helper
# ==========================================================

def get_field(
    symbol: str,
    field: str,
):

    return _get_field(

        symbol,

        field,

    )


# ==========================================================
# Validation
# ==========================================================

def element_exists(
    symbol: str,
) -> bool:

    return get_element(symbol) is not None


def elements_exist(
    symbols,
) -> bool:

    if isinstance(

        symbols,

        str,

    ):

        symbols = [symbols]

    return all(

        element_exists(symbol)

        for symbol in symbols

    )


# ==========================================================
# Basic Properties
# ==========================================================

def get_element_name(
    symbol: str,
):

    return _get_field(

        symbol,

        "name",

    )


def get_atomic_mass(
    symbol: str,
):

    return _get_field(

        symbol,

        "atomic_weight",

    )


def get_category(
    symbol: str,
):

    return _get_field(

        symbol,

        "category",

    )


def get_group(
    symbol: str,
):

    return _get_field(

        symbol,

        "group",

    )


def get_period(
    symbol: str,
):

    return _get_field(

        symbol,

        "period",

    )


def get_electronegativity(
    symbol: str,
):

    return _get_field(

        symbol,

        "electronegativity",

    )


# ==========================================================
# Classification
# ==========================================================

def is_metal(
    symbol: str,
) -> bool:

    return (

        get_category(symbol)

        in

        METAL_CATEGORIES

    )


def is_nonmetal(
    symbol: str,
) -> bool:

    category = get_category(symbol)

    return (

        category is not None

        and

        category not in METAL_CATEGORIES

    )

# ==========================================================
# Oxidation States
# ==========================================================

def get_oxidation_states(symbol: str):
    """
    Return all possible oxidation states
    of an element.

    Examples
    --------
    Fe -> [2, 3]
    Na -> [1]
    O  -> [-2]
    """

    element = get_element(symbol)

    if element is None:

        return []

    return element.get(
        "oxidation_states",
        [],
    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print(get_element("Na"))

    print(get_element_name("Na"))

    print(get_atomic_mass("Na"))

    print(get_electronegativity("Na"))

    print(get_category("Na"))

    print(get_group("Na"))

    print(get_period("Na"))

    print(get_field("Na", "melting_point"))

    print(get_field("Na", "boiling_point"))

    print(is_metal("Na"))

    print(is_nonmetal("O"))

    print(elements_exist(["Na", "Cl", "O"]))