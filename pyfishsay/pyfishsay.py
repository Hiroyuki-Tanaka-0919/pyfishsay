# pyfishsay : A joke app where fish talk
# Ver       : 0.0.2
# Auther    : Hiroyuki Tanaka

import sys
import random

def main():
    args = sys.argv
    rand = ['','... < ギョギョギョ！ >',
            '','... < ヒマだね～ >',
            '']
    msg1 = ''
    msg2 = random.choice(rand)

    if len(args) < 2:
        print("Usage: pyfishsay <message>")
        return

    for c in args[1]:
        if   c == 'ご': msg1 += 'ぎょ'
        elif c == 'ゴ': msg1 += 'ギョ'
        else:           msg1 += c

    print()
    print('      ><(((°>', msg2 )
    print(f'   ><(((°>   ><(((°> ... < { msg1 } >')

if __name__ == "__main__":
    main()