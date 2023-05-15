from utility import get_raw_flags

class Characteristic:
    def __init__(self, code):
        self.IMAGE_FILE_RELOCS_STRIPPED = hex(code & 0x0001)
        self.IMAGE_FILE_EXECUTABLE_IMAGE = hex(code & 0x0002)
        self.IMAGE_FILE_LINE_NUMS_STRIPPED = hex(code & 0x0004)
        self.IMAGE_FILE_LOCAL_SYMS_STRIPPED = hex(code & 0x0008)
        self.IMAGE_FILE_AGGRESSIVE_WS_TRIM = hex(code & 0x0010)
        self.IMAGE_FILE_LARGE_ADDRESS_AWARE = hex(code & 0x0020)
        self.IMAGE_FILE_BYTES_REVERSED_LO = hex(code & 0x0080)
        self.IMAGE_FILE_32BIT_MACHINE = hex(code & 0x0100)
        self.IMAGE_FILE_DEBUG_STRIPPED = hex(code & 0x0200)
        self.IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP = hex(code & 0x0400)
        self.IMAGE_FILE_NET_RUN_FROM_SWAP = hex(code & 0x0800)
        self.IMAGE_FILE_SYSTEM = hex(code & 0x1000)
        self.IMAGE_FILE_DLL = hex(code & 0x2000)
        self.IMAGE_FILE_UP_SYSTEM_ONLY = hex(code & 0x4000)
        self.IMAGE_FILE_BYTES_REVERSED_HI = hex(code & 0x8000)

    def __str__(self):
        res = ""
        for (field, value) in vars(self).items():
            res += get_raw_flags(value, field.lower(), 1)
        return res
