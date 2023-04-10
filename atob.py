#!/bin/python
from PIL import Image

raw = "                ______________________________________        "\
"               /_____________________________________/        "\
"              //                                    /         "\
"             //|   .____________________________.  /          "\
"            // |   |                            | /           "\
"           //  |   |                            |/            "\
"          //   |   |                            /             "\
"         //    |   |___________________________/              "\
"      __//     |                              /_______________"\
"      __/      |                             |________________"\
"     - |       |                               |              "\
"     | |       |                               |              "\
"0.95m| |       |                               |              "\
"     | |       |                               |              "\
"     - |       |__                             |              "\
"     | |      /  /|                            |              "\
"     | |     /  / |____________________________| 2.80m        "\
"     | |    /  / /___-_________________________|              "\
"1.45m| |   /  / /   /                          |              "\
"     | |  /  / /   /                           |              "\
"     | | /  / /   /2.475m                      |              "\
"     - |/__/ /   /                             |              "\
"0.40m| |   |/   /                             /|              "\
"     - |___/   -                             /_|______________"\
"                                                              "\
"       |---|--------------------------------|--|              "\
"       0.30m             4.05m              0.15m             "\
"                                                              "\
"       |---------------------------------------|              "\
"                         4.50m                                "
w,h = 62, 30
img = Image.new("1", (w * 4, h * 8))
pix = img.load()

def hline(x, y, l):
    global pix
    for a in range(l):
        pix[x + a, y] = (255)

def vline(x, y, l):
    global pix
    for a in range(l):
        pix[x, y + a] = (255)
def sevenseg(x, y, s):
    global pix
    if s[0] == '1':
        hline(x * 4 + 1, y * 8 + 1, 3)
    if s[3] == '1':
        hline(x * 4 + 1, y * 8 + 4, 3)
    if s[6] == '1':
        hline(x * 4 + 1, y * 8 + 7, 3)

    if s[1] == '1':
        vline(x * 4 + 1, y * 8 + 2, 2)
    if s[4] == '1':
        vline(x * 4 + 1, y * 8 + 5, 2)

    if s[2] == '1':
        vline(x * 4 + 3, y * 8 + 2, 2)
    if s[5] == '1':
        vline(x * 4 + 3, y * 8 + 5, 2)

for x in range(w):
    for y in range(h):
        c = raw[x + y * w]
        if c == '_':
            hline(x * 4, y * 8 + 7, 4)
        elif c == '-':
            hline(x * 4, y * 8 + 3, 4)
        elif c == '|':
            vline(x * 4 + 2, y * 8, 8)
        elif c == '/':
            for i in range(8):
                pix[x * 4 + (4 - i // 2), y * 8 + i] = (255)
        elif c == '\\':
            for i in range(8):
                pix[x * 4 + i // 2, y * 8 + i] = (255)
        elif c == '.':
            pix[x * 4 + 2, y * 8 + 7] = (255)
        elif c == '0':
            sevenseg(x, y, "1110111")
        elif c == '1':
            sevenseg(x, y, "0010010")
        elif c == '2':
            sevenseg(x, y, "1011101")
        elif c == '3':
            sevenseg(x, y, "1011011")
        elif c == '4':
            sevenseg(x, y, "0111010")
        elif c == '5':
            sevenseg(x, y, "1101011")
        elif c == '6':
            sevenseg(x, y, "1101111")
        elif c == '7':
            sevenseg(x, y, "1010010")
        elif c == '8':
            sevenseg(x, y, "1111111")
        elif c == '9':
            sevenseg(x, y, "1111011")
        elif c == 'm':
            pix[x * 4, y * 8 + 3] = (255)
            pix[x * 4 + 2, y * 8 + 3] = (255)
            vline(x * 4 + 1, y * 8 + 4, 4)
            vline(x * 4 + 3, y * 8 + 4, 4)

img.save(input("Save to "))
