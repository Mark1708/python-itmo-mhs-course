from .latex_constants import n_line


class LatexTable:

    def __init__(self, header=None, data=None, first_header=True):
        self.header = [] if header is None else header
        self.data = [] if data is None else data
        self.first_header = first_header

    def __str__(self):
        if len(self.data) == 0:
            raise Exception("Данные пустые")

        if not self.first_header:
            self.data.insert(0, self.header)

        def row_to_latex(row):
            return " & ".join(row)

        header = row_to_latex(self.data[0])
        rows = "\n".join(map(lambda row: row_to_latex(row) + " \\\\", self.data[1:]))

        return (
            f"\\begin{{tabular}}{{|{'|'.join(['c'] * len(self.data[0]))}|}}{n_line}"
            f"\\hline{n_line}"
            f"{header} \\\\{n_line}"
            f"\\hline{n_line}"
            f"{rows}{n_line}"
            f"\\hline{n_line}"
            f"\\end{{tabular}}{n_line}"
        )
