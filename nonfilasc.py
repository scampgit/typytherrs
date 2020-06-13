#!/usr/bin/env python3

#file examples

def main():
    file = "xmp/mtrics"
    numb = 0
    for line in open(file):
        print(f"#{numb}: here the {line}")
        numb += 1

    print(f"*******\nwe can do:")
    with open(file) as file_:
        numb = 0
        for line in file_:
            print(f"gotcha {numb} & {line.strip()}")
            numb += 1

if __name__ == '__main__':
    main()
    exit()
