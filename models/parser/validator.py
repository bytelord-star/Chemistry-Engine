import re


def detect_input_type(text):

    text = text.strip()

    # Reaction

    if "=" in text or "->" in text:

        return "reaction"

    # Element

    if re.fullmatch(
        r"[A-Z][a-z]?",
        text
    ):

        return "element"

    # Compound

    if re.fullmatch(
        r"[A-Za-z0-9()]+",
        text
    ):

        return "compound"

    return "invalid"