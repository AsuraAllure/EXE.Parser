from MSDOS.Header import MSDOSHeader
from MSDOS.NotExeException import NotExeFileException

class MSDOSParser:
    def __init__(self, file):
        self.file = file
        self.header = MSDOSHeader()

    def build_header(self):
        self.header.empty = False

        data = self.file.read(2)
        if data != b'MZ':
            raise NotExeFileException
        self.header.fields["magic"] = data
        self.header.fields["cblp"] = self.file.read(2)
        self.header.fields["cp"] = self.file.read(2)
        self.header.fields["crlc"] = self.file.read(2)
        self.header.fields["cparhdr"] = self.file.read(2)
        self.header.fields["minalloc"] = self.file.read(2)
        self.header.fields["maxalloc"] = self.file.read(2)
        self.header.fields["ss"] = self.file.read(2)
        self.header.fields["sp"] = self.file.read(2)
        self.header.fields["csum"] = self.file.read(2)
        self.header.fields["ip"] = self.file.read(2)
        self.header.fields["cs"] = self.file.read(2)
        self.header.fields["lfarlc"] = self.file.read(2)
        self.header.fields["ovno"] = self.file.read(2)
        self.file.seek(self.file.tell()+8)
        self.header.fields["oemid"] = self.file.read(2)
        self.header.fields["oeminfo"] = self.file.read(2)
        self.file.seek(self.file.tell() + 20)
        self.header.fields["pe_offset"] = self.file.read(2)


    def get_header(self):
        if self.header.empty:
            self.build_header()
        return self.header
