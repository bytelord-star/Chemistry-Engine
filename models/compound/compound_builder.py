def build_compound(

        parsed,

        molar_mass,

        bond_type,

        molecular_polarity,

        classification,

        acid_data=None

):

    return {

        # ==========================
        # Formula Information
        # ==========================

        "formula": parsed["formula"],

        "elements": parsed["atoms"],

        "groups": parsed["groups"],

        "polyatomic_ions": parsed["polyatomic_ions"],

        "total_atoms": parsed["total_atoms"],

        # ==========================
        # Physical Properties
        # ==========================

        "molar_mass": molar_mass,

        # ==========================
        # Chemical Properties
        # ==========================

        "bond_type": bond_type,

        "molecular_polarity": molecular_polarity,

        "classification": classification,

        "acid_data": acid_data

    }