from pathlib import Path
from typing import Any

from models.core.utils import load_json
from models.core.utils import save_json


# ==========================================================
# JSON Database
# ==========================================================

class JsonDatabase:
    """
    Generic JSON database manager.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(
        self,
        path: Path,
        formula_key: str = "formula",
        name_keys: list[str] | None = None,
    ):

        self.path = path

        self.formula_key = formula_key

        self.name_keys = name_keys or [

            "name",

            "iupac_name",

            "common_name",

        ]

        self.data = []

        self.reload()

    # ======================================================
    # Reload
    # ======================================================

    def reload(self) -> None:

        self.data = load_json(

            self.path,

            default=[]

        )

    # ======================================================
    # Save
    # ======================================================

    def save(self) -> None:

        save_json(

            self.path,

            self.data,

        )

    # ======================================================
    # Get All
    # ======================================================

    def all(self) -> list[dict]:

        return self.data

    # ======================================================
    # Count
    # ======================================================

    def count(self) -> int:

        return len(self.data)

    # ======================================================
    # Find by Formula
    # ======================================================

    def find_by_formula(
        self,
        formula: str,
    ) -> dict | None:

        formula = formula.strip().lower()

        for item in self.data:

            value = str(

                item.get(

                    self.formula_key,

                    "",

                )

            ).lower()

            if value == formula:

                return item

        return None

    # ======================================================
    # Find by Name
    # ======================================================

    def find_by_name(
        self,
        name: str,
    ) -> dict | None:

        name = name.strip().lower()

        for item in self.data:

            for key in self.name_keys:

                value = str(

                    item.get(

                        key,

                        "",

                    )

                ).lower()

                if value == name:

                    return item

        return None

    # ======================================================
    # Exists
    # ======================================================

    def exists(
        self,
        formula: str,
    ) -> bool:

        return (

            self.find_by_formula(

                formula,

            )

            is not None

        )

    # ======================================================
    # Filter
    # ======================================================

    def filter(
        self,
        key: str,
        value: Any,
    ) -> list[dict]:

        return [

            item

            for item in self.data

            if item.get(key) == value

        ]

    # ======================================================
    # Append
    # ======================================================

    def append(
        self,
        item: dict,
    ) -> None:

        self.data.append(item)

        self.save()

    # ======================================================
    # Update
    # ======================================================

    def update(
        self,
        formula: str,
        new_data: dict,
    ) -> bool:

        compound = self.find_by_formula(

            formula,

        )

        if compound is None:

            return False

        compound.update(

            new_data,

        )

        self.save()

        return True

    # ======================================================
    # Delete
    # ======================================================

    def delete(
        self,
        formula: str,
    ) -> bool:

        formula = formula.strip().lower()

        original_size = len(

            self.data,

        )

        self.data = [

            item

            for item in self.data

            if str(

                item.get(

                    self.formula_key,

                    "",

                )

            ).lower()

            != formula

        ]

        if len(self.data) == original_size:

            return False

        self.save()

        return True

    # ======================================================
    # Clear
    # ======================================================

    def clear(self) -> None:

        self.data.clear()

        self.save()

    # ======================================================
    # Magic Methods
    # ======================================================

    def __len__(self):

        return len(

            self.data,

        )

    def __iter__(self):

        return iter(

            self.data,

        )