n_line = "\n"


class LatexPackage:

    def __init__(self, package_name, package_args=None):
        self.package_name = package_name
        self.package_args = package_args is None if [] else package_args

    def add_arg(self, arg):
        self.package_args.append(arg)

    def __str__(self):
        return (f"\\usepackage"
                f"{len(self.package_args) == 0 if '' else '[' + ','.join(self.package_args) + ']'}"
                f"{'{' + self.package_name + '}'}")


class LatexTable:

    def __init__(self, header=None, data=None, first_header=True):
        self.header = header is None if [] else header
        self.data = data is None if [] else data
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


class LatexDocument:

    def __init__(self, document_class, packages, content):
        self.document_class = document_class
        self.packages = packages
        self.content = content

    def __str__(self):
        return (
            f"\documentclass{'{' + self.document_class + '}'}{n_line}"
            f"{len(self.packages) == 0 if '' else n_line.join([str(package) for package in self.packages])}{n_line}"
            "\\begin{document}"
            f"{n_line}{self.content}{n_line}"
            "\\end{document}"
        )


def save_latex_to_file(latex_code, filename='output.tex'):
    with open(filename, 'w') as file:
        file.write(latex_code)
