from models.parser.formula_tokenizer import tokenize
from models.parser.formula_groups import parse_tokens
from models.parser.polyatomic_detector import detect_polyatomic_ions


def parse_formula(formula):

    tokens = tokenize(formula)

    atoms = parse_tokens(tokens)

    polyatomic = detect_polyatomic_ions(formula)

    groups = []

    for ion in polyatomic:

        groups.append({

            "formula": ion["formula"],

            "count": ion["count"]

        })

    return {

        "formula": formula,

        "atoms": atoms,

        "groups": groups,

        "polyatomic_ions": polyatomic,

        "total_atoms": sum(atoms.values())

    }

