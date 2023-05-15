from utility import get_raw

PE32_MAGIC = b'\x0b\x01'
PE64_MAGIC = b'\x0b\x02'


class OptionalHeader:
    def __init__(self):
        self.empty = True
        self.standart = None
        self.windows_specific = None
        self.data = None

    def __str__(self):
        st = "\tOptional Header\n"
        st +=  "Standart:" + str(self.standart) +'\n'
        st += "Windows Specifics:\n" + str(self.windows_specific)+'\n'
        st += "Data Directories:" + str(self.data) + '\n'
        return st
