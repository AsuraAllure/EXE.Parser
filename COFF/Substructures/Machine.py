from functools import reduce


class Machine:
    def __init__(self, code):
        self.value = None
        self.map = dict()
        filename = ("C:\\Users\\Пользователь\\Desktop\\Предметы" +
                    "\\Питон\\EXE\\COFF\\Substructures\\MachineMapping.txt")
        with open(filename, 'r') as file:
            for line in file:
                line = line.split()
                key = hex(int(line[0], 16))
                self.map[key] = reduce(lambda x, y: x + " " + y, line[1:])
        self.value = self.map.get(code)

    def __str__(self):
        return self.value


if __name__ == "__main__":
    assert (Machine("0").value != "The content of this field is assumed to be applicable to any machine type")
    assert (Machine("0x0").value == "The content of this field is assumed to be applicable to any machine type")
    assert (Machine("0x184").value == "Alpha AXP, 32-bit address space")
    assert (Machine("0x123").value is None)
    assert (Machine("0x8664").value is not None)
