from config import ACIDS_PATH

from models.core.database_loader import JsonDatabase


# ==========================================================
# Database
# ==========================================================

acid_db = JsonDatabase(
    ACIDS_PATH
)


# ==========================================================
# Find by Formula
# ==========================================================

def find_acid(
    formula: str,
):

    return acid_db.find_by_formula(
        formula
    )


# ==========================================================
# Find by Name
# ==========================================================

def find_acid_by_name(
    name: str,
):

    return acid_db.find_by_name(
        name
    )


# ==========================================================
# Strong Acids
# ==========================================================

def get_strong_acids():

    return acid_db.filter(
        "strength",
        "Strong"
    )


# ==========================================================
# Organic Acids
# ==========================================================

def get_organic_acids():

    return acid_db.filter(
        "is_organic",
        True
    )


# ==========================================================
# Reload
# ==========================================================

def reload_acids():

    acid_db.reload()