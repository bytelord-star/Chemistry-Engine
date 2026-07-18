from models.core.element_manager import get_element
from models.naming.prefixes import get_prefix
from models.naming.naming_rules import (
    to_ide,
    combine_prefix,
    show_mono,
    format_name,
)


# ==========================================================
# Molecular Naming
# ==========================================================

def generate_molecular_name(parsed):
    """
    Generate IUPAC name for a binary molecular compound.

    Examples
    --------
    CO2  -> Carbon Dioxide
    CO   -> Carbon Monoxide
    SO3  -> Sulfur Trioxide
    N2O5 -> Dinitrogen Pentoxide
    """

    atoms = parsed["atoms"]

    # ---------------------------------------------
    # Only binary molecular compounds are supported
    # ---------------------------------------------

    if len(atoms) != 2:

        return {

            "name": "Unknown Molecular Compound",

            "iupac_name": "Unknown Molecular Compound",

            "common_name": "Unknown Molecular Compound",

        }

    symbols = list(atoms.keys())

    first_symbol = symbols[0]
    second_symbol = symbols[1]

    first_count = atoms[first_symbol]
    second_count = atoms[second_symbol]

    first_element = get_element(first_symbol)
    second_element = get_element(second_symbol)

    if first_element is None or second_element is None:

        return {

            "name": "Unknown Molecular Compound",

            "iupac_name": "Unknown Molecular Compound",

            "common_name": "Unknown Molecular Compound",

        }

    # =====================================================
    # First Element
    # =====================================================

    first_name = first_element["name"]

    if first_count > 1:

        first_name = (

            get_prefix(first_count)

            +

            first_name.lower()

        )

    # =====================================================
    # Second Element
    # =====================================================

    second_name = to_ide(

        second_element["name"]

    )

    if second_count == 1:

        if show_mono(False):

            second_name = combine_prefix(

                "mono",

                second_name

            )

    else:

        second_name = combine_prefix(

            get_prefix(second_count),

            second_name

        )

    # =====================================================
    # Final Name
    # =====================================================

    final_name = format_name(

        first_name

        +

        " "

        +

        second_name

    )

    return {

    "name": final_name,

    "iupac_name": final_name,

    "common_name": None,

}