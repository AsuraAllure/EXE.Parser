from config import left_bound_raw


def addition_space(string):
    if len(string) < left_bound_raw:
        return string + " " * (left_bound_raw - len(string))


def convert_to_hex(b):
    return hex(int.from_bytes(b, "little"))
