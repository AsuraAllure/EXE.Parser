import argparse
from MSDOS.Parser import MSDOSParser
from COFF.Parser import COFFParser
from Optional.Parser import OptionalParser
from TableSections.Parser import SectionTableParser
from ImportTable.Parser import ImportTableParser

from MSDOS.NotExeException import NotExeFileException
from COFF.NotPEFormatException import NotPeFormat
from Optional.Errors import OptionalHeaderParseError
from RVA_calculator import NO_SECTION_EXCEPTION

from RVA_calculator import RVACalculator


def dumping(dump_file):
    try:
        msdos_parser = MSDOSParser(dump_file)
        msdos_header = msdos_parser.get_header()
        print(msdos_header)

        cur_positions = int(msdos_header.pe_offset, 16)
        dump_file.seek(cur_positions)

        pe_parser = COFFParser(dump_file)
        pe_header = pe_parser.get_header()
        print(pe_header)

        optional_header_parser = OptionalParser(dump_file, int(pe_header.soh, 16))
        optional_header = optional_header_parser.get_header()
        print(optional_header)

        table_section_parser = SectionTableParser(dump_file, int(pe_header.nsec, 16))
        table_sections = table_section_parser.get_table()
        print(table_sections)

        import_table_section = optional_header.data.directories[1]
        import_rva = int(import_table_section.virtual_address, 16)
        rva_calc = RVACalculator(table_sections.sections)

        offset = rva_calc.resolve(import_rva)
        dump_file.seek(offset)
        import_table_bytes = dump_file.read(int(import_table_section.size, 16))

        import_table_parser = ImportTableParser(import_table_bytes)
        import_table = import_table_parser.get_table()

        print(import_table)

    except NotExeFileException:
        print("File not executable")
    except NotPeFormat:
        print("File not in PE format")
    except OptionalHeaderParseError as e:
        print(e)
    except NO_SECTION_EXCEPTION:
        print("Dont search sections")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="EXE_PARSER",
        description="This is program to dump exe file.",
        exit_on_error=False
    )
    parser.add_argument(
        "filename",
        nargs=1,
        help="Name of file, which need dump.",
        type=str
    )

    # args = vars(parser.parse_args())
    # filename = args["filename"][0]
    filename = "hiew32.exe"
    try:
        file = open(filename, 'rb')
    except FileNotFoundError:
        print("No such file or directory: '{0}'".format(filename))
    else:
        with file:
            dumping(file)
