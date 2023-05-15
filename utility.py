from config import left_bound_raw


def get_raw(field, spec, level):
    value = (field
             .upper()
             .replace("X", 'x', 1))
    spec = " ".join([x.lower().title() for x in spec.split('_')])
    spec = '    '*level + spec
    return addition_space(spec) + value + "\n"


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
    return addition_space(spec) + value + "\n"




def addition_space(string):
    if len(string) < left_bound_raw:
        return string + " " * (left_bound_raw - len(string))


def convert_to_hex(b):
    return hex(int.from_bytes(b, "little"))
