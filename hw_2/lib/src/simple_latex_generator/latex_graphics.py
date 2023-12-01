import os

from .latex_constants import n_line


class LatexGraphics:

    def __init__(self, graphics_path, height=None, width=None, caption=None):
        if graphics_path is None:
            raise Exception("У самурая нет цели, есть только путь. Так вот у картинки тоже должен быть путь!")
        self.graphics_path = graphics_path
        self.height = height
        self.width = width
        self.caption = graphics_path.split(os.sep)[-1]

    def __str__(self):
        sizes = []
        caption_tex = ''
        if self.height is not None:
            sizes.append('height=' + self.height)
        if self.width is not None:
            sizes.append('width=' + self.width)
        if self.caption is not None:
            caption_tex += ("\\vspace{9 mm}" + f"{n_line}\caption{'{' + self.caption + '}'}")

        return (
            "\\begin{figure}[ht!]"
            f"{n_line}"
            "\\centering"
            f"{n_line}"
            "\includegraphics"
            f"{len(sizes) == 0 if '' else '[' + ', '.join(sizes) + ']'}"
            f"{'{' + self.graphics_path + '}' + n_line}"
            f"{caption_tex}{n_line}"
            "\\end{figure}"
        )
