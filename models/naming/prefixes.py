"""
Greek prefixes used in chemical nomenclature.

Examples
--------
1 -> mono
2 -> di
3 -> tri
4 -> tetra
"""

# ==========================================================
# Greek Prefixes
# ==========================================================

PREFIXES = {

    1: "mono",
    2: "di",
    3: "tri",
    4: "tetra",
    5: "penta",
    6: "hexa",
    7: "hepta",
    8: "octa",
    9: "nona",
    10: "deca",

}


# ==========================================================
# Get Prefix
# ==========================================================

def get_prefix(count: int) -> str:
    """
    Return the Greek prefix for a given atom count.

    Parameters
    ----------
    count : int

    Returns
    -------
    str

    Raises
    ------
    ValueError
        If count is less than 1.
    """

    if count < 1:

        raise ValueError(
            "Atom count must be greater than zero."
        )

    return PREFIXES.get(
        count,
        str(count)
    )


# ==========================================================
# Should Display 'mono'
# ==========================================================

def use_mono(count: int) -> bool:
    """
    Determine whether the prefix 'mono' should be displayed.

    Returns
    -------
    bool
    """

    return count == 1


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    for number in range(1, 11):

        print(
            number,
            "->",
            get_prefix(number)
        )