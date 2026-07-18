import re


# ==========================================================
# Patterns
# ==========================================================

TOKEN_PATTERN = re.compile(
    r"[A-Z][a-z]?|\d+|\(|\)"
)


# ==========================================================
# Tokenizer
# ==========================================================

def tokenize(
    formula: str,
) -> list[str]:
    """
    Convert a chemical formula into tokens.

    Example
    -------
    Fe2(SO4)3

    Returns
    -------
    list[str]

    ['Fe', '2', '(', 'S', 'O', '4', ')', '3']
    """

    return TOKEN_PATTERN.findall(formula)


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print(tokenize("Fe2(SO4)3"))

    print(tokenize("Ca(OH)2"))

    print(tokenize("NaCl"))