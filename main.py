


from models.core.chemistry_core import analyze

from models.core.report_generator import (
    element_report,
    compound_report,
    reaction_report
)





def show_result(result):

    if not result["success"]:
        print(result["message"])
        return

    if result["type"] == "element":
        print(element_report(result["data"]))

    elif result["type"] == "compound":
        print(compound_report(result["data"]))

    elif result["type"] == "reaction":
        print(reaction_report(result["data"]))


def main():

    print("========== Chemistry Engine ==========")

    while True:

        query = input("\nSearch (exit): ")

        if query.lower() == "exit":
            break

        result = analyze(query)

        show_result(result)


if __name__ == "__main__":
    main()