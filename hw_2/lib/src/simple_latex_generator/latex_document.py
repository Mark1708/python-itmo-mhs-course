from .latex_constants import n_line


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
