from config import BASES_PATH

from models.core.database_loader import JsonDatabase


# ==========================================================
# Database
# ==========================================================

base_db = JsonDatabase(
    BASES_PATH
)


# ==========================================================
# Find by Formula
# ==========================================================

def find_base(
    formula: str,
):

    return base_db.find_by_formula(
        formula
    )


# ==========================================================
# Find by Name
# ==========================================================

def find_base_by_name(
    name: str,
):

    return base_db.find_by_name(
        name
    )


# ==========================================================
# Strong Bases
# ==========================================================

def get_strong_bases():

    return base_db.filter(
        "strength",
        "Strong"
    )


# ==========================================================
# Alkalis
# ==========================================================

def get_alkalis():

    return base_db.filter(
        "is_alkali",
        True
    )


# ==========================================================
# Reload
# ==========================================================

def reload_bases():

    base_db.reload()