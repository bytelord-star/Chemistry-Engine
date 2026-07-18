from models.core.chemistry_core import analyze
from models.core.report_generator import (
    element_report,
    compound_report,
    reaction_report,
)


# ==========================================================
# Show Result
# ==========================================================

def show_result(result):

    if not result.get("success", False):
        print(result.get("message", "Unknown error"))
        return

    report_functions = {
        "element": element_report,
        "compound": compound_report,
        "reaction": reaction_report,
    }

    report = report_functions.get(result["type"])

    if report:
        print(report(result["data"]))
    else:
        print("Unknown result type.")


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 45)
    print("        Chemistry Engine")
    print("=" * 45)

    while True:

        query = input("\nSearch (exit): ").strip()

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        if not query:
            continue

        result = analyze(query)

        show_result(result)


if __name__ == "__main__":
    main()