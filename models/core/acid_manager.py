import json
from pathlib import Path

from config import ACIDS_PATH


def load_acids():
    """
    Load all acids from database.
    """

    with open(
        ACIDS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)
    
def find_acid(formula):

    acids = load_acids()

    for acid in acids:

        if acid["formula"] == formula:

            return acid

    return None

def find_acid_by_name(name):

    acids = load_acids()

    name = name.lower()

    for acid in acids:

        if acid["name"].lower() == name:
            return acid

        if acid["iupac_name"].lower() == name:
            return acid

        if acid["common_name"].lower() == name:
            return acid

    return None


def get_strong_acids():

    acids = load_acids()

    return [

        acid

        for acid in acids

        if acid["strength"] == "Strong"

    ]

def get_organic_acids():

    acids = load_acids()

    return [

        acid

        for acid in acids

        if acid["is_organic"]

    ]

if __name__ == "__main__":

    print(find_acid("H2SO4"))

    print()

    print(find_acid_by_name("Acetic Acid"))

    print()

    print(len(get_strong_acids()))

    print(len(get_organic_acids()))