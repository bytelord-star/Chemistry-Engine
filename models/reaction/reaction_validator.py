# models/reaction_validator.py

from models.parser.formula_validator import is_valid_formula

from models.parser.element_validator import validate_elements



# =========================
# Check Reaction Format
# =========================

def is_reaction(text):


    text = text.strip()


    # باید = یا -> داشته باشد

    if "=" in text:

        return True


    if "->" in text:

        return True


    return False





# =========================
# Split Reaction
# =========================

def split_reaction(reaction):


    if "=" in reaction:


        left, right = reaction.split(
            "=",
            1
        )


    elif "->" in reaction:


        left, right = reaction.split(
            "->",
            1
        )


    else:


        return None, None



    reactants = [

        x.strip()

        for x in left.split("+")
    ]



    products = [

        x.strip()

        for x in right.split("+")
    ]



    return reactants, products





# =========================
# Validate Formulas
# =========================

def validate_reaction(reaction):


    if not is_reaction(reaction):

        return False



    reactants, products = split_reaction(
        reaction
    )



    if not reactants or not products:

        return False



    all_compounds = (
        reactants + products
    )



    for formula in all_compounds:



        if not is_valid_formula(formula):

            return False



        if not validate_elements(formula):

            return False



    return True





# =========================
# Full Analysis
# =========================

def analyze_reaction_input(reaction):


    if not validate_reaction(reaction):

        return {

            "valid": False,

            "message":
            "Invalid reaction"

        }



    reactants, products = split_reaction(
        reaction
    )



    return {


        "valid": True,


        "reactants": reactants,


        "products": products


    }