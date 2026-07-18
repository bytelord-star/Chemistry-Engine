from models.parser.formula_tokenizer import tokenize
from models.parser.token_parser import parse_tokens
from models.parser.polyatomic_detector import detect_polyatomic_ions


# ==========================================================
# Formula Parser
# ==========================================================

def parse_formula(formula: str) -> dict:


    tokens = tokenize(formula)

    atoms = parse_tokens(tokens)

    polyatomic_ions = detect_polyatomic_ions(
        formula
    )

    return {

        "formula": formula,

        "tokens": tokens,

        "atoms": atoms,
 # Reserved for future parser upgrades
        "groups": [],

        "polyatomic_ions": polyatomic_ions,

        "total_atoms": sum(
            atoms.values()
        ),

    }