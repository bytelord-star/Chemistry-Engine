import re


def tokenize(formula: str):

    """
    Convert a chemical formula into tokens.

    Example:
        Fe2(SO4)3

    Returns:
        ['Fe','2','(','S','O','4',')','3']
    """

    return re.findall(

        r"[A-Z][a-z]?|\d+|\(|\)",

        formula

    )