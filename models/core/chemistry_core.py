import json
from pathlib import Path
import sys

# =========================
# Root
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# =========================
# Config
# =========================

from config import ELEMENTS_PATH

# =========================
# Imports
# =========================

from models.parser.validator import detect_input_type
from models.reaction.reaction_validator import is_reaction

from models.reaction.reaction_engine import solve_reaction
from models.compound.compound_engine import create_compound
from models.core.database_manager import find_compound

# =========================
# Load Elements
# =========================

with open(
    ELEMENTS_PATH,
    "r",
    encoding="utf-8"
) as file:

    ELEMENTS = json.load(file)


# =========================
# Find Element
# =========================

def find_element(symbol):

    for element in ELEMENTS:

        if element["symbol"].lower() == symbol.lower():

            return element

    return None


# =========================
# Main Analyze Function
# =========================

def analyze(query):

    query = query.strip()

    if not query:

        return {

            "success": False,
            "message": "Empty input"

        }

    # =====================================
    # Reaction
    # =====================================

    if is_reaction(query):

        reaction = solve_reaction(query)

        return {

            "success": True,

            "type": "reaction",

            "data": reaction

        }

    # =====================================
    # Detect Type
    # =====================================

    input_type = detect_input_type(query)

    # =====================================
    # Element
    # =====================================

    if input_type == "element":

        element = find_element(query)

        if element:

            return {

                "success": True,

                "type": "element",

                "data": element

            }

        return {

            "success": False,

            "message": "Element not found"

        }

    # =====================================
    # Compound
    # =====================================

    elif input_type == "compound":

        compound = find_compound(query)

        if compound is None:

            try:

                compound = create_compound(query)

            except Exception as error:

                return {

                    "success": False,

                    "message": str(error)

                }

        return {

            "success": True,

            "type": "compound",

            "data": compound

        }

    # =====================================
    # Invalid
    # =====================================

    return {

        "success": False,

        "message": "Unknown chemistry input"

    }


# =========================
# Test
# =========================

if __name__ == "__main__":

    while True:

        query = input("\nSearch (exit): ")

        if query.lower() == "exit":

            break

        result = analyze(query)

        print(result)