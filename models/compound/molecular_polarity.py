def predict_polarity(
        bond_type,
        formula
):


    if bond_type == "Nonpolar Covalent":

        return "Nonpolar"


    if bond_type == "Polar Covalent":


        if formula in [
            "CO2",
            "CH4"
        ]:

            return "Nonpolar"


        return "Polar"



    if bond_type == "Ionic":

        return "Ionic Compound"



    return "Unknown"