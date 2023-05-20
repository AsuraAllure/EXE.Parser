from utility import convert_to_hex, get_raw, get_raw_flags, addition_space


class WindowsSpecific32Fields:
    def __init__(self, file):
        self.image_base = convert_to_hex(file.read(4))
        self.section_aligment = convert_to_hex(file.read(4))
        self.file_aligment = convert_to_hex(file.read(4))
        self.major_os_version = convert_to_hex(file.read(2))
        self.minor_os_version = convert_to_hex(file.read(2))
        self.major_image_version = convert_to_hex(file.read(2))
        self.minor_image_version = convert_to_hex(file.read(2))
        self.major_subsystem_version = convert_to_hex(file.read(2))
        self.minor_subsystem_version = convert_to_hex(file.read(2))
        self.win32_version = convert_to_hex(file.read(4))
        self.size_image = convert_to_hex(file.read(4))
        self.size_headers = convert_to_hex(file.read(4))
        self.check_sum = convert_to_hex(file.read(4))
        self.subsystem = WindowsSubsystem(convert_to_hex(file.read(2)))
        self.dll_characteristics = DLLCharacteristics(convert_to_hex(file.read(2)))
        self.size_stack_reserve = convert_to_hex(file.read(4))
        self.size_stack_commit = convert_to_hex(file.read(4))
        self.size_heap_reserve = convert_to_hex(file.read(4))
        self.size_heap_commit = convert_to_hex(file.read(4))
        self.loader_flags = convert_to_hex(file.read(4))
        self.number_rva_and_size = convert_to_hex(file.read(4))

    def __str__(self):
        res = ""
        for (field, value) in vars(self).items():
            if field != "dll_characteristics" and field != 'subsystem':
                res += get_raw(value, field, 1)
            else:
                if field == "subsystem":
                    res += get_raw(str(value), field, 1)
                else:
                    res += str(self.dll_characteristics)

        return res

class WindowsSpecific64Fields:
    def __init__(self, file):
        self.image_base = convert_to_hex(file.read(8))
        self.section_aligment = convert_to_hex(file.read(4))
        self.file_aligment = convert_to_hex(file.read(4))
        self.major_os_version = convert_to_hex(file.read(2))
        self.minor_os_version = convert_to_hex(file.read(2))
        self.major_image_version = convert_to_hex(file.read(2))
        self.minor_image_version = convert_to_hex(file.read(2))
        self.major_subsystem_version = convert_to_hex(file.read(2))
        self.minor_subsystem_version = convert_to_hex(file.read(2))
        self.win32_version = convert_to_hex(file.read(4))
        self.size_image = convert_to_hex(file.read(4))
        self.size_headers = convert_to_hex(file.read(4))
        self.check_sum = convert_to_hex(file.read(4))
        self.subsystem = WindowsSubsystem(convert_to_hex(file.read(2)))
        self.dll_characteristics = DLLCharacteristics(convert_to_hex(file.read(2)))
        self.size_stack_reserve = convert_to_hex(file.read(8))
        self.size_stack_commit = convert_to_hex(file.read(8))
        self.size_heap_reserve = convert_to_hex(file.read(8))
        self.size_heap_commit = convert_to_hex(file.read(8))
        self.loader_flags = convert_to_hex(file.read(4))
        self.number_rva_and_size = convert_to_hex(file.read(4))

    def __str__(self):
        res = ""
        for (field, value) in vars(self).items():
            if field != "dll_characteristics" and field != 'subsystem':
                res += get_raw(value, field, 1)
            else:
                if field == "subsystem":
                    res += get_raw(str(value), field, 1)
                else:
                    res += str(self.dll_characteristics)

        return res


class WindowsSubsystem:
    def __init__(self, code):
        self.code = code.upper()

    def __str__(self):
        switcher = {
            '0X0': "unknown",
            '0X1': "Device drivers and native Windows processes",
            '0X2': "The Windows graphical user interface (GUI) subsystem",
            '0X3': "The Windows character subsystem",
            '0X5': "The OS/2 character subsystem",
            '0X7': "The Posix character subsystem",
            '0X8': "Native Win9x driver",
            '0X9': "Windows CE",
            '0XA': "An Extensible Firmware Interface (EFI) application",
            '0XB': "An EFI driver with boot services",
            '0XC': "An EFI driver with run-time services",
            '0XD': "An EFI ROM image",
            '0XE': "XBOX",
            '0X10': "Windows boot application"
        }
        return switcher[self.code]


class DLLCharacteristics:
    def __init__(self, bytes):
        bytes = int(bytes, 16)
        self.IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA = bytes & 0x0020
        self.IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE = bytes & 0x0040
        self.IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY = bytes & 0x0080
        self.IMAGE_DLLCHARACTERISTICS_NX_COMPAT = bytes & 0x0100
        self.IMAGE_DLLCHARACTERISTICS_NO_ISOLATION = bytes & 0x0200
        self.IMAGE_DLLCHARACTERISTICS_NO_SEH = bytes & 0x0400
        self.IMAGE_DLLCHARACTERISTICS_NO_BIND = bytes & 0x0800
        self.IMAGE_DLLCHARACTERISTICS_APPCONTAINER = bytes & 0x1000
        self.IMAGE_DLLCHARACTERISTICS_WDM_DRIVER = bytes & 0x2000
        self.IMAGE_DLLCHARACTERISTICS_GUARD_CF = bytes & 0x4000
        self.IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE = bytes & 0x8000

    def __str__(self):
        res = "\tDLL Characteristics:\n"
        for (field, value) in vars(self).items():
            res += get_raw_flags(hex(value), field.lower(), 2)
        return res
