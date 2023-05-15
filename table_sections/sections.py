from table_sections.characteristics import Characteristics
from utility import convert_to_hex, get_raw


class Section:
    def __init__(self, data):
        self.name = data[:8].decode('utf-8').replace(b'\x00'.decode("utf-8"), '')
        self.virtual_size = convert_to_hex(data[8:12])
        self.virtual_address = convert_to_hex(data[12:16])
        self.size_row_data = convert_to_hex(data[16:20])
        self.pointer_raw_data = convert_to_hex(data[20:24])
        self.pointer_relocations = convert_to_hex(data[24:28])
        self.pointer_line_numbers = convert_to_hex(data[28:32])
        self.count_relocation = convert_to_hex(data[32:34])
        self.count_line_numbers = convert_to_hex(data[34:36])
        self.characteristics = Characteristics(int(convert_to_hex(data[36:]), 16))

    def __str__(self):
        st = vars(self).items()
        res = "Section:\n"
        for (spec, field) in st:
            if spec != "characteristics":
                res += get_raw(field, spec+":", 1)
        return res + str(self.characteristics)

