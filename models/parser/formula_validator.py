import re


def is_valid_formula(formula):

    formula = formula.strip()


    if not re.fullmatch(
        r"[A-Za-z0-9()]+",
        formula
    ):
        return False


    stack = []

    for char in formula:

        if char == "(":
            stack.append(char)

        elif char == ")":

            if not stack:
                return False

            stack.pop()

    if stack:
        return False

    return True