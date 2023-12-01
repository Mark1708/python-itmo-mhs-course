import os
import subprocess


def save_latex_to_file(latex_code, filename='output.tex'):
    with open(filename, 'w') as file:
        file.write(latex_code)


def tex_to_pdf(file_path, output_dir):
    file_name = file_path.split(os.sep)[-1].split('.')[0]
    subprocess.run(['pdflatex', '-shell-escape', '-interaction=nonstopmode',
                    f"-output-directory={output_dir}", file_path])

    os.unlink(f"{output_dir}/{file_name}.aux")
    os.unlink(f"{output_dir}/{file_name}.log")