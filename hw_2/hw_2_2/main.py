import sys

from simple_latex_generator import save_latex_to_file, LatexDocument, LatexPackage, LatexGraphics, tex_to_pdf

if __name__ == "__main__":
    # photo_path = 'hw_2/test/kot-van-dam.png'
    #
    # result_dir_path = "hw_2/artifacts/2.2"
    # file_path = result_dir_path + "/hw_2_2.tex"

    args = sys.argv[1:]
    file_path = args[0]
    photo_path = args[1]
    result_dir_path = args[2]

    save_latex_to_file(
        str(
            LatexDocument(
                "article",
                [
                    LatexPackage("babel", ["russian", "english"]),
                    LatexPackage("graphicx")
                ],
                str(LatexGraphics(photo_path, height='10cm'))
            )
        ), file_path
    )

    tex_to_pdf(file_path, result_dir_path)
