from config import POLYATOMIC_IONS_PATH

from models.core.database_loader import JsonDatabase


# ==========================================================
# Database
# ==========================================================

polyatomic_db = JsonDatabase(

    POLYATOMIC_IONS_PATH,

    formula_key="formula",

    name_keys=[

        "name",

        "iupac_name",

        "common_name",

        "aliases",

    ],

)


# ==========================================================
# Find by Formula
# ==========================================================

def get_polyatomic_by_formula(
    formula: str,
):

    return polyatomic_db.find_by_formula(

        formula

    )


# ==========================================================
# Find by Name
# ==========================================================

def get_polyatomic_by_name(
    name: str,
):

    return polyatomic_db.find_by_name(

        name

    )


# ==========================================================
# Exists
# ==========================================================

def polyatomic_exists(
    formula: str,
):

    return polyatomic_db.exists(

        formula

    )


# ==========================================================
# Get All
# ==========================================================

def get_all_polyatomic():

    return polyatomic_db.all()


# ==========================================================
# Reload
# ==========================================================

def reload_polyatomic_database():

    polyatomic_db.reload()


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print(

        get_polyatomic_by_formula(

            "SO4"

        )

    )

    print(

        get_polyatomic_by_formula(

            "CO3"

        )

    )

    print(

        get_polyatomic_by_name(

            "Sulfate"

        )

    )