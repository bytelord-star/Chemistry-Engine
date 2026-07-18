from models.parser.formula_parser import parse_formula
from models.core.element_manager import get_atomic_mass


# =========================
# Calculate Molar Mass
# =========================

def calculate_molar_mass(atoms):

    total_mass = 0.0

    for symbol, count in atoms.items():

        atomic_mass = get_atomic_mass(symbol)

        if atomic_mass is None:

            raise ValueError(
                f"Element '{symbol}' not found."
            )

        total_mass += atomic_mass * count

    return round(total_mass, 4)


# =========================
# Test
# =========================

def main():

    while True:

        print("\n===== MOLAR MASS CALCULATOR =====")

        formula = input(
            "Formula (exit): "
        ).strip()

        if formula.lower() == "exit":
            break

        try:

            parsed = parse_formula(formula)

            mass = calculate_molar_mass(
                parsed["atoms"]
            )

            print(
                f"\nMolar Mass = {mass} g/mol"
            )

        except ValueError as error:

            print(f"\n❌ {error}")


if __name__ == "__main__":
    main()