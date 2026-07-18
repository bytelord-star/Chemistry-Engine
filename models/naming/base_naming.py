def generate_base_name(parsed, base_data):

    if base_data is None:

        return {
            "name": "Unknown Base",
            "iupac_name": "Unknown Base",
            "common_name": "Unknown Base"
        }

    return {
    "name": base_data["common_name"] or base_data["iupac_name"],
    "iupac_name": base_data["iupac_name"],
    "common_name": base_data["common_name"],
}