from collections import defaultdict
import re


# ==========================================================
# Patterns
# ==========================================================

ELEMENT_PATTERN = re.compile(
    r"[A-Z][a-z]?"
)


# ==========================================================
# Read Multiplier
# ==========================================================

def read_multiplier(tokens, index):
    """
    Read multiplier after an element or group.

    Returns
    -------
    tuple
        (multiplier, new_index)
    """

    if (
        index + 1 < len(tokens)
        and tokens[index + 1].isdigit()
    ):

        return int(tokens[index + 1]), index + 1

    return 1, index


# ==========================================================
# Parse Tokens
# ==========================================================

def parse_tokens(tokens: list[str]) -> dict:
    """
    Convert tokenized formula into atom counts.
    """

    stack = [defaultdict(int)]

    i = 0

    while i < len(tokens):

        token = tokens[i]

        # --------------------------------------------------
        # Opening Parenthesis
        # --------------------------------------------------

        if token == "(":

            stack.append(defaultdict(int))

        # --------------------------------------------------
        # Closing Parenthesis
        # --------------------------------------------------

        elif token == ")":

            if len(stack) == 1:

                raise ValueError(
                    "Unmatched closing parenthesis."
                )

            group = stack.pop()

            multiplier, i = read_multiplier(
                tokens,
                i
            )

            for atom, count in group.items():

                stack[-1][atom] += (
                    count * multiplier
                )

        # --------------------------------------------------
        # Element
        # --------------------------------------------------

        elif ELEMENT_PATTERN.fullmatch(token):

            multiplier, i = read_multiplier(
                tokens,
                i
            )

            stack[-1][token] += multiplier

        # --------------------------------------------------
        # Invalid Token
        # --------------------------------------------------

        else:

            raise ValueError(
                f"Unexpected token: {token}"
            )

        i += 1

    if len(stack) != 1:

        raise ValueError(
            "Missing closing parenthesis."
        )

    return dict(stack[0])