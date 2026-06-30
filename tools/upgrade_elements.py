import json
import sys
from pathlib import Path


# ========= Project Root =========

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))


from config import ELEMENTS_PATH


# ========= Data Paths =========

DATA_DIR = ELEMENTS_PATH.parent


GROUPS_PATH = DATA_DIR / "periodic_groups.json"

VALENCE_PATH = DATA_DIR / "valence_data.json"



# ========= Load JSON =========

def load_json(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except FileNotFoundError:

        print(f"❌ File not found: {path}")

        exit()



elements = load_json(
    ELEMENTS_PATH
)


periodic_groups = load_json(
    GROUPS_PATH
)


valence_data = load_json(
    VALENCE_PATH
)



# ========= Create Category Lookup =========

category_lookup = {}


for category, numbers in periodic_groups.items():


    for number in numbers:

        category_lookup[number] = category



# ========= Upgrade Database =========

updated_category = 0
updated_valence = 0


for element in elements:


    atomic_number = element.get(
        "atomic_number"
    )


    symbol = element.get(
        "symbol"
    )



    # ---- Category ----

    if atomic_number in category_lookup:


        element["category"] = (
            category_lookup[atomic_number]
        )

        updated_category += 1


    else:

        element["category"] = "unknown"



    # ---- Valence ----

    if symbol in valence_data:


        element["valence"] = (
            valence_data[symbol]
        )

        updated_valence += 1


    else:

        element["valence"] = []




# ========= Save Elements =========

with open(
    ELEMENTS_PATH,
    "w",
    encoding="utf-8"
) as file:


    json.dump(

        elements,

        file,

        indent=4,

        ensure_ascii=False

    )



# ========= Report =========

print("\n==============================")

print(
    f"✅ Categories updated : {updated_category}"
)

print(
    f"✅ Valences updated   : {updated_valence}"
)


print(
    "🎉 elements.json upgraded successfully!"
)


print("==============================")