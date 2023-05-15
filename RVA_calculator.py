class NO_SECTION_EXCEPTION(Exception):
    pass


class RVACalculator:
    def __init__(self, table):
        self.table = table

    def resolve(self, RVA):

        for section in self.table:
            if int(section.virtual_address, 16) + int(section.virtual_size, 16) > RVA >= int(section.virtual_address, 16):
                return RVA - int(section.virtual_address, 16) + int(section.pointer_raw_data, 16)

        raise NO_SECTION_EXCEPTION
