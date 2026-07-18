# ========= Naming =========
from models.naming.name_manager import generate_name
# ========= Parser =========
from models.parser.formula_validator import is_valid_formula
from models.parser.element_validator import validate_elements
from models.parser.formula_parser import parse_formula

# ========= Compound =========
from models.compound.compound_builder import build_compound
from models.compound.compound_processor import (
    prepare_compound_data,
)

# ========= Database =========
from models.core.database_manager import (
    add_compound,
    find_compound,
)


# ==========================================================
# Validation
# ==========================================================

def validate_formula_input(
    formula: str,
):

    if not is_valid_formula(formula):

        raise ValueError(
            f"Invalid formula: {formula}"
        )

    if not validate_elements(formula):

        raise ValueError(
            f"Unknown element in formula: {formula}"
        )


# ==========================================================
# Database
# ==========================================================

def load_existing_compound(
    formula: str,
):

    compound = find_compound(
        formula
    )

    if compound is not None:

        print(
            "✓ Loaded from database"
        )

    return compound


# ==========================================================
# Save
# ==========================================================

def save_compound(
    compound: dict,
):

    if add_compound(compound):

        print(
            "✓ Saved to database."
        )

    else:

        print(
            "✓ Already exists."
        )


# ==========================================================
# Create Compound
# ==========================================================

def create_compound(
    formula: str,
):

    formula = formula.strip()

    validate_formula_input(
        formula
    )

    compound = load_existing_compound(
        formula
    )

    if compound:

        return compound

    print(
        "Creating new compound..."
    )

    parsed = parse_formula(
        formula
    )

    data = prepare_compound_data(

        parsed,

        formula,

    )

    

    compound = build_compound(

    parsed=data["parsed"],

    name_data=data["name_data"],

    molar_mass=data["molar_mass"],

    bond_type=data["bond_type"],

    molecular_polarity=data["molecular_polarity"],

    classification=data["classification"],

    acid_data=data["acid_data"],

    base_data=data["base_data"],

)

    save_compound(
        compound
    )

    return compound


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    while True:

        formula = input(
            "\nFormula (exit): "
        ).strip()

        if formula.lower() == "exit":

            break

        result = create_compound(
            formula
        )

        print(
            "\n========== RESULT =========="
        )

        for key, value in result.items():

            print(
                f"{key}: {value}"
            )