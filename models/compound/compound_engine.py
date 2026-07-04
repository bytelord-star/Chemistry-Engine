import sys
from pathlib import Path

# ========= Root =========

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# ========= Models =========


from models.parser.formula_validator import is_valid_formula
from models.parser.element_validator import validate_elements
from models.parser.formula_parser import parse_formula

from models.compound.compound_builder import build_compound
from models.compound.molecular_mass import calculate_molar_mass
from models.compound.compound_classification import classify_compound
from models.compound.bonding import calculate_bond_type
from models.compound.molecular_polarity import predict_polarity

from models.core.base_manager import find_base
from models.core.acid_manager import find_acid
from models.core.database_manager import (
    find_compound,
    add_compound
)


# =========================
# Create Compound
# =========================

def create_compound(formula):

    formula = formula.strip()

    # -----------------------
    # Validate Formula
    # -----------------------

    if not is_valid_formula(formula):

        raise ValueError(
            f"Invalid formula: {formula}"
        )

    # -----------------------
    # Validate Elements
    # -----------------------

    if not validate_elements(formula):

        raise ValueError(
            f"Unknown element in formula: {formula}"
        )

    # -----------------------
    # Database
    # -----------------------

    existing = find_compound(formula)

    if existing:

        print("✓ Loaded from database")

        return existing

    print("Creating new compound...")

    # -----------------------
    # Parse (ONLY ONCE)
    # -----------------------

    parsed = parse_formula(formula)

    atoms = parsed["atoms"]

    # -----------------------
    # Molar Mass
    # -----------------------

    mass = calculate_molar_mass(atoms)

    # -----------------------
    # Bond
    # -----------------------

    bond = calculate_bond_type(parsed)

    # -----------------------
    # Polarity
    # -----------------------

    polarity = predict_polarity(
        bond,
        formula
    )

    # -----------------------
    # Classification
    # -----------------------

    classification = classify_compound(parsed)

    # _____________________

    acid_data = None

    if classification["type"] == "Acid":
        acid_data = find_acid(parsed["formula"])

    base_data = None

    if classification["type"] == "Base":
        base_data = find_base(parsed["formula"])

    # -----------------------
    # Compound Object
    # -----------------------

    compound = build_compound( 

        parsed,
        mass,
        bond,
        polarity,
        classification,
        acid_data,
        base_data

    )

    added = add_compound(compound)

    if added:

        print("✓")

    else:

        print("✓")

    return compound


# =========================
# Test
# =========================

if __name__ == "__main__":

    while True:

        formula = input("\nFormula (exit): ")

        if formula.lower() == "exit":

            break

        result = create_compound(formula)

        print("\n========== RESULT ==========")

        for key, value in result.items():

            print(f"{key}: {value}")