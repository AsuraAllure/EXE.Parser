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
        self.magic = None
        self.cblp = None
        self.cp = None
        self.crlc = None
        self.cparhdr = None
        self.minalloc = None
        self.maxalloc = None
        self.ss = None
        self.sp = None
        self.csum = None
        self.ip = None
        self.cs = None
        self.lfarlc = None
        self.ovno = None
        self.oemid = None
        self.oeminfo = None
        self.pe_offset = None
        self.empty = True

    def get_raw(self, field, spec):
        value = (field
                 .upper()
                 .replace("X", 'x', 1))
        return addition_space(spec) + value + "\n"

    def __str__(self):
        to_print = "\tMSDOS Header:\n"
        to_print += self.get_raw(self.magic, "Magic number:")
        to_print += self.get_raw(self.cblp, "Bytes on last page:")
        to_print += self.get_raw(self.cp,  "Count page:")
        to_print += self.get_raw(self.crlc, "Count relocations:")
        to_print += self.get_raw(self.cparhdr, "Paragraphs in header:")
        to_print += self.get_raw(self.minalloc, "Minimum memory:")
        to_print += self.get_raw(self.maxalloc, "Maximum memory:")
        to_print += self.get_raw(self.ss, "Start offset SS register:")
        to_print += self.get_raw(self.sp, "Start offset SP register:")
        to_print += self.get_raw(self.csum, "Control summ:")
        to_print += self.get_raw(self.ip, "Start offset IP register:")
        to_print += self.get_raw(self.cs, "Start offset CS register:")
        to_print += self.get_raw(self.lfarlc, "Relocations table address:")
        to_print += self.get_raw(self.ovno, "Overlay number:")
        to_print += self.get_raw(self.oemid, "Overlay identification:")
        to_print += self.get_raw(self.oeminfo, "Overlay information:")
        to_print += self.get_raw(self.pe_offset, "Address COFF header:")
        return to_print
