from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "DATA"

ELEMENTS_PATH = DATA_DIR / "elements.json"
ACIDS_PATH = DATA_DIR / "acid.json"
BASES_PATH = DATA_DIR / "bases.json"
COMPOUNDS_PATH = DATA_DIR / "compounds.json"
COMMON_NAMES_PATH = BASE_DIR / "DATA" / "common_names.json"
POLYATOMIC_IONS_PATH = DATA_DIR / "polyatomic_ions.json"
