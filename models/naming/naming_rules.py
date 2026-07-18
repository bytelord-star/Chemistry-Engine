"""
Naming rules used by the Chemistry Engine.

This module contains reusable IUPAC naming rules shared by
molecular, oxide, salt and future naming engines.
"""

# ==========================================================
# Element Endings
# ==========================================================

ELEMENT_ENDINGS = {

    "oxygen": "oxide",
    "fluorine": "fluoride",
    "chlorine": "chloride",
    "bromine": "bromide",
    "iodine": "iodide",
    "sulfur": "sulfide",
    "selenium": "selenide",
    "tellurium": "telluride",
    "nitrogen": "nitride",
    "phosphorus": "phosphide",
    "arsenic": "arsenide",
    "carbon": "carbide",
    "silicon": "silicide",
    "boron": "boride",
    "hydrogen": "hydride",

}

# ==========================================================
# Special Prefix Combinations
# ==========================================================

SPECIAL_COMBINATIONS = {

    ("mono", "oxide"): "monoxide",
    ("di", "oxide"): "dioxide",
    ("tri", "oxide"): "trioxide",
    ("tetra", "oxide"): "tetroxide",
    ("penta", "oxide"): "pentoxide",
    ("hexa", "oxide"): "hexoxide",
    ("hepta", "oxide"): "heptoxide",
    ("octa", "oxide"): "octoxide",
    ("nona", "oxide"): "nonoxide",
    ("deca", "oxide"): "decoxide",

}

# ==========================================================
# Convert Element Name to -ide
# ==========================================================

def to_ide(element_name: str) -> str:

    """
    Convert an element name into its '-ide' form.

    Examples
    --------
    oxygen -> oxide
    chlorine -> chloride
    sulfur -> sulfide
    """

    if not element_name:

        return ""

    return ELEMENT_ENDINGS.get(

        element_name.lower(),

        element_name.lower()

    )


# ==========================================================
# Combine Prefix
# ==========================================================

def combine_prefix(
    prefix: str,
    word: str,
) -> str:

    """
    Combine a Greek prefix with an element ending.

    Handles official IUPAC spelling.

    Examples
    --------
    mono + oxide
    -> monoxide

    di + oxide
    -> dioxide

    tri + oxide
    -> trioxide

    tetra + oxide
    -> tetroxide

    penta + oxide
    -> pentoxide
    """

    prefix = prefix.lower().strip()

    word = word.lower().strip()

    if not prefix:

        return word

    special = SPECIAL_COMBINATIONS.get(

        (prefix, word)

    )

    if special:

        return special

    return prefix + word


# ==========================================================
# Show Mono?
# ==========================================================

def show_mono(
    is_first_element: bool,
) -> bool:

    """
    Determines whether 'mono' should appear.

    First element:
        mono omitted

    Second element:
        mono shown
    """

    return not is_first_element


# ==========================================================
# Format Name
# ==========================================================

def format_name(name: str) -> str:
    """
    Format chemical names while preserving
    oxidation-state Roman numerals.

    Examples
    --------
    carbon dioxide
        -> Carbon Dioxide

    iron(ii) oxide
        -> Iron(II) Oxide

    copper(iv) sulfate
        -> Copper(IV) Sulfate
    """

    words = []

    for word in name.split():

        if "(" in word and ")" in word:

            left = word[:word.index("(")]

            middle = word[word.index("(") + 1:word.index(")")]

            right = word[word.index(")"):]

            words.append(

                left.capitalize()

                + "("

                + middle.upper()

                + right

            )

        else:

            words.append(

                word.capitalize()

            )

    return " ".join(words)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    tests = [

        ("mono", "oxide"),
        ("di", "oxide"),
        ("tri", "oxide"),
        ("tetra", "oxide"),
        ("penta", "oxide"),
        ("hexa", "oxide"),
        ("hepta", "oxide"),
        ("octa", "oxide"),
        ("nona", "oxide"),
        ("deca", "oxide"),

    ]

    for prefix, word in tests:

        print(

            combine_prefix(

                prefix,

                word,

            )

        )