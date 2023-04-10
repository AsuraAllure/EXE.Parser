from utility import addition_space
from utility import convert_to_hex

"""
MSDOS Header.
0	magic;		    - Сигнатура заголовка
2	cblp;		    - количество байт на последней странице файла
4	cp;		        - количество страниц в файле
6	crlc;		    - Relocations
8	cparhdr;		- Размер заголовка в параграфах
A	minalloc;		- Минимальные дополнительные параграфы
C	maxalloc;		- Максимальные дополнительные параграфы
E	ss;		        - начальное  относительное значение регистра SS
10	sp;		        - начальное значение регистра SP
12	csum;		    - контрольная сумма
14	ip;		        - начальное значение регистра IP
16	cs;		        - начальное относительное значение регистра CS
18	lfarlc;		    - адрес в файле на таблицу переадресации
1A	ovno;		    - количество оверлеев
1C	res[4];		    - Зарезервировано
24	oemid;		    - OEM идентифкатор
26	oeminfo;		- OEM информация
28	res2[10];		- Зарезервировано
3C	pe_offset;		- адрес в файле нового .exe заголовка (COFF)
"""



class MSDOSHeader:
    def __init__(self):
        self.fields = {
            "magic": None,
            "cblp": None,
            "cp": None,
            "crlc": None,
            "cparhdr": None,
            "minalloc": None,
            "maxalloc": None,
            "ss": None,
            "sp": None,
            "csum": None,
            "ip": None,
            "cs": None,
            "lfarlc": None,
            "ovno": None,
            "oemid": None,
            "oeminfo": None,
            "pe_offset": None
        }
        self.empty = True

    def get_raw(self, field, spec):
        value = (str(convert_to_hex(self.fields[field]))
                 .upper()
                 .replace("X", 'x', 1))
        return addition_space(spec) + value + "\n"

    def __str__(self):
        to_print = "\tMSDOS Header:\n"
        to_print += self.get_raw("magic", "Magic number:")
        to_print += self.get_raw("cblp", "Bytes on last page:")
        to_print += self.get_raw("cp", "Count page:")
        to_print += self.get_raw("crlc", "Count relocations:")
        to_print += self.get_raw("cparhdr", "Paragraphs in header:")
        to_print += self.get_raw("minalloc", "Minimum memory:")
        to_print += self.get_raw("maxalloc", "Maximum memory:")
        to_print += self.get_raw("ss", "Start offset SS register:")
        to_print += self.get_raw("sp", "Start offset SP register:")
        to_print += self.get_raw("csum", "Control summ:")
        to_print += self.get_raw("ip", "Start offset IP register:")
        to_print += self.get_raw("cs", "Start offset CS register:")
        to_print += self.get_raw("lfarlc", "Relocations table address:")
        to_print += self.get_raw("ovno", "Overlay number:")
        to_print += self.get_raw("oemid", "Overlay identification:")
        to_print += self.get_raw("oeminfo", "Overlay information:")
        to_print += self.get_raw("pe_offset", "Address COFF header:")
        return to_print
