from COFF.not_PE_format_exception import NotPeFormat
from COFF.header import COFFHeader
from utility import convert_to_hex
from COFF.substructures.machine import Machine
from COFF.substructures.time_date_stamp import TimeDateStamp
from COFF.substructures.characteristic import Characteristic


class COFFParser:

    def __init__(self, file):
        self.file = file
        self.header = COFFHeader()

    def build_header(self):
        self.header.empty = False
        data = self.file.read(4)
        if data != b"PE\x00\x00":
            raise NotPeFormat
        self.header.mch = Machine(convert_to_hex(self.file.read(2)))
        self.header.nsec = convert_to_hex(self.file.read(2))
        self.header.tds = TimeDateStamp(self.file.read(4))
        self.header.ptr = convert_to_hex(self.file.read(4))
        self.header.nsb = convert_to_hex(self.file.read(4))
        self.header.soh = convert_to_hex(self.file.read(2))
        self.header.char = Characteristic(int(convert_to_hex(self.file.read(2)), 16))
        return self.header

    def get_header(self):
        if self.header.empty:
            self.build_header()
        return self.header

