from config import COMMON_NAMES_PATH

from models.core.database_loader import JsonDatabase


# ==========================================================
# Database
# ==========================================================

common_name_db = JsonDatabase(
    COMMON_NAMES_PATH
)


# ==========================================================
# Find by Formula
# ==========================================================

def find_common_name(
    formula: str,
):
    """
    Returns a normalized naming dictionary.

    Output
    ------
    {
        "name": "...",
        "iupac_name": "...",
        "common_name": "..."
    }
    """

    compound = common_name_db.find_by_formula(
        formula
    )

    if compound is None:
        return None

    common_name = compound.get(
        "common_name",
        ""
    )

    iupac_name = compound.get(
        "iupac_name",
        common_name
    )

    return {

        "name": common_name,

        "iupac_name": iupac_name,

        "common_name": common_name,

    }


# ==========================================================
# Find by Name
# ==========================================================

def find_common_name_by_name(
    name: str,
):

    compound = common_name_db.find_by_name(
        name
    )

    if compound is None:
        return None

    common_name = compound.get(
        "common_name",
        ""
    )

    iupac_name = compound.get(
        "iupac_name",
        common_name
    )

    return {

        "name": common_name,

        "iupac_name": iupac_name,

        "common_name": common_name,

    }


# ==========================================================
# Exists
# ==========================================================

def has_common_name(
    formula: str,
):

    return common_name_db.exists(
        formula
    )


# ==========================================================
# Reload
# ==========================================================

def reload_common_names():

    common_name_db.reload()