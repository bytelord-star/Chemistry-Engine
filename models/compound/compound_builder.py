def build_compound(
    parsed,
    name_data,
    molar_mass,
    bond_type,
    molecular_polarity,
    classification,
    acid_data=None,
    base_data=None
):

    return {

        "formula": parsed["formula"],

        "name": name_data["name"],

        "iupac_name": name_data["iupac_name"],

        "common_name": name_data["common_name"],

        "elements": parsed["atoms"],

        "groups": parsed["groups"],

        "polyatomic_ions": parsed["polyatomic_ions"],

        "total_atoms": parsed["total_atoms"],

        "molar_mass": molar_mass,

        "bond_type": bond_type,

        "molecular_polarity": molecular_polarity,

        "classification": classification,

        "acid_data": acid_data,

        "base_data": base_data

    }