from models.parser.element_validator import validate_elements
from models.parser.formula_validator import is_valid_formula


# ==========================================================
# Constants
# ==========================================================

REACTION_SEPARATORS = (
    "=",
    "->",
)


# ==========================================================
# Detect Reaction
# ==========================================================

def is_reaction(text: str) -> bool:
    """
    Check whether the input looks
    like a chemical reaction.
    """

    text = text.strip()

    return any(
        separator in text
        for separator in REACTION_SEPARATORS
    )


# ==========================================================
# Split Reaction
# ==========================================================

def split_reaction(reaction: str):
    """
    Split reaction into reactants
    and products.
    """

    for separator in REACTION_SEPARATORS:

        if separator in reaction:

            left, right = reaction.split(
                separator,
                1
            )

            reactants = [

                item.strip()

                for item in left.split("+")

                if item.strip()

            ]

            products = [

                item.strip()

                for item in right.split("+")

                if item.strip()

            ]

            return reactants, products

    return None, None


# ==========================================================
# Validate Reaction
# ==========================================================

def validate_reaction(reaction: str):
    """
    Validate reaction syntax.
    """

    if not is_reaction(reaction):

        return False, None, None

    reactants, products = split_reaction(reaction)

    if not reactants or not products:

        return False, None, None

    for formula in reactants + products:

        if not is_valid_formula(formula):

            return False, None, None

        if not validate_elements(formula):

            return False, None, None

    return True, reactants, products


# ==========================================================
# Analyze Reaction
# ==========================================================

def analyze_reaction_input(reaction: str):
    """
    Validate and parse reaction.
    """

    valid, reactants, products = validate_reaction(
        reaction
    )

    if not valid:

        return {

            "valid": False,

            "message": "Invalid reaction"

        }

    return {

        "valid": True,

        "reactants": reactants,

        "products": products

    }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    while True:

        reaction = input(
            "Reaction (exit): "
        ).strip()

        if reaction.lower() == "exit":

            break

        print(
            analyze_reaction_input(reaction)
        )