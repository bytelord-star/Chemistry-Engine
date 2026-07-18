def generate_acid_name(parsed, acid_data):

    if acid_data is None:

        return {
            "name": "Unknown Acid",
            "iupac_name": "Unknown Acid",
            "common_name": "Unknown Acid"
        }

    return {
    "name": acid_data["common_name"] or acid_data["iupac_name"],
    "iupac_name": acid_data["iupac_name"],
    "common_name": acid_data["common_name"],
    }