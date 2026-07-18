from models.core.element_manager import (
    get_element,
    get_atomic_mass,
    get_element_name,
)

AVOGADRO_NUMBER = 6.02214076e23

def mass_to_mole_value(symbol, mass):

    atomic_mass = get_atomic_mass(symbol)

    if atomic_mass is None:
        return None

    return mass / atomic_mass

def mole_to_mass_value(symbol, mole):

    atomic_mass = get_atomic_mass(symbol)

    if atomic_mass is None:
        return None

    return mole * atomic_mass

def mole_to_atoms_value(mole):

    return mole * AVOGADRO_NUMBER

def atoms_to_mole_value(atoms):

    return atoms / AVOGADRO_NUMBER

def mass_to_atoms_value(symbol, mass):

    mole = mass_to_mole_value(symbol, mass)

    if mole is None:
        return None

    return mole_to_atoms_value(mole)

def atoms_to_mass_value(symbol, atoms):

    mole = atoms_to_mole_value(atoms)

    return mole_to_mass_value(symbol, mole)