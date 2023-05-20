from config import left_bound_raw


def read_file_name_rva_hex(file, rva, rva_calc):
    offset_name = rva_calc.resolve(int(rva, 16))
    cur_positions = file.tell()
    file.seek(offset_name)
    name = ''
    b = file.read(1)
    while b != b'\x00' and b != b'@':
        name += chr(int(convert_to_hex(b), 16))
        b = file.read(1)
    file.seek(cur_positions)
    return name


def get_raw_lower_value(field, spec, level):
    spec = " ".join([x.lower().title() for x in spec.split('_')])
    spec = '    '*level + spec
    return addition_space(spec+":") + field + "\n"

def get_raw(field, spec, level):
    value = (field
             .upper()
             .replace("X", 'x', 1))
    spec = " ".join([x.lower().title() for x in spec.split('_')])
    spec = '    '*level + spec
    return addition_space(spec+":") + value + "\n"


def get_raw_flags(field, spec, level):
    value = (field
             .upper()
             .replace("X", 'x', 1))
    spec = " ".join([x.title() for x in spec.split('_')])
    spec = '    '*level + spec

    if value != "0x0":
        value = "1"
    else:
        value = "0"
    return addition_space(spec+":") + value + "\n"




def addition_space(string):
    if len(string) < left_bound_raw:
        return string + " " * (left_bound_raw - len(string))


def convert_to_hex(b):
    return hex(int.from_bytes(b, "little"))
