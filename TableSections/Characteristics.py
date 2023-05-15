from utility import get_raw_flags


class Characteristics:
    def __init__(self, code):
        self.IMAGE_TYPE_NO_PAD = hex(code & 0x00000008)
        self.IMAGE_CONTAINT_CODE = hex(code & 0x00000020)
        self.IMAGE_CONTAINT_INITIALIZED_DATA = hex(code & 0x00000040)
        self.IMAGE_CONTAINT_UNINITIALIZED_DATA = hex(code & 0x00000080)
        self.IMAGE_LINK_INFO = hex(code & 0x00000200)
        self.IMAGE_LINK_REMOVE = hex(code & 0x00000800)
        self.IMAGE_LINK_COMDAT = hex(code & 0x00001000)
        self.IMAGE_GLOBAL_POINTER_RELOCATIONS = hex(code & 0x00008000)
        self.IMAGE_LINK_NRELOC_OVFL = hex(code & 0x01000000)
        self.IMAGE_MEMORY_DISCARDABLE = hex(code & 0x02000000)
        self.IMAGE_MEMORY_NOT_CACHED = hex(code & 0x04000000)
        self.IMAGE_MEMORY_NOT_PAGED = hex(code & 0x08000000)
        self.IMAGE_MEMORY_SHARED = hex(code & 0x10000000)
        self.IMAGE_MEMORY_EXECUTE = hex(code & 0x20000000)
        self.IMAGE_MEMORY_READ = hex(code & 0x40000000)
        self.IMAGE_MEMORY_WRITE = hex(code & 0x80000000)

    def __str__(self):
        st = "\tCharacteristics:\n"
        for (field, value) in vars(self).items():
            st += get_raw_flags(value, field, 2)
        return st
