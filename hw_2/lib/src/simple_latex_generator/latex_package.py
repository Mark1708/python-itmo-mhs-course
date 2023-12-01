class LatexPackage:

    def __init__(self, package_name, package_args=None):
        self.package_name = package_name
        self.package_args = [] if package_args is None else package_args

    def add_arg(self, arg):
        self.package_args.append(arg)

    def __str__(self):
        return (f"\\usepackage"
                f"{len(self.package_args) == 0 if '' else '[' + ','.join(self.package_args) + ']'}"
                f"{'{' + self.package_name + '}'}")
