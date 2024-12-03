import math

cmp_operations = {
    "ifeq": "__eq__",
    "ifne": "__ne__",
    "ifgt": "__gt__",
    "ifge": "__ge__",
    "iflt": "__lt__",
    "ifle": "__le__",
}

ar_operations = {
    "add": "__add__",
    "sub": "__sub__",
    "mul": "__mul__",
    "div": "__truediv__",
}


class ASM_Interpreter:

    def __init__(self):
        self.program = []
        self.variables = {}
        self.labels = {}
        self.curr_line = 0

    def _to_float(self, value):
        try:
            return float(value)
        except ValueError:
            return 0.0

    def _do_operation(self, op, x1, x2):
        try:
            return getattr(self.variables.get(x1, 0.0), ar_operations.get(op))(
                self.variables.get(x2, 0.0)
            )
        except ZeroDivisionError:
            return math.inf

    def _do_compare(self, cmp, x1, x2):
        return getattr(self.variables.get(x1, 0.0), cmp_operations.get(cmp))(
            self.variables.get(x2, 0.0)
        )

    def _read_program(self):
        signs = []
        while True:
            try:
                line = input().strip()
            except EOFError:
                break

            if not line:
                continue

            if ":" in line:
                label_name, command = line.split(":")
                label_name = label_name.strip()
                command = command.strip() if command else None
                self.labels[label_name] = len(self.program) - 1
                if command:
                    self.program.append(command)
                else:
                    self.program.append("")
            if any(
                elem in line
                for elem in ("ifeq", "ifne", "ifgt", "ifge", "iflt", "ifle")
            ):
                if len(line.split()) == 4 or len(line.split()) == 5 and ":" in line:
                    signs.append(line.split()[-1])
            self.program.append(line)
        for sign in signs:
            if sign not in self.labels:
                return False
        return True

    def _interpret_program(self):
        while self.curr_line < len(self.program):
            line = self.program[self.curr_line].strip()
            match line.split():
                case ["stop"]:
                    return
                case ["store", str(x), str(var)]:
                    self.variables[var] = self._to_float(x)
                case [
                    ("add" | "sub" | "div" | "mul") as op,
                    str(x1),
                    str(x2),
                    str(store),
                ]:
                    self.variables[store] = self._do_operation(op, x1, x2)
                case [
                    ("ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle") as cmp,
                    str(x1),
                    str(x2),
                    str(label),
                ]:
                    if self._do_compare(cmp, x1, x2):
                        self.curr_line = self.labels[label]
                case ["out", str(x1)]:
                    print(self.variables[x1])
                case default:
                    pass
            self.curr_line += 1

    def run(self):
        if self._read_program():
            self._interpret_program()


asm = ASM_Interpreter()
asm.run()
