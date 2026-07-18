# =========================
# Element Report
# =========================

def element_report(element):


    return f"""

========== ELEMENT INFORMATION ==========


Name:
{element.get('name')}


Symbol:
{element.get('symbol')}


Atomic Number:
{element.get('atomic_number')}


Atomic Weight:
{element.get('atomic_weight')}


Category:
{element.get('category')}


Group:
{element.get('group')}


Period:
{element.get('period')}


Valence:
{element.get('valence')}


Oxidation States:
{element.get('oxidation_states')}

"""





# =========================
# Compound Report
# =========================

def compound_report(compound):

    return f"""
========== COMPOUND INFORMATION ==========

Formula:
{compound.get("formula")}

Name:
{compound.get("name")}

IUPAC Name:
{compound.get("iupac_name")}

Common Name:
{compound.get("common_name")}

Elements:
{compound.get("elements")}

Total Atoms:
{compound.get("total_atoms")}

Molar Mass:
{compound.get("molar_mass")} g/mol

Bond Type:
{compound.get("bond_type")}

Molecular Polarity:
{compound.get("molecular_polarity")}

Classification:
{compound.get("classification")}
"""





# =========================
# Reaction Report
# =========================

def reaction_report(result):


    text = """

========== REACTION ANALYSIS ==========


"""


    text += f"""

Reactants atoms:
{result.get('reactants_atoms')}


Products atoms:
{result.get('products_atoms')}


Balanced:
{result.get('balanced')}

"""



    if not result.get("balanced"):


        text += f"""

Suggested balanced reaction:

{result.get('suggestion')}

"""



    return text