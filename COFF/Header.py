from utility import addition_space

"""
COFF Header.
0 Machine - type of target machine.
2 Number section - размер таблицы секций.
4 Time Date Stamp - временная метка.
8 Pointer to Symbol Table 
12 Number of Symbol
16 Size Option Header
18 Characteristic
"""


class COFFHeader:
    def __init__(self):
        self.empty = True
        self.mch = None
        self.nsec = None
        self.tds = None
        self.ptr = None
        self.nsb = None
        self.soh = None
        self.char = None

    def __str__(self):
        to_string = "\tCOFF Header:\n"
        to_string += (addition_space("Type target machine:")
                     + str(self.mch) + '\n')
        to_string += (addition_space("Count of section:")
                      + self.nsec.upper() + '\n')
        to_string += (addition_space("TimeDataStamp:")
                      + str(self.tds) + '\n')
        to_string += (addition_space("Pointer to Symbol table:")
                      + self.ptr.upper() + '\n')
        to_string += (addition_space("Number Symbols:")
                      + self.nsb.upper() + '\n')
        to_string += (addition_space("Size option header:")
                      + self.soh.upper() + '\n')
        to_string += (addition_space("Flags:") + '\n'
                      + str(self.char) + '\n')
        return to_string
