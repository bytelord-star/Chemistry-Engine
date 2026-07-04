import json

from config import BASES_PATH


def load_bases():
    """
    Load all bases from database.
    """

    with open(
        BASES_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def find_base(formula):

    bases = load_bases()

    for base in bases:

        if base["formula"] == formula:

            return base

    return None


def find_base_by_name(name):

    bases = load_bases()

    name = name.lower()

    for base in bases:

        if base["name"].lower() == name:
            return base

        if base["iupac_name"].lower() == name:
            return base

        if base["common_name"].lower() == name:
            return base

    return None


def get_strong_bases():

    bases = load_bases()

    return [

        base

        for base in bases

        if base["strength"] == "Strong"

    ]


def get_alkalis():

    bases = load_bases()

    return [

        base

        for base in bases

        if base["is_alkali"]

    ]