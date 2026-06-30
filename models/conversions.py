import json

from config import ELEMENTS_PATH


# ========= Load Elements Database =========

try:
    with open(ELEMENTS_PATH, "r", encoding="utf-8") as file:
        elements = json.load(file)

except FileNotFoundError:
    print("ERROR: elements.json not found!")
    exit()

except json.JSONDecodeError:
    print("ERROR: Invalid JSON file!")
    exit()
# ========= Constants =========

AVOGADRO_NUMBER = 6.022e23

# ========= Load Elements Database =========

try:
    with open(ELEMENTS_PATH, "r", encoding="utf-8") as file:
        elements = json.load(file)

except FileNotFoundError:
    print("ERROR: elements.json not found!")
    exit()

except json.JSONDecodeError:
    print("ERROR: Invalid JSON file!")
    exit()

# ========= Functions =========

def mass_to_mole_value(symbol, mass):

    element = get_element(symbol)

    if not element:
        return None


    return mass / element["atomic_weight"]



def mole_to_mass_value(symbol, mole):

    element = get_element(symbol)

    if not element:
        return None


    return mole * element["atomic_weight"]



def get_element(symbol):
    """
    Search element by symbol.
    """

    symbol = symbol.strip().lower()

    return next(
        (
            e for e in elements
            if e["symbol"].lower() == symbol
        ),
        None
    )


def show_element_info():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    print("\n========== ELEMENT INFORMATION ==========")

    print(f"Name                : {element.get('name', 'N/A')}")
    print(f"Symbol              : {element.get('symbol', 'N/A')}")
    print(f"Atomic Number       : {element.get('atomic_number', 'N/A')}")
    print(f"Atomic Weight       : {element.get('atomic_weight', 'N/A')} g/mol")
    print(f"Group               : {element.get('group', 'N/A')}")
    print(f"Period              : {element.get('period', 'N/A')}")
    print(f"Electronegativity   : {element.get('electronegativity', 'N/A')}")
    print(f"Electron Affinity   : {element.get('electron_affinity', 'N/A')}")
    print(f"Melting Point       : {element.get('melting_point', 'N/A')} K")
    print(f"Boiling Point       : {element.get('boiling_point', 'N/A')} K")


def mass_to_mole():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    try:
        mass = float(input("Mass (g): "))
    except ValueError:
        print("❌ Invalid number.")
        return

    molar_mass = element["atomic_weight"]

    moles = mass / molar_mass

    print("\n========== RESULT ==========")
    print(f"Element : {element['name']}")
    print(f"Mass    : {mass} g")
    print(f"Moles   : {moles:.6f} mol")


def mole_to_mass():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    try:
        moles = float(input("Moles: "))
    except ValueError:
        print("❌ Invalid number.")
        return

    molar_mass = element["atomic_weight"]

    mass = moles * molar_mass

    print("\n========== RESULT ==========")
    print(f"Element : {element['name']}")
    print(f"Moles   : {moles}")
    print(f"Mass    : {mass:.6f} g")


def mole_to_atoms():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    try:
        moles = float(input("Moles: "))
    except ValueError:
        print("❌ Invalid number.")
        return

    atoms = moles * AVOGADRO_NUMBER

    print("\n========== RESULT ==========")
    print(f"Element : {element['name']}")
    print(f"Moles   : {moles}")
    print(f"Atoms   : {atoms:.3e}")


def atoms_to_mole():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    try:
        atoms = float(input("Number of atoms: "))
    except ValueError:
        print("❌ Invalid number.")
        return

    moles = atoms / AVOGADRO_NUMBER

    print("\n========== RESULT ==========")
    print(f"Element : {element['name']}")
    print(f"Atoms   : {atoms:.3e}")
    print(f"Moles   : {moles:.6f}")

def mass_to_atoms():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    try:
        mass = float(input("Mass (g): "))
    except ValueError:
        print("❌ Invalid number.")
        return

    molar_mass = element["atomic_weight"]

    moles = mass / molar_mass
    atoms = moles * AVOGADRO_NUMBER

    print("\n========== RESULT ==========")
    print(f"Element : {element['name']}")
    print(f"Mass    : {mass} g")
    print(f"Moles   : {moles:.6f} mol")
    print(f"Atoms   : {atoms:.3e}")

def atoms_to_mass():

    symbol = input("\nElement symbol: ")

    element = get_element(symbol)

    if not element:
        print("❌ Element not found.")
        return

    try:
        atoms = float(input("Number of atoms: "))
    except ValueError:
        print("❌ Invalid number.")
        return

    moles = atoms / AVOGADRO_NUMBER
    mass = moles * element["atomic_weight"]

    print("\n========== RESULT ==========")
    print(f"Element : {element['name']}")
    print(f"Atoms   : {atoms:.3e}")
    print(f"Moles   : {moles:.6f}")
    print(f"Mass    : {mass:.6f} g")

# ========= Main Menu =========

def main():

    while True:
        print("\n===================================")
        print("      CHEMISTRY CALCULATOR")
        print("===================================")
        print("1. Element Information")
        print("2. Mass → Mole")
        print("3. Mole → Mass")
        print("4. Mole → Atoms")
        print("5. Atoms → Mole")
        print("6. Mass → Atoms")
        print("7. Atoms → Mass")
        print("8. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_element_info()

        elif choice == "2":
            mass_to_mole()

        elif choice == "3":
            mole_to_mass()

        elif choice == "4":
            mole_to_atoms()

        elif choice == "5":
            atoms_to_mole()

        elif choice == "6":
            mass_to_atoms()

        elif choice == "7":
            atoms_to_mass()

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()