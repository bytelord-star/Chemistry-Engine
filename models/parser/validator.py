import re

from models.parser.formula_validator import (
    is_valid_formula,
)

# ==========================================================
# Patterns
# ==========================================================

ELEMENT_PATTERN = re.compile(
    r"[A-Z][a-z]?"
)


# ==========================================================
# Detect Input Type
# ==========================================================

def detect_input_type(
    text: str,
) -> str:
    """
    Detect chemistry input type.

    Returns
    -------
    element
    compound
    reaction
    invalid
    """

    text = text.strip()

    if not text:
        return "invalid"

    # ------------------------------------------------------
    # Reaction
    # ------------------------------------------------------

    if "=" in text or "->" in text:
        return "reaction"

    # ------------------------------------------------------
    # Element
    # ------------------------------------------------------

    if ELEMENT_PATTERN.fullmatch(text):
        return "element"

    # ------------------------------------------------------
    # Compound
    # ------------------------------------------------------

    if is_valid_formula(text):
        return "compound"

    # ------------------------------------------------------
    # Invalid
    # ------------------------------------------------------

    return "invalid"