import argparse
from MSDOS.Parser import MSDOSParser
from COFF.Parser import COFFParser
from MSDOS.NotExeException import NotExeFileException
from COFF.NotPEFormatException import NotPeFormat

def dumping(dump_file):
    try:
        msdos_parser = MSDOSParser(dump_file)
        msdos_header = msdos_parser.get_header()
    except NotExeFileException:
        print("File not executable")
        return
    print(msdos_header)
    dump_file.seek(int.from_bytes(msdos_header.fields["pe_offset"], "little"))

    try:
        pe_parser = COFFParser(dump_file)
        pe_header = pe_parser.get_header()
    except NotPeFormat:
        print("File not in PE format")
        return
    print(pe_header)


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
    filename = "hiew32.exe"
    try:
        file = open(filename, 'rb')
    except FileNotFoundError:
        print("No such file or directory: '{0}'".format(filename))
    else:
        with file:
            dumping(file)
