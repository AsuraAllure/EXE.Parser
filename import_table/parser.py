from utility import convert_to_hex
from COFF.substructures.time_date_stamp import TimeDateStamp

class ImportTableParser:
    def __init__(self, data):
        self.directory_table = DirectoryTable(data[:20])


class DirectoryTable:
    def __init__(self, data):
        self.import_lookup_table_rva = convert_to_hex(data[:4])
        self.time_date_stamp = TimeDateStamp(data[4:8])
        self.forwared_chain = convert_to_hex(data[8:12])
        self.name_rva = convert_to_hex(data[12:16])
        self.thunk_table = convert_to_hex(data[16:20])
