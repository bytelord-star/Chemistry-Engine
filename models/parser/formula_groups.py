from collections import defaultdict
import re


def parse_tokens(tokens):

    """
    Parse tokenized chemical formula.

    Parameters
    ----------
    tokens : list[str]

    Returns
    -------
    dict
        atoms dictionary
    """

    stack = [defaultdict(int)]

    i = 0

    while i < len(tokens):

        token = tokens[i]

        # ------------------------
        # Opening Parenthesis
        # ------------------------

        if token == "(":

            stack.append(
                defaultdict(int)
            )

        # ------------------------
        # Closing Parenthesis
        # ------------------------

        elif token == ")":

            if len(stack) == 1:

                raise ValueError(
                    "Unmatched closing parenthesis."
                )

            group = stack.pop()

            multiplier = 1

            if (

                i + 1 < len(tokens)

                and

                tokens[i + 1].isdigit()

            ):

                multiplier = int(

                    tokens[i + 1]

                )

                i += 1

            for atom, count in group.items():

                stack[-1][atom] += (

                    count * multiplier

                )

        # ------------------------
        # Element
        # ------------------------

        elif re.fullmatch(

            r"[A-Z][a-z]?",

            token

        ):

            multiplier = 1

            if (

                i + 1 < len(tokens)

                and

                tokens[i + 1].isdigit()

            ):

                multiplier = int(

                    tokens[i + 1]

                )

                i += 1

            stack[-1][token] += multiplier

        else:

            raise ValueError(

                f"Unexpected token: {token}"

            )

        i += 1

    if len(stack) != 1:

        raise ValueError(

            "Missing closing parenthesis."

        )

    return dict(

        stack[0]

    )