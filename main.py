import argparse
from MSDOS.parser import MSDOSParser
from COFF.parser import COFFParser
from export_table.parser import ExportDirectoriesTable, ExportTableParser
from optional.parser import OptionalParser
from table_sections.parser import SectionTableParser
from import_table.parser import ImportTableParser

from MSDOS.not_exe_exception import NotExeFileException
from COFF.not_PE_format_exception import NotPeFormat
from optional.errors import OptionalHeaderParseError
from RVA_calculator import NO_SECTION_EXCEPTION

from RVA_calculator import RVACalculator


def dumping(dump_file):
    try:

        #file.seek(int("0x8E20", 16))
        #print(file.read(100))

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
        rva_calc = RVACalculator(table_sections.sections)

        export_table_section = optional_header.data.directories[0]

        if export_table_section.size == "0x0":
            print("No Export Table\n")
        else:
            export_rva = int(export_table_section.virtual_address, 16)
            offset = rva_calc.resolve(export_rva)
            dump_file.seek(offset)
            export_table_parser = ExportTableParser(dump_file, int(export_table_section.size, 16), rva_calc)
            print(export_table_parser)

        import_table_section = optional_header.data.directories[1]
        if import_table_section.size == "0x0":
            print("No Import Table\n")
        else:
            import_rva = int(import_table_section.virtual_address, 16)
            offset = rva_calc.resolve(import_rva)
            dump_file.seek(offset)
            import_table_parser = ImportTableParser(
                dump_file,
                int(import_table_section.size, 16),
                rva_calc,
                optional_header.standart.magic
            )
            print(import_table_parser)


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

    #args = vars(parser.parse_args())
    #filename = args["filename"][0]
    filename = "sqlceqp35.dll"
    #filename = "hiew32.exe"
    try:
        file = open(filename, 'rb')
    except FileNotFoundError:
        print("No such file or directory: '{0}'".format(filename))
    else:
        with file:
            dumping(file)
