import json
from pathlib import Path

from config import ELEMENTS_PATH



# ========= Database Path =========

COMPOUNDS_PATH = (
    ELEMENTS_PATH.parent / "compounds.json"
)

print("ELEMENTS_PATH :", ELEMENTS_PATH)
print("COMPOUNDS_PATH:", COMPOUNDS_PATH)


# ========= Load =========

def load_compounds():

    if not COMPOUNDS_PATH.exists():

        return []


    with open(
        COMPOUNDS_PATH,
        "r",
        encoding="utf-8"
    ) as file:


        content = file.read().strip()


        if not content:

            return []


        return json.loads(content)



# ========= Save =========

def save_compounds(compounds):

    print("Saving to:", COMPOUNDS_PATH)

    with open(
        COMPOUNDS_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            compounds,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Number of compounds:", len(compounds))



# ========= Find =========

def find_compound(formula):


    compounds = load_compounds()



    for compound in compounds:


        if compound["formula"].lower() == formula.lower():

            return compound



    return None



# ========= Add =========

def add_compound(compound):

    compounds = load_compounds()

    for c in compounds:
        
        if c["formula"].lower() == compound["formula"].lower():

            return False
    compounds.append(compound)

    save_compounds(compounds)

    return True



# ========= Update =========

def update_compound(
        formula,
        new_data
):


    compounds = load_compounds()



    for compound in compounds:


        if compound["formula"].lower() == formula.lower():


            compound.update(
                new_data
            )


            save_compounds(
                compounds
            )


            return True



    return False



# ========= Delete =========

def delete_compound(formula):


    compounds = load_compounds()



    new_list = [

        c for c in compounds

        if c["formula"].lower()
        != formula.lower()

    ]



    if len(new_list) == len(compounds):

        return False



    save_compounds(
        new_list
    )


    return True



# ========= Test =========

if __name__ == "__main__":


    while True:


        print(
            "\n===== DATABASE MANAGER ====="
        )


        print(
            "1. Find compound"
        )


        print(
            "2. Delete compound"
        )


        print(
            "3. Exit"
        )


        choice = input(
            "Choose: "
        )



        if choice == "1":


            formula = input(
                "Formula: "
            )


            result = find_compound(
                formula
            )


            print(
                result
            )



        elif choice == "2":


            formula = input(
                "Formula: "
            )


            if delete_compound(formula):

                print(
                    "Deleted"
                )

            else:

                print(
                    "Not found"
                )



        elif choice == "3":

            break