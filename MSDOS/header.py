from utility import addition_space, get_raw
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
        res = "\tMSDOS Header:\n"

        st = vars(self).items()
        for (spec, field) in st:
            if spec != 'empty':
                res += get_raw(field, spec.lower() , 0)
        return res
