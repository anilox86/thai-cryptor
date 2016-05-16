#!/usr/bin/python3

import sys

def decrypt_eng(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def encrypt_eng(text, dic):
    for i, j in dic.items():
        text = text.replace(j, i)
    return text

def print_usage():
    print("Usage: thai-cryptor <command> [<file1>] [<file2>] ...\n\
\n\
command:\n\
    decrypt     replace english to thai\n\
    encrypt     replace thai to english\n\
\n\
Examples:\n\
    ./thai-cryptor decrypt\n\
    ./thai-cryptor encrypt sometextfile.txt\n\
    ./thai-cryptor decrypt file1.txt file2.txt file3.txt\n\
\n\
Then check your output in out.txt")
    return

def dec(list_in):
    write_file = open("out.txt", "w")
    try:
        for i in list_in:
            with open(i, "r") as fan:
                lines = fan.read().splitlines()

            write_file.write("file: " + i + "\n")
            for line in lines:
                txt = decrypt_eng(line, reps)
                write_file.write(txt + "\n")
            write_file.write("\n")
    except:
        print("Error: file not found(?)")
    finally:
        write_file.close()

def enc(list_in):
    write_file = open("out.txt", "w")
    try:
        for i in list_in:
            with open(i, "r") as fan:
                lines = fan.read().splitlines()

            write_file.write("file: " + i + "\n")
            for line in lines:
                txt = encrypt_eng(line, reps)
                write_file.write(txt + "\n")
            write_file.write("\n")
    except:
        print("Error: file not found(?)")
    finally:
        write_file.close()

reps = {'A':'ฤ',
        'B':'ฺ',
        'C':'ฉ',
        'D':'ฏ',
        'E':'ฎ',
        'F':'โ',
        'G':'ฌ',
        'H':'็',
        'I':'ณ',
        'J':'๋',
        'K':'ษ',
        'L':'ศ',
        'M':'?',
        'N':'์',
        'O':'ฯ',
        'P':'ญ',
        'Q':'๐',
        'R':'ฑ',
        'S':'ฆ',
        'T':'ธ',
        'U':'๊',
        'V':'ฮ',
        'W':'"',
        'X':')',
        'Y':'ํ',
        'Z':'(',
        'a':'ฟ',
        'b':'ิ',
        'c':'แ',
        'd':'ก',
        'e':'ำ',
        'f':'ด',
        'g':'เ',
        'h':'้',
        'i':'ร',
        'j':'่',
        'k':'า',
        'l':'ส',
        'm':'ท',
        'n':'ื',
        'o':'น',
        'p':'ย',
        'q':'ๆ',
        'r':'พ',
        's':'ห',
        't':'ะ',
        'u':'ี',
        'v':'อ',
        'w':'ไ',
        'x':'ป',
        'y':'ั',
        'z':'ผ',
        '0':'จ',
        '1':'ๅ',
#        '2':'/',
#        '3':'-',
        '4':'ภ',
        '5':'ถ',
        '6':'ุ',
        '7':'ึ',
        '8':'ค',
        '9':'ต',
        '^':'ู',
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
#        '\"':'.',
#        '}':',',
#        '|':'ฅ',
#        '\\':'ฃ',
        '{':'ฐ'
        }

def main():
    if(len(sys.argv) < 2):
        print_usage()
        return

    elif(sys.argv[1] == 'decrypt'):
        if(len(sys.argv) > 2):
            ins = sys.argv[2:]
            for i in ins:
                print(i)
        else: # len == 2
            ins = ["in.txt"]
        dec(ins)
        return

    elif(sys.argv[1] == 'encrypt'):
        if(len(sys.argv) > 2):
            ins = sys.argv[2:]
            for i in ins:
                print(i)
        else: # len == 2
            ins = ["in.txt"]
        enc(ins)
        return

    else:
        print_usage()
        return


if(__name__ == "__main__"):
    main()
