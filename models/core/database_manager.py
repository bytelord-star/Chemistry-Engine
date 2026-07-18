from config import COMPOUNDS_PATH

from models.core.database_loader import JsonDatabase


# ==========================================================
# Database
# ==========================================================

compound_db = JsonDatabase(
    COMPOUNDS_PATH
)


# ==========================================================
# Load
# ==========================================================

def load_compounds():

    return compound_db.all()


# ==========================================================
# Save
# ==========================================================

def save_compounds(compounds):

    compound_db.data = compounds

    compound_db.save()


# ==========================================================
# Exists
# ==========================================================

def compound_exists(
    formula: str,
):

    return compound_db.exists(
        formula
    )


# ==========================================================
# Find
# ==========================================================

def find_compound(
    formula: str,
):

    return compound_db.find_by_formula(
        formula
    )


# ==========================================================
# Add
# ==========================================================

def add_compound(
    compound: dict,
):

    if compound_db.exists(

        compound["formula"]

    ):

        return False

    compound_db.append(
        compound
    )

    return True


# ==========================================================
# Update
# ==========================================================

def update_compound(
    formula: str,
    new_data: dict,
):

    return compound_db.update(

        formula,

        new_data,

    )


# ==========================================================
# Delete
# ==========================================================

def delete_compound(
    formula: str,
):

    return compound_db.delete(
        formula
    )


# ==========================================================
# Reload
# ==========================================================

def reload_compounds():

    compound_db.reload()


# ==========================================================
# Count
# ==========================================================

def compound_count():

    return len(
        compound_db
    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    while True:

        print("\n===== DATABASE MANAGER =====")

        print("1. Find Compound")

        print("2. Delete Compound")

        print("3. Count")

        print("4. Exit")

        choice = input(
            "Choose: "
        ).strip()

        if choice == "1":

            formula = input(
                "Formula: "
            ).strip()

            print(
                find_compound(
                    formula
                )
            )

        elif choice == "2":

            formula = input(
                "Formula: "
            ).strip()

            print(

                "Deleted."

                if delete_compound(
                    formula
                )

                else

                "Compound not found."

            )

        elif choice == "3":

            print(
                compound_count()
            )

        elif choice == "4":

            break