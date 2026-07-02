# pyfishsay : A joke app where fish talk
# Ver       : 0.0.4
# Auther    : Hiroyuki Tanaka

import sys
import random

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: pyfishsay <message>")
        return

    msg1 = msg2 = ''
    msgt = [
        'ギョギョギョ！',
        'なんしようと～',
        'ヒマだね～',
        'どこ行きようと～',
        'ハラへった～',
    ]

    if random.random() < 1/3: # 1/3の確率でイベント発生
        msg2 = '... < ' + random.choice(msgt) + ' >'

    for c in args[1]:
        if   c == 'ご': msg1 += 'ぎょ'
        elif c == 'ゴ': msg1 += 'ギョ'
        else:           msg1 += c

    print()
    print('      ><(((°>', msg2 )
    print(f'   ><(((°>   ><(((°> ... < { msg1 } >')

if __name__ == "__main__":
    main()