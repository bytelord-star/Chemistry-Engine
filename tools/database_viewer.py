import sys
from pathlib import Path


# ========= Project Root =========

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))


from models.core.database_manager import (
    load_compounds,
    find_compound
)



# =========================
# Show All Compounds
# =========================

def show_all():


    compounds = load_compounds()



    if not compounds:

        print(
            "\nDatabase is empty."
        )

        return



    print(
        "\n========== ALL COMPOUNDS =========="
    )


    for index, compound in enumerate(
        compounds,
        start=1
    ):


        print(
            f"{index}. {compound['formula']}"
        )



    print(
        f"\nTotal: {len(compounds)} compounds"
    )



# =========================
# Search
# =========================

def search_compound():


    formula = input(
        "\nEnter formula: "
    )



    result = find_compound(
        formula
    )



    if result:


        print(
            "\n========== FOUND =========="
        )


        for key,value in result.items():

            print(
                f"{key}: {value}"
            )


    else:


        print(
            "❌ Compound not found"
        )



# =========================
# Menu
# =========================

def main():


    while True:


        print(
            "\n=============================="
        )

        print(
            "       DATABASE VIEWER"
        )

        print(
            "=============================="
        )


        print(
            "1. Show all compounds"
        )


        print(
            "2. Search compound"
        )


        print(
            "3. Exit"
        )



        choice = input(
            "\nChoose: "
        )



        if choice == "1":

            show_all()



        elif choice == "2":

            search_compound()



        elif choice == "3":

            break



        else:

            print(
                "Invalid choice"
            )




if __name__ == "__main__":

    main()