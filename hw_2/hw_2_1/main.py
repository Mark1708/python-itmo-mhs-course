import sys

from simple_latex_generator import save_latex_to_file, LatexDocument, LatexPackage, LatexTable, tex_to_pdf

if __name__ == "__main__":
    args = sys.argv[1:]
    # result_dir_path = "hw_2/artifacts/2.1"
    # file_path = result_dir_path + "/hw_2_1.tex"
    file_path = args[0]
    result_dir_path = args[1]

    save_latex_to_file(
        str(
            LatexDocument(
                "article",
                [LatexPackage("babel", ["russian", "english"])],
                str(LatexTable(data=[['col1', 'col2'], ['1', '2'], ['3', '4']]))
            )
        ), file_path
    )

    tex_to_pdf(file_path, result_dir_path)
