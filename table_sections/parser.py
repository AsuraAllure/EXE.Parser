from table_sections.sections import Section


class SectionTableParser:
    def __init__(self, file, count_sections_header):
        self.sections = TableSections()
        for x in range(count_sections_header):
            sect = Section(file.read(40))
            self.sections.add_section(sect)

    def get_table(self):
        return self.sections


class TableSections:
    def __init__(self):
        self.sections = []

    def add_section(self, sect):
        self.sections.append(sect)

    def __str__(self):
        st = "\tTable Sections\n"
        for x in self.sections:
            st += str(x)+'\n'
        return st