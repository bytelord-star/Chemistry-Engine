import json
import re

from config import ELEMENTS_PATH


with open(
    ELEMENTS_PATH,
    "r",
    encoding="utf-8"
) as file:

    elements = json.load(file)



VALID_SYMBOLS = {

    element["symbol"]

    for element in elements

}



def extract_symbols(formula):

    return re.findall(

        r"[A-Z][a-z]?",

        formula

    )



def validate_elements(formula):


    symbols = extract_symbols(
        formula
    )


    for symbol in symbols:


        if symbol not in VALID_SYMBOLS:

            return False


    return True