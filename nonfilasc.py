#!/usr/bin/env python3

from urllib.parse import urlparse 

#file examples

def main():
    file = "xmp/mtrics"
    print(f"read file w/ urls:")
    with open(file) as file_:
        numb = 0
        for line in file_:
            url = urlparse(line)
            hostname = url.hostname
            path = url.path
            if hostname:
                print(f"{numb} - {line.strip()}: where hostname is {hostname} & path is {path}")
            numb += 1

if __name__ == '__main__':
    main()
    exit()
