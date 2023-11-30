from LatexGenerator import LatexPackage, LatexDocument, LatexTable, save_latex_to_file

if __name__ == "__main__":
    save_latex_to_file(
        str(
            LatexDocument(
                "article",
                [LatexPackage("babel", ["russian", "english"])],
                str(LatexTable(data=[['col1', 'col2'], ['1', '2'], ['3', '4']]))
            )
        ), "../artifacts/2.1/hw_1_1.tex"
    )
