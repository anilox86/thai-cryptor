#!/usr/bin/python3

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

reps = {'A':'ฤ',
        'B':'\ฺ',
        'C':'ฉ',
        'D':'ฏ',
        'E':'ฎ',
        'F':'โ',
        'G':'ฌ',
        'H':'\็',
        'I':'ณ',
        'J':'\๋',
        'K':'ษ',
        'L':'ศ',
        'M':'?',
        'N':'\์',
        'O':'ฯ',
        'P':'ญ',
        'Q':'๐',
        'R':'ฑ',
        'S':'ฆ',
        'T':'ธ',
        'U':'\๊',
        'V':'ฮ',
        'W':'"',
        'X':')',
        'Y':'\ํ',
        'Z':'(',
        'a':'ฟ',
        'b':'\ิ',
        'c':'แ',
        'd':'ก',
        'e':'ำ',
        'f':'ด',
        'g':'เ',
        'h':'\้',
        'i':'ร',
        'j':'\่',
        'k':'า',
        'l':'ส',
        'm':'ท',
        'n':'\ื',
        'o':'น',
        'p':'ย',
        'q':'ๆ',
        'r':'พ',
        's':'ห',
        't':'ะ',
        'u':'\ี',
        'v':'อ',
        'w':'ไ',
        'x':'ป',
        'y':'\ั',
        'z':'ผ',
        '0':'จ',
        '1':'ๅ',
        '2':'/',
        '3':'-',
        '4':'ภ',
        '5':'ถ',
        '6':'\ุ',
        '7':'\ึ',
        '8':'ค',
        '9':'ต',
        '^':'\ู',
        '-':'ข',
        '=':'ช',
        ',':'ม',
        '.':'ใ',
        '/':'ฝ',
        '<':'ฒ',
        '>':'ฬ',
        '?':'ฦ',
        ';':'ว',
        '\'':'ง',
        '[':'บ',
        ']':'ล',
        ':':'ซ',
        '\"':'.',
        '{':'ฐ',
        '}':',',
        '|':'ฅ',
        '\\':'ฃ'
        }
sp = { '\\':'' }


def main():
    write_file = open("out.txt", "w")
    try:
        with open("in.txt", "r") as fan:
            lines = fan.read().splitlines()

        for line in lines:
            txt = replace_all(line, reps)
            txt2 = replace_all(txt, sp)
            write_file.write(txt2 + "\n")
    except:
        print("please create in.txt and put text you want to decrypt in it")
    finally:
        write_file.close()


if(__name__ == "__main__"):
    main()
