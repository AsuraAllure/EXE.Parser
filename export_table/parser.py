from COFF.substructures.time_date_stamp import TimeDateStamp
from utility import convert_to_hex, get_raw, get_raw_lower_value, read_file_name_rva_hex


class ExportTableParser:
    def __init__(self, file, size_export_table, rva_calculator):
        base_export_table = file.tell()

        self.export_directory_table = ExportDirectoriesTable(file, rva_calculator)
        offset_address_table = rva_calculator.resolve(int(self.export_directory_table.export_address_table_rva, 16))
        file.seek(offset_address_table)

        self.export_address_table = ExportAddressTable(
            file,
            int(self.export_directory_table.address_table_entries, 16),
            base_export_table,
            size_export_table,
            rva_calculator
        )

        offset_name_pointer_table = rva_calculator.resolve(int(self.export_directory_table.name_pointer_rva, 16))
        file.seek(offset_name_pointer_table)
        name_pointer_table = NamePointerTable(file, int(self.export_directory_table.number_name_pointers, 16))

        offset_ordinal_table = rva_calculator.resolve(int(self.export_directory_table.ordinal_table_rva, 16))
        file.seek(offset_ordinal_table)

        self.ordinal_table = OrdinalTable(file, int(self.export_directory_table.number_name_pointers, 16))
        self.export_name_table = ExportNameTable(file, name_pointer_table.names_rva, rva_calculator)

    def __str__(self):
        res = "\tExport Table:\n"
        for (spec, field) in vars(self).items():
            res += get_raw_lower_value(str(field), spec.lower(), 0)
        return res

class ExportNameTable:
    def __init__(self, file,  name_table, rva_calc):
        self.names = []
        for i in name_table:
            name_export_functions = read_file_name_rva_hex(file, i, rva_calc)
            self.names.append(name_export_functions)

    def __str__(self):
        res = "\n"
        for x in self.names:
            res += get_raw_lower_value(x, "Name", 1)
        return res




class OrdinalTable:
    def __init__(self, file, size):
        self.ordinals = []
        for x in range(size):
            self.ordinals.append(convert_to_hex(file.read(2)))

    def __str__(self):
        res = "\n"
        for x in self.ordinals:
            res += get_raw(x, "Index", 1)
        return res


class NamePointerTable:
    def __init__(self, file, count_names):
        self.names_rva = []

        for x in range(count_names):
            name = convert_to_hex(file.read(4))
            self.names_rva.append(name)

    def __str__(self):
        res = "\n"
        for x in self.names_rva:
            res += get_raw(x, "Addres", 1)
        return res


class ExportAddressTable:
    def __init__(self, file, count_functions, base, size, rva_calc):
        self.descriptors = []
        for x in range(count_functions):
            rva = convert_to_hex(file.read(4))
            if rva == '0x0':
                self.descriptors.append((rva, "ZERO"))
            else:
                offset = rva_calc.resolve(int(rva, 16))
                if base <= offset < base+size:
                    self.descriptors.append((rva, True))
                else:
                    self.descriptors.append((rva, False))

    def __str__(self):
        res = '\n'
        for x, type in self.descriptors:
            if type == "ZERO":
                res += get_raw(x+" (Name not defined)", "Addres code", 1)
            elif type:
                res += get_raw(x+" (forwarded)", "Addres code", 1)
            else:
                res += get_raw(x + " (direct export)", "Addres code", 1)
        return res


class ExportDirectoriesTable:
    def __init__(self, file, rva_calculator):
        self.flags = convert_to_hex(file.read(4))
        self.time_date_stamp = str(TimeDateStamp(file.read(4)))
        self.major_version = convert_to_hex(file.read(2))
        self.minor_version = convert_to_hex(file.read(2))
        self.name_export_dll = read_file_name_rva_hex(file, convert_to_hex(file.read(4)), rva_calculator )
        self.ordinal_base = convert_to_hex(file.read(4))
        self.address_table_entries = convert_to_hex(file.read(4))
        self.number_name_pointers = convert_to_hex(file.read(4))
        self.export_address_table_rva = convert_to_hex(file.read(4))
        self.name_pointer_rva = convert_to_hex(file.read(4))
        self.ordinal_table_rva = convert_to_hex(file.read(4))

    def __str__(self):
        res = "\n"
        for (field, value) in vars(self).items():
            res += get_raw(value, field.lower(), 1)
        return res