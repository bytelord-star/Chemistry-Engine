# models/reaction_engine.py


from models.reaction.reaction_validator import (
    analyze_reaction_input
)

from models.parser.formula_parser import (
    parse_formula
)

from models.reaction.reaction_matrix import (
    balance_matrix
)



# =========================
# Count atoms in one side
# =========================

def count_side(compounds):


    total = {}


    for formula in compounds:


        atoms = parse_formula(
            formula
        )


        for element, count in atoms.items():


            total[element] = (

                total.get(element, 0)

                +

                count

            )


    return total





# =========================
# Main Reaction Solver
# =========================

def solve_reaction(reaction):


    data = analyze_reaction_input(
        reaction
    )



    if not data["valid"]:


        return {

            "valid": False,

            "message": "Invalid reaction"

        }





    reactants = data["reactants"]

    products = data["products"]




    reactant_atoms = count_side(
        reactants
    )


    product_atoms = count_side(
        products
    )



    balanced = (

        reactant_atoms == product_atoms

    )



    result = {


        "valid": True,


        "reactants_atoms":
            reactant_atoms,


        "products_atoms":
            product_atoms,


        "balanced":
            balanced


    }




    # اگر بالانس نیست پیشنهاد بده

    if not balanced:


        result["suggestion"] = balance_matrix(

            reaction

        )



    return result





# =========================
# Test
# =========================

if __name__ == "__main__":


    while True:


        reaction = input(
            "Reaction (exit): "
        )



        if reaction.lower() == "exit":

            break



        print(

            solve_reaction(
                reaction
            )

        )