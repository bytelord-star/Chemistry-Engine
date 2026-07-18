from models.naming.acid_naming import generate_acid_name
from models.naming.base_naming import generate_base_name
from models.naming.salt_naming import generate_salt_name
from models.naming.metal_oxide_naming import generate_metal_oxide_name
from models.naming.molecular_naming import generate_molecular_name

from models.core.common_name_manager import find_common_name


# ==========================================================
# Naming Routers
# ==========================================================

NAMING_ROUTERS = {

    "Salt": generate_salt_name,

    "Molecular Compound": generate_molecular_name,

}


# ==========================================================
# Generate Name
# ==========================================================

def generate_name(
    parsed,
    classification,
    acid_data=None,
    base_data=None,
):

    # ------------------------------------------------------
    # Acid
    # ------------------------------------------------------

    if acid_data is not None:

        return generate_acid_name(
            parsed,
            acid_data,
        )

    # ------------------------------------------------------
    # Base
    # ------------------------------------------------------

    if base_data is not None:

        return generate_base_name(
            parsed,
            base_data,
        )

    # ------------------------------------------------------
    # Oxides
    # ------------------------------------------------------

    if classification["type"] == "Oxide":

        if classification["subcategory"] == "Metal Oxide":

            name_data = generate_metal_oxide_name(
                parsed
            )

        else:

            name_data = generate_molecular_name(
                parsed
            )

    # ------------------------------------------------------
    # Other Naming Engines
    # ------------------------------------------------------

    else:

        generator = NAMING_ROUTERS.get(
            classification["type"]
        )

        if generator:

            name_data = generator(
                parsed
            )

        else:

            formula = parsed["formula"]

            name_data = {

                "name": formula,

                "iupac_name": formula,

                "common_name": None,

            }

    # ------------------------------------------------------
    # Apply Common Name
    # ------------------------------------------------------

    common = find_common_name(
        parsed["formula"]
    )

    if common:

        name_data["name"] = common["common_name"]

        name_data["common_name"] = common["common_name"]

    else:

        name_data["name"] = name_data["iupac_name"]

        name_data["common_name"] = None

    return name_data