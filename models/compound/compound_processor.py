from models.naming.name_manager import generate_name

from models.compound.bonding import calculate_bond_type
from models.compound.compound_classification import classify_compound
from models.compound.molecular_mass import calculate_molar_mass
from models.compound.molecular_polarity import predict_polarity

from models.core.acid_manager import find_acid
from models.core.base_manager import find_base


# ==========================================================
# Calculate Properties
# ==========================================================

def calculate_properties(
    parsed,
    formula,
):
    """
    Calculate physical properties of a compound.
    """

    molar_mass = calculate_molar_mass(
        parsed["atoms"]
    )

    bond_type = calculate_bond_type(
        parsed
    )

    molecular_polarity = predict_polarity(
        bond_type,
        formula,
    )

    return {

        "molar_mass": molar_mass,

        "bond_type": bond_type,

        "molecular_polarity": molecular_polarity,

    }


# ==========================================================
# Collect Metadata
# ==========================================================

def collect_metadata(
    parsed,
):
    """
    Collect classification and extra metadata.
    """

    classification = classify_compound(
        parsed
    )

    acid_data = None

    base_data = None

    if classification["type"] == "Acid":

        acid_data = find_acid(
            parsed["formula"]
        )

    elif classification["type"] == "Base":

        base_data = find_base(
            parsed["formula"]
        )

    return {

        "classification": classification,

        "acid_data": acid_data,

        "base_data": base_data,

    }


# ==========================================================
# Prepare Compound Data
# ==========================================================

def prepare_compound_data(
    parsed,
    formula,
):
    """
    Prepare every piece of data required
    to build a compound object.
    """

    properties = calculate_properties(
        parsed,
        formula,
    )

    metadata = collect_metadata(
        parsed,
    )

    name_data = generate_name(

    parsed,

    metadata["classification"],

    metadata["acid_data"],

    metadata["base_data"],

)

    return {

    "parsed": parsed,

    "name_data": name_data,

    **properties,

    **metadata,

}