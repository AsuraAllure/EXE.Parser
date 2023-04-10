from COFF.NotPEFormatException import NotPeFormat
from COFF.Header import COFFHeader
from utility import convert_to_hex
from COFF.Substructures.Machine import Machine
from COFF.Substructures.TimeDateStamp import TimeDateStamp
from COFF.Substructures.Characteristic import Characteristic


class COFFParser:

    def __init__(self, file):
        self.file = file
        self.header = COFFHeader()

    def build_header(self):
        self.header.empty = False
        data = self.file.read(4)
        if data != b"PE\x00\x00":
            raise NotPeFormat
        self.header.fields["mch"] = Machine(convert_to_hex(self.file.read(2)))
        self.header.fields["nsec"] = convert_to_hex(self.file.read(2))
        self.header.fields["tds"] = TimeDateStamp(self.file.read(4))
        self.header.fields["ptr"] = convert_to_hex(self.file.read(4))
        self.header.fields["nsb"] = convert_to_hex(self.file.read(4))
        self.header.fields["soh"] = int(convert_to_hex(self.file.read(2)), 16)
        self.header.fields["char"] = Characteristic(int(convert_to_hex(self.file.read(2)), 16))
        return self.header

    def get_header(self):
        if self.header.empty:
            self.build_header()
        return self.header
