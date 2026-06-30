import json
import sys
from pathlib import Path


# ========= Project Root =========

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))


from config import ELEMENTS_PATH
from models.parser.formula_parser import parse_formula
from models.compound.molecular_mass import calculate_molar_mass



COMPOUNDS_PATH = (
    ELEMENTS_PATH.parent / "compounds.json"
)



# ========= Load JSON =========

def load_json(path):

    if not path.exists():

        return []


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:


        content = file.read().strip()


        if not content:

            return []


        return json.loads(content)




# ========= Save =========

def save_compound(data):


    compounds = load_json(
        COMPOUNDS_PATH
    )


    for c in compounds:

        if c["formula"] == data["formula"]:

            print(
                "\n⚠️ Compound already exists."
            )

            return



    compounds.append(
        data
    )



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



    print(
        "\n✅ Saved"
    )




# ========= Compound Type =========

def classify_compound(atoms):


    has_metal = False


    for symbol in atoms:


        element = next(

            (
                e for e in load_json(ELEMENTS_PATH)
                if e["symbol"] == symbol
            ),

            None

        )


        if element:

            category = element.get(
                "category"
            )


            if "metal" in str(category):

                has_metal = True



    if has_metal:

        return "Inorganic Compound"


    return "Molecular Compound"




# ========= Main =========

def main():


    print(
        "\n========== COMPOUND MAKER V2 =========="
    )


    formula = input(
        "Enter formula: "
    ).strip()



    try:

        atoms = parse_formula(
            formula
        )


        mass = calculate_molar_mass(
            formula
        )



    except Exception as error:


        print(
            f"❌ Error: {error}"
        )

        return



    compound = {


        "formula": formula,


        "elements": atoms,


        "total_atoms":
            sum(atoms.values()),


        "molar_mass":
            mass,


        "compound_type":
            classify_compound(atoms)


    }



    save_compound(
        compound
    )



    print(
        "\n========== RESULT =========="
    )


    for key,value in compound.items():

        print(
            f"{key}: {value}"
        )




if __name__ == "__main__":

    main()