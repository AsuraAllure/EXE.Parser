import argparse
import os

from MSDOS.parser import MSDOSParser
from COFF.parser import COFFParser
from code_parser.pars import parse_code
from export_table.parser import ExportTableParser
from optional.parser import OptionalParser
from table_sections.parser import SectionTableParser
from import_table.parser import ImportTableParser
from pathlib import Path

from MSDOS.not_exe_exception import NotExeFileException
from COFF.not_PE_format_exception import NotPeFormat
from optional.errors import OptionalHeaderParseError
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

        base_code = int(optional_header.standart.base_code, 16)
        size_code = int(rva_calc.get_size_section_by_rva(base_code),16)

        offset_code = rva_calc.resolve(base_code)

        file.seek(offset_code)

        bin_dir_path = Path(
            os.path.join(
                os.path.dirname(__file__),
                'bin'
            )
        )
        if not bin_dir_path.exists():
            os.mkdir(bin_dir_path)

        bin_file_path = Path(
            os.path.join(
                bin_dir_path,
                filename + '.txt'
            )
        )

        with open(bin_file_path, 'w') as bin_file:
            parse_code(file, bin_file, size_code)

    except NotExeFileException:
        print("File not executable")
    except NotPeFormat:
        print("File not in PE format")
    except OptionalHeaderParseError as e:
        print(e)
    except NO_SECTION_EXCEPTION:
        print("Dont search sections")
    except FileNotFoundError:
        print("Cant create text_bin file")


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
    filename = "sqlceqp35.dll"
    # filename = "hiew32.exe"
    try:
        file = open(filename, 'rb')
    except FileNotFoundError:
        print("No such file or directory: '{0}'".format(filename))
    else:
        with file:
            dumping(file)
