from utility import convert_to_hex, get_raw


class Standart32:

    def __init__(self, file):
        self.magic = None
        self.major_linker_version = convert_to_hex(file.read(1))
        self.minor_linker_version = convert_to_hex(file.read(1))
        self.size_code = convert_to_hex(file.read(4))
        self.size_initialized_data = convert_to_hex(file.read(4))
        self.size_uninitialized_data = convert_to_hex(file.read(4))
        self.address_entry_point = convert_to_hex(file.read(4))
        self.base_code = convert_to_hex(file.read(4))
        self.base_data = convert_to_hex(file.read(4))

    def __str__(self):
        st = vars(self).items()
        res = "\n"
        for (spec, field) in st:
            res += get_raw(field, spec.lower() + ":", 1)
        return res


class Standart64:
    def __init__(self, file):
        self.magic = None
        self.major_linker_version = convert_to_hex(file.read(1))
        self.minor_linker_version = convert_to_hex(file.read(1))
        self.size_code = convert_to_hex(file.read(4))
        self.size_initialized_data = convert_to_hex(file.read(4))
        self.size_uninitialized_data = convert_to_hex(file.read(4))
        self.address_entry_point = convert_to_hex(file.read(4))
        self.base_code = convert_to_hex(file.read(4))

    def __str__(self):
        st = vars(self).items()
        res = ""
        for (spec, field) in st:
            res += get_raw(field, spec + ":", 1)
        return res
