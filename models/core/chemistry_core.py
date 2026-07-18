from models.parser.validator import detect_input_type

from models.reaction.reaction_validator import is_reaction
from models.reaction.reaction_engine import solve_reaction

from models.compound.compound_engine import create_compound

from models.core.database_manager import find_compound
from models.core.element_manager import get_element


# ==========================================================
# Element Handler
# ==========================================================

def handle_element(query: str) -> dict:

    element = get_element(query)

    if element is None:

        return {
            "success": False,
            "message": "Element not found"
        }

    return {
        "success": True,
        "type": "element",
        "data": element
    }


# ==========================================================
# Compound Handler
# ==========================================================

def handle_compound(query: str) -> dict:

    compound = find_compound(query)

    if compound is None:

        try:

            compound = create_compound(query)

        except Exception as error:

            return {
                "success": False,
                "message": str(error)
            }

    return {
        "success": True,
        "type": "compound",
        "data": compound
    }


# ==========================================================
# Reaction Handler
# ==========================================================

def handle_reaction(query: str) -> dict:

    return {
        "success": True,
        "type": "reaction",
        "data": solve_reaction(query)
    }


# ==========================================================
# Analyze
# ==========================================================

def analyze(query: str) -> dict:
    """
    Analyze any chemistry input.

    Parameters
    ----------
    query : str

    Returns
    -------
    dict
    """

    query = query.strip()

    if not query:

        return {
            "success": False,
            "message": "Empty input"
        }

    # ------------------------------------------------------
    # Chemical Reaction
    # ------------------------------------------------------

    if is_reaction(query):

        return handle_reaction(query)

    # ------------------------------------------------------
    # Detect Input Type
    # ------------------------------------------------------

    input_type = detect_input_type(query)

    # ------------------------------------------------------
    # Element
    # ------------------------------------------------------

    if input_type == "element":

        return handle_element(query)

    # ------------------------------------------------------
    # Compound
    # ------------------------------------------------------

    if input_type == "compound":

        return handle_compound(query)

    # ------------------------------------------------------
    # Unknown
    # ------------------------------------------------------

    return {
        "success": False,
        "message": "Unknown chemistry input"
    }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    while True:

        query = input("\nSearch (exit): ").strip()

        if query.lower() == "exit":
            break

        print(analyze(query))