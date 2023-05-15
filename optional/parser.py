from optional.header import *
from optional.substructures.data import *
from optional.substructures.standarts import *
from optional.substructures.windows_specific import *
from optional.errors import *
from utility import convert_to_hex


class OptionalParser:
    def __init__(self, file, size_header):
        self.size_header = size_header
        self.file = file
        self.header = OptionalHeader()

    def build_header(self):
        self.header.empty = False
        magic = self.file.read(2)
        if magic == PE32_MAGIC:
            self.header.standart = Standart32(self.file)
            self.header.standart.magic = convert_to_hex(magic)
            self.header.windows_specific = WindowsSpecific32Fields(self.file)
            self.header.data = Data(self.file.read(self.size_header - 96))
        elif magic == PE64_MAGIC:
            self.header.standart = Standart64(self.file.read(22))
            self.header.standart.magic = convert_to_hex(magic)
            self.header.windows_specific = WindowsSpecific64Fields(self.file)
            self.header.data = Data(self.file.read(self.size_header - 112))
        else:
            raise OptionalHeaderParseError("Magic number unknown: " + convert_to_hex(magic))

    def get_header(self):
        if self.header.empty:
            self.build_header()
        return self.header
