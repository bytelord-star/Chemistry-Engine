import re


# ==========================================================
# Patterns
# ==========================================================

FORMULA_PATTERN = re.compile(
    r"[A-Za-z0-9()]+"
)


# ==========================================================
# Formula Validator
# ==========================================================

def is_valid_formula(formula: str) -> bool:
    """
    Validate the basic syntax of a chemical formula.

    Checks:
    - Allowed characters
    - Balanced parentheses
    """

    formula = formula.strip()

    if not formula:
        return False

    if not FORMULA_PATTERN.fullmatch(formula):
        return False

    parentheses_stack = []

    for char in formula:

        if char == "(":

            parentheses_stack.append(char)

        elif char == ")":

            if not parentheses_stack:
                return False

            parentheses_stack.pop()

    return len(parentheses_stack) == 0


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    tests = [

        "H2O",
        "NaCl",
        "Ca(OH)2",
        "Fe2(SO4)3",
        "Ca(OH",
        "H2O)",
        "",
        "Na@Cl"

    ]

    for formula in tests:

        print(f"{formula:<12} -> {is_valid_formula(formula)}")