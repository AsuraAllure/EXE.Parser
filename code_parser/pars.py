from config import byte_in_line
from utility import convert_to_hex


total_length = 9 + 3*byte_in_line

def parse_code(source_file, output_file, size_code):
    count_byte = 0
    while size_code >= byte_in_line:
        line = to_full_hex(count_byte)+':\t'
        for _ in range(byte_in_line):
            line += formate_byte(source_file.read(1)) + '-'
        output_file.write(line[:-1]+'\n')
        size_code -= byte_in_line
        count_byte += byte_in_line
    if size_code > 0:
        line = to_full_hex(count_byte) + ':\t'
        for _ in range(size_code):
            line += formate_byte(source_file.read(1)) + '-'
        line = complete_line(line)
        output_file.write(line)


def complete_line(line):
    return line[:-1] + '?'*(total_length - len(line) + 1)


def formate_byte(_byte):
    _byte = convert_to_hex(_byte)[2:]
    if len(_byte) == 1:
        _byte = "0" + _byte
    return _byte.upper()


def to_full_hex(count_byte):
    count_byte = hex(count_byte)
    if len(count_byte) < 8:
        count_byte = count_byte[:2] +\
                     "0"*(8-len(count_byte)) +\
                     count_byte[2:]
    return count_byte.upper()
