from utility import convert_to_hex, get_raw, get_raw_lower_value, read_file_name_rva_hex
from COFF.substructures.time_date_stamp import TimeDateStamp


class ImportTableParser:
    def __init__(self, file, size_table, rva_calculator, magic):
        self.directory_table = []
        count_readied = 20
        import_descriptor_bytes = file.read(20)
        null_descriptor = b'\x00' * 20
        while import_descriptor_bytes != null_descriptor and count_readied <= size_table:
            self.directory_table.append(ImportDescriptor(import_descriptor_bytes, rva_calculator, file, magic))
            import_descriptor_bytes = file.read(20)
            count_readied += 20

    def __str__(self):
        res = ""
        for x in self.directory_table:
            res += str(x) + '\n'
        return res

class ImportDescriptor:
    def __init__(self, data, rva_calc, file, magic):

        self.import_lookup_table = self.fill_lookup(data[:4], rva_calc, file, magic)
        self.time_date_stamp = TimeDateStamp(data[4:8])
        self.forwarded_chain = convert_to_hex(data[8:12])
        self.name_DLL = read_file_name_rva_hex(file, convert_to_hex(data[12:16]), rva_calc)
        self.thunk_table = self.fill_lookup(data[16:20], rva_calc, file, magic)

    def fill_lookup(self, hex_rva, rva_calc, file, magic):
        rva_lookup_table = convert_to_hex(hex_rva)
        if rva_lookup_table == '0x0':
            return []
        offset_lookup_table = rva_calc.resolve(int(rva_lookup_table, 16))
        cur_positions = file.tell()
        file.seek(offset_lookup_table)

        raw = convert_to_hex(file.read(4))

        tables = []

        while raw != '0x0':
            import_lookup_data = int(raw, 16)

            import_lookup_table = LookupTable()
            if magic == '0x10b':
                import_lookup_table.flag = int(bool(import_lookup_data & 0x80000000))
            else:
                import_lookup_table.flag = int(bool(import_lookup_data & 0x8000000000000000))

            if import_lookup_table.flag:
                import_lookup_table.ordinal = hex(import_lookup_data & 0xffff)
            else:
                import_lookup_table.name_functions = read_file_name_rva_hex(
                    file,
                    hex((import_lookup_data & 0x7fffffff)+2),
                    rva_calc
                )

            tables.append(import_lookup_table)
            raw = convert_to_hex(file.read(4))

        file.seek(cur_positions)
        return tables

    def __str__(self):
        res = ""
        for (field, value) in vars(self).items():
            if field == "import_lookup_table":
                res += "Import Lookup Table:\n"
                if len(self.import_lookup_table) == 0:
                    res += "\tNo Structures\n"
                elif len(self.thunk_table) != 0:
                    res += "\tSee Thunk Table\n"
                else:
                    for x in self.import_lookup_table:
                        res += get_raw_lower_value(str(x), "Lookup Descriptor", 1)
            elif field == "thunk_table":
                res += "Thunk Table:\n"
                if len(self.thunk_table) == 0:
                    res += "\tNo Structures\n"
                else:
                    for x in self.thunk_table:
                        res += get_raw_lower_value(str(x), "Lookup Descriptor", 1)
            else:
                res += get_raw(str(value), field, 0)
        return res


class LookupTable:
    def __init__(self):
        self.flag = None

    def __str__(self):
        res = "\n"
        if self.flag is None:
            return res + "\tNo structures"

        for (spec, field) in vars(self).items():
            res += get_raw_lower_value(str(field), spec.lower(), 2)

        return res[:-1]
