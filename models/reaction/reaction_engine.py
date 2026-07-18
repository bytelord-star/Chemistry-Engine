from models.parser.formula_parser import parse_formula

from models.reaction.reaction_matrix import balance_matrix
from models.reaction.reaction_validator import analyze_reaction_input


# ==========================================================
# Count atoms on one side
# ==========================================================

def count_atoms(compounds: list[str]) -> dict:
    """
    Count atoms in one side of a reaction.
    """

    total = {}

    for formula in compounds:

        parsed = parse_formula(formula)

        atoms = parsed["atoms"]

        for element, count in atoms.items():

            total[element] = (
                total.get(element, 0)
                + count
            )

    return total


# ==========================================================
# Solve Reaction
# ==========================================================

def solve_reaction(reaction: str) -> dict:
    """
    Analyze a chemical reaction.
    """

    data = analyze_reaction_input(reaction)

    if not data["valid"]:

        return {

            "valid": False,

            "message": "Invalid reaction"

        }

    reactants = data["reactants"]

    products = data["products"]

    reactant_atoms = count_atoms(reactants)

    product_atoms = count_atoms(products)

    balanced = (
        reactant_atoms == product_atoms
    )

    result = {

        "valid": True,

        "balanced": balanced,

        "reactants_atoms": reactant_atoms,

        "products_atoms": product_atoms

    }

    if not balanced:

        result["suggestion"] = balance_matrix(
            reaction
        )

    return result


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
            solve_reaction(reaction)
        )