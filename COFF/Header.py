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
        self.fields = {
            "mch": None,
            "nsec": None,
            "tds": None,
            "ptr": None,
            "nsb": None,
            "soh": None,
            "char": None
        }

    def __str__(self):
        to_string = (addition_space("Type target machine:")
                     + str(self.fields["mch"]) + '\n')
        to_string += (addition_space("Count of section:")
                      + self.fields["nsec"] + '\n')
        to_string += (addition_space("TimeDataStamp:")
                      + str(self.fields["tds"]) + '\n')
        to_string += (addition_space("Pointer to Symbol table:")
                      + self.fields["ptr"] + '\n')
        to_string += (addition_space("Number Symbols:")
                      + self.fields["nsb"] + '\n')
        to_string += (addition_space("Size option header:")
                      + str(self.fields["soh"]) + '\n')
        to_string += (addition_space("Flags:") + '\n'
                      + str(self.fields["char"]) + '\n')
        return to_string
