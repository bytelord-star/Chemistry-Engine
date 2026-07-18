import numpy as np

from fractions import Fraction
from math import gcd

from models.parser.formula_parser import parse_formula
from models.reaction.reaction_validator import (
    analyze_reaction_input
)


# ==========================================================
# Collect Elements
# ==========================================================

def collect_elements(compounds):
    """
    Collect all unique elements
    appearing in compounds.
    """

    elements = []

    for compound in compounds:

        parsed = parse_formula(compound)

        atoms = parsed["atoms"]

        for element in atoms:

            if element not in elements:

                elements.append(element)

    return elements


# ==========================================================
# Build Stoichiometric Matrix
# ==========================================================

def build_matrix(reactants, products):
    """
    Build stoichiometric matrix.
    """

    compounds = reactants + products

    elements = collect_elements(compounds)

    parsed_compounds = [
        parse_formula(compound)["atoms"]
        for compound in compounds
    ]

    matrix = []

    for element in elements:

        row = []

        for i, atoms in enumerate(parsed_compounds):

            value = atoms.get(element, 0)

            if i < len(reactants):

                row.append(value)

            else:

                row.append(-value)

        matrix.append(row)

    return matrix


# ==========================================================
# Balance Reaction
# ==========================================================

def balance_matrix(reaction):
    """
    Balance a chemical reaction
    using matrix null-space.
    """

    data = analyze_reaction_input(reaction)

    if not data["valid"]:

        return None

    reactants = data["reactants"]

    products = data["products"]

    matrix = np.array(

        build_matrix(
            reactants,
            products
        ),

        dtype=float

    )

    # ------------------------------------------------------
    # Null Space
    # ------------------------------------------------------

    _, _, vh = np.linalg.svd(matrix)

    vector = vh[-1]

    vector = [

        Fraction(float(value)).limit_denominator(100)

        for value in vector

    ]

    # ------------------------------------------------------
    # Convert Fractions → Integers
    # ------------------------------------------------------

    lcm = 1

    for fraction in vector:

        lcm = lcm * fraction.denominator // gcd(
            lcm,
            fraction.denominator
        )

    coefficients = [

        int(value * lcm)

        for value in vector

    ]

    # ------------------------------------------------------
    # Simplify
    # ------------------------------------------------------

    divisor = abs(coefficients[0])

    for coefficient in coefficients:

        divisor = gcd(

            divisor,

            abs(coefficient)

        )

    coefficients = [

        coefficient // divisor

        for coefficient in coefficients

    ]

    # ------------------------------------------------------
    # Make Positive
    # ------------------------------------------------------

    if any(c < 0 for c in coefficients):

        if coefficients[0] < 0:

            coefficients = [

                -c

                for c in coefficients

            ]

    # ------------------------------------------------------
    # Build Equation
    # ------------------------------------------------------

    left = []

    right = []

    for index, coefficient in enumerate(coefficients):

        coefficient_text = (

            ""

            if coefficient == 1

            else str(coefficient)

        )

        if index < len(reactants):

            left.append(

                f"{coefficient_text}{reactants[index]}"

            )

        else:

            right.append(

                f"{coefficient_text}{products[index-len(reactants)]}"

            )

    return (

        " + ".join(left)

        + " = "

        + " + ".join(right)

    )


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

            balance_matrix(reaction)

        )