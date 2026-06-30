# models/reaction_matrix.py


import numpy as np

from math import gcd

from fractions import Fraction

from models.reaction.reaction_validator import (
    analyze_reaction_input
)

from models.parser.formula_parser import (
    parse_formula
)



# =========================
# Get elements
# =========================

def get_all_elements(compounds):


    elements = []


    for compound in compounds:


        atoms = parse_formula(
            compound
        )


        for e in atoms:

            if e not in elements:

                elements.append(e)



    return elements





# =========================
# Build Matrix
# =========================

def build_matrix(reactants, products):


    all_compounds = (

        reactants
        +
        products

    )


    elements = get_all_elements(
        all_compounds
    )



    matrix = []



    for element in elements:


        row = []



        for compound in reactants:


            atoms = parse_formula(
                compound
            )


            row.append(
                atoms.get(element,0)
            )



        for compound in products:


            atoms = parse_formula(
                compound
            )


            row.append(
                -atoms.get(element,0)
            )



        matrix.append(row)



    return matrix





# =========================
# Balance
# =========================

def balance_matrix(reaction):


    data = analyze_reaction_input(
        reaction
    )



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



    # Null space

    u,s,v = np.linalg.svd(
        matrix
    )



    vector = v[-1]



    # Convert to integer

    vector = [

        Fraction(float(x)).limit_denominator(100)

        for x in vector

    ]


    
    denominators = [
        x.denominator
        for x in vector
    ]



    


# =========================
# Convert fractions to integers
# =========================

    denominators = [

        x.denominator

        for x in vector

    ]


    lcm = 1


    for d in denominators:

        lcm = lcm * d // gcd(lcm, d)



    coefficients = [

        int(x * lcm)

        for x in vector

    ]



# =========================
# Simplify coefficients
# =========================

    g = abs(coefficients[0])


    for c in coefficients:

        g = gcd(
            g,
            abs(c)
    )



    coefficients = [

        c // g

        for c in coefficients

    ]



# =========================
# Make positive
# =========================

    if min(coefficients) < 0:


        coefficients = [

            -x

            for x in coefficients

    ]


        coefficients = [

            -x

            for x in coefficients

        ]



    left = []


    right = []



    for i,c in enumerate(coefficients):


        if i < len(reactants):

            left.append(

                f"{c}{reactants[i]}"

            )

        else:

            right.append(

                f"{c}{products[i-len(reactants)]}"

            )



    return (

        " + ".join(left)

        +

        " = "

        +

        " + ".join(right)

    )





# =========================
# Test
# =========================

if __name__== "__main__":


    while True:


        r=input(
            "Reaction: "
        )


        if r=="exit":

            break



        print(

            balance_matrix(r)

        )