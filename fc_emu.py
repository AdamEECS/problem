from asm_dict import d, d_bytes


def load_file(file):
    with open(file, 'rb') as f:
        c = f.read()
    return c


def file_to_asm(file):
    s = load_file(file)
    length = 0
    for i in range(16, 30):
        opcode = '{:02x}'.format(s[i])
        if length == 0:
            ins = d.get(opcode)
            length = d_bytes.get(opcode, 0)
        else:
            ins = ''
        # print(opcode, ins)
        print('{:02} {:08b} {} {}'.format(i, s[i], opcode, ins))
        length -= 1


def main():
    file_to_asm('mario.nes')


if __name__ == '__main__':
    main()
