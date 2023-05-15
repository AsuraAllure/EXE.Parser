from MSDOS.header import MSDOSHeader
from MSDOS.not_exe_exception import NotExeFileException
from utility import convert_to_hex

class MSDOSParser:
    def __init__(self, file):
        self.file = file
        self.header = MSDOSHeader()

    def build_header(self):
        self.header.empty = False

        data = self.file.read(2)
        if data != b'MZ':
            raise NotExeFileException
        self.header.magic = convert_to_hex(data)
        self.header.cblp = convert_to_hex(self.file.read(2))
        self.header.cp = convert_to_hex(self.file.read(2))
        self.header.crlc = convert_to_hex(self.file.read(2))
        self.header.cparhdr = convert_to_hex(self.file.read(2))
        self.header.minalloc = convert_to_hex(self.file.read(2))
        self.header.maxalloc = convert_to_hex(self.file.read(2))
        self.header.ss = convert_to_hex(self.file.read(2))
        self.header.sp = convert_to_hex(self.file.read(2))
        self.header.csum = convert_to_hex(self.file.read(2))
        self.header.ip = convert_to_hex(self.file.read(2))
        self.header.cs = convert_to_hex(self.file.read(2))
        self.header.lfarlc = convert_to_hex(self.file.read(2))
        self.header.ovno = convert_to_hex(self.file.read(2))
        self.file.seek(self.file.tell()+8)
        self.header.oemid = convert_to_hex(self.file.read(2))
        self.header.oeminfo = convert_to_hex(self.file.read(2))
        self.file.seek(self.file.tell() + 20)
        self.header.pe_offset = convert_to_hex(self.file.read(2))

    def get_header(self):
        if self.header.empty:
            self.build_header()
        return self.header
