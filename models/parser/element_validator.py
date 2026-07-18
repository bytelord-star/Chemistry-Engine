import re

from models.core.element_manager import element_exists


# ==========================================================
# Pattern
# ==========================================================

ELEMENT_PATTERN = re.compile(
    r"[A-Z][a-z]?"
)


# ==========================================================
# Extract Element Symbols
# ==========================================================

def extract_element_symbols(
    formula: str,
) -> list[str]:
    """
    Extract element symbols from a chemical formula.

    Example
    -------
    H2SO4 -> ["H", "S", "O"]
    """

    return ELEMENT_PATTERN.findall(
        formula
    )


# ==========================================================
# Validate Elements
# ==========================================================

def validate_elements(
    formula: str,
) -> bool:
    """
    Check whether every extracted element
    exists in the database.
    """

    return all(

        element_exists(symbol)

        for symbol in extract_element_symbols(
            formula
        )

    )