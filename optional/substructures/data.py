from utility import convert_to_hex, addition_space

class Data:
    def __init__(self, byt):
        self.byt = byt
        self.directories = []
        while len(byt) != 0:
            ddir = ImageDataDirectory(byt[:8])
            byt = byt[8:]
            self.directories.append(ddir)

    def __str__(self):
        st = "\n"
        for x in self.directories:
            st += str(x)+"\n"
        return st


class ImageDataDirectory:
    def __init__(self, bytes):
        self.virtual_address = convert_to_hex(bytes[:4])
        self.size = convert_to_hex(bytes[4:])

    def get_raw(self, field, spec):
        value = (field
                 .upper()
                 .replace("X", 'x', 1))
        return addition_space(spec) + value + "\n"

    def __str__(self):
        st ="\tDIR:\n" +  self.get_raw(self.virtual_address, "    Virtual Address:")
        st += self.get_raw(self.size, "    Size:")[:-1]
        return st

